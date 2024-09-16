import pdfkit
from pymongo import MongoClient
import os

def convert_mongodb_data_to_pdf(output_folder):
    # Set up MongoDB connection
    client = MongoClient('localhost', 27017)
    db = client['web_crawler']
    collection = db['scraped_data']

    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all documents in the collection
    for document in collection.find():
        url = document['url']
        content = document['content']
        
        # Define PDF file name based on URL
        pdf_file = os.path.join(output_folder, f"{url.split('//')[-1].split('/')[0]}.pdf")
        
        # Convert HTML content to PDF
        try:
            # Use pdfkit to convert HTML content to PDF
            pdfkit.from_string(content, pdf_file)
            print(f"Converted {url} to {pdf_file}")
        except Exception as e:
            print(f"Failed to convert {url} to PDF: {e}")

# Usage
output_directory = './mongodb_pdfs'
convert_mongodb_data_to_pdf(output_directory)
