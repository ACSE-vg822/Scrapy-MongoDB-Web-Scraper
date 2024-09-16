# 🕷️ Scrapy-MongoDB Web Scraper  
Effortlessly scrape the web using just a few keywords!

## 📖 Table of Contents
- [Overview](#overview)
- [Setup Guide](#setup-guide)
  - [1. Create and Activate a Virtual Environment](#1-create-and-activate-a-virtual-environment)
  - [2. Install Required Python Packages](#2-install-required-python-packages)
  - [3. Install MongoDB](#3-install-mongodb)
  - [4. Create Data Directory for MongoDB](#4-create-data-directory-for-mongodb)
  - [5. Start the MongoDB Server](#5-start-the-mongodb-server)
  - [6. (Optional) Configure MongoDB for WSL](#6-optional-configure-mongodb-for-wsl)
  - [7. Connect to the MongoDB Server](#7-connect-to-the-mongodb-server)
  - [8. Run the Scrapy Spider](#8-run-the-scrapy-spider)

## 📝 Overview
This guide walks you through setting up a web scraping environment using Scrapy and MongoDB on Ubuntu/Debian Linux systems. With just a few keywords, you'll be able to scrape the web and store the results in a MongoDB database.

## 🛠️ Setup Guide

### 1. Create and Activate a Virtual Environment
```bash
python3 -m venv scraper
source scraper/bin/activate
```

### 2. Install Required Python Packages
```bash
pip install -r requirements.txt
```
### 3. Install MongoDB
#### Step 1: Import the MongoDB Public Key
```bash
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
```
#### Step 2: Create the MongoDB Source List File
```bash
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```
#### Step 3: Update the Package Database
```bash
sudo apt-get update
```
#### Step 4: Install MongoDB
```bash
sudo apt-get install -y mongodb-org
```
### 4. Create Data Directory for MongoDB
```bash
mkdir -p ~/path/to/your/project/data/db
```
### 5. Start the MongoDB Server
```bash
mongod --dbpath ~/path/to/your/project/data/db
```
### 6. (Optional) Configure MongoDB for WSL
If you are using WSL, you may want to specify a different port or use configuration files:
```bash
mongod --dbpath ~/data/db --bind_ip 0.0.0.0 --port 27017
```
### 7. Connect to the MongoDB Server
Open a new terminal window and connect to the MongoDB server:
```bash
mongo
```
If you encounter an error, run:
```bash
sudo apt update
sudo apt install mongodb-clients
```

### 8. Run the Scrapy Spider
```bash
cd webcrawler
scrapy crawl spider -a keywords="climate change" # You can add whatever keyword you want to scrape for
```