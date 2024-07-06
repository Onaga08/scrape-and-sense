import csv
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Before anything, for the ease of further processing, I will convert the input.xlsx file 
#into a .csv file.
def convert_xlsx_to_csv():
    df = pd.read_excel('Input.xlsx')
    df.to_csv('Input.csv', index=False)

#Parsing Function to extract text
def extract_article_heading_and_body(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            #using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            heading_list = ['entry-title', 'tdb-title-text']
            heading = soup.find('h1', class_= heading_list) #Finding heading using specific class of div
            body = soup.find('div', class_= 'td-post-content tagdiv-type') #Finding body using class of div
            if body is None: #exception for diff format of article page
                body = soup.find('div', class_='td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type')

            if heading and body:
                heading_text = heading.get_text()
                body_text = body.get_text()
              
                return heading_text, body_text
            else:
                print(f"Heading or body not found on {url}")
               
                return None, None

        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            
            return None, None
    except Exception as e:
        print(f"Error while processing {url}: {e}")
        return None, None

convert_xlsx_to_csv()

#Created a directory
output_directory = 'text_files'
os.makedirs(output_directory, exist_ok=True)
csv_filename = 'Input.csv'

with open(csv_filename, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        url_id, url = row

        heading, body = extract_article_heading_and_body(url)

        if heading is not None and body is not None:
            #Creating a spearate file for each url_id
            txt_filename = os.path.join(output_directory, f'{url_id}.txt')
            with open(txt_filename, 'w', encoding='utf-8') as txtfile:
                txtfile.write(heading + '\n\n')
                txtfile.write(body)

            print(f"Processed {url_id}: {url} -> {txt_filename}")

print("Text extraction and file creation completed.")
