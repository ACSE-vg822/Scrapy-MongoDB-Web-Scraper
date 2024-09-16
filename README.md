# Scrapy-MongoDB-Web-Scraper
Scrape the web by using just some keywords!

# Web Scraper Setup Guide
This guide will help you set up a web scraping environment using Scrapy and MongoDB on Ubuntu/Debian Linux systems.

# 1. Create and Activate a Virtual Environment
python3 -m venv scraper
source scraper/bin/activate

# 2. Install Required Python Packages
pip install -r requiremnts.txt

# 3. Install MongoDB

## Step 1: Import the MongoDB Public Key
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

## Step 2: Create the MongoDB Source List File
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

## Step 3: Update the Package Database
sudo apt-get update

## Step 4: Install MongoDB
sudo apt-get install -y mongodb-org

# 4. Create Data Directory for MongoDB
mkdir -p ~/path/to/your/project/data/db

# 5. Start the MongoDB Server
mongod --dbpath ~/path/to/your/project/data/db

# 6. (Optional) Configure MongoDB for WSL
## If you are using WSL, you may also want to specify a different port or use configuration files:
mongod --dbpath ~/data/db --bind_ip 0.0.0.0 --port 27017

# 7. Connect to the MongoDB Server in a new terminal window
mongo

## If you encounter an error:
sudo apt update
sudo apt install mongodb-clients

# 8. Run the Scrapy Spider
# Go to the folder containing the scrapy.cfg file:
cd webcrawler
scrapy crawl spider -a keywords="climate change" # You can add whatever keyword you want to scrape for

