import sys
import os
import requests  # To download PDF files
from urllib.parse import urljoin  # To handle relative URLs
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")

from generate_urls import generate_urls_from_duckduckgo  # Import the URL generator function

import scrapy
from pymongo import MongoClient

class Spider(scrapy.Spider):
    name = 'spider'
    
    def __init__(self, keywords=None, *args, **kwargs):
        super(Spider, self).__init__(*args, **kwargs)
        
        # Set up MongoDB connection (customize the host and port if needed)
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['web_crawler']  # Use a generic database
        self.collection = self.db['scraped_data']  # Use a generic collection

        # Generate start URLs based on the provided keywords using DuckDuckGo
        if keywords:
            # Split the keywords by comma and strip whitespace
            keyword_list = [kw.strip() for kw in keywords.split(',')]
            self.start_urls = generate_urls_from_duckduckgo(keyword_list, max_results=10)
        else:
            self.start_urls = []  # Empty if no keywords provided

    def parse(self, response):
        # Extract the main content of the webpage
        content = response.xpath('//body').get()

        # Save data to MongoDB
        data = {
            'url': response.url,
            'content': content,
        }
        self.collection.insert_one(data)
        self.log(f"Saved {response.url} to MongoDB")

        # Download any existing PDFs on this page
        pdf_links = response.css('a[href$=".pdf"]::attr(href)').extract()
        for pdf_link in pdf_links:
            pdf_url = urljoin(response.url, pdf_link)
            self.download_pdf(pdf_url)

        # Follow links on the page to scrape more pages
        for href in response.css('a::attr(href)').extract():
            # Generate absolute URLs for each link
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse)

    def download_pdf(self, pdf_url):
        """Download PDF file from the given URL."""
        # Directory to store downloaded PDFs
        pdf_directory = './mongodb_pdfs'
        if not os.path.exists(pdf_directory):
            os.makedirs(pdf_directory)

        # Get the filename from the URL
        filename = os.path.join(pdf_directory, pdf_url.split('/')[-1])

        # Download the PDF file
        try:
            self.log(f"Downloading PDF: {pdf_url}")
            response = requests.get(pdf_url, stream=True)
            response.raise_for_status()  # Ensure we notice bad responses
            with open(filename, 'wb') as pdf_file:
                for chunk in response.iter_content(chunk_size=8192):
                    pdf_file.write(chunk)
            self.log(f"Saved PDF: {filename}")
        except Exception as e:
            self.log(f"Failed to download {pdf_url}: {e}")
