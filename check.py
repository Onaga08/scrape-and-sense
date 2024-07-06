#This is a code to check if all the files are correctly written. It checks if all the files 
#have more than 3 lines, which gives us an idea if any article was not extracted.
import os
import chardet

directory = 'text_files'
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        
        #To detect encoding
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            encoding_info = chardet.detect(raw_data)
            file_encoding = encoding_info['encoding']
        
        
        with open(file_path, 'r', encoding=file_encoding, errors='ignore') as file:
            lines = file.readlines()
        
        #To check if the file has more than 3 lines
        if len(lines) < 3:
            print(f"{filename} has less than 3 lines.")
print("Checking Complete!")

