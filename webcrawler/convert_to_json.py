import json
from pymongo import MongoClient
import os

def convert_mongodb_data_to_json(output_folder):
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
        
        # Define JSON file name based on URL (sanitized to avoid invalid filenames)
        json_filename = url.split('//')[-1].split('/')[0].replace('.', '_') + '.json'
        json_file_path = os.path.join(output_folder, json_filename)

        # Convert document to a dictionary and remove MongoDB's internal `_id` field
        document_dict = {
            'url': url,
            'content': content
        }

        # Save the document as a JSON file
        try:
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(document_dict, json_file, ensure_ascii=False, indent=4)
            print(f"Converted {url} to {json_file_path}")
        except Exception as e:
            print(f"Failed to convert {url} to JSON: {e}")

# Usage
output_directory = './mongodb_jsons'
convert_mongodb_data_to_json(output_directory)
