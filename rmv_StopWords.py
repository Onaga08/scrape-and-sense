#remove stop_words
from function import combine, remove
import os
import re

file_paths = ['Stop Words\StopWords_GenericLong.txt', 'Stop Words\StopWords_Geographic.txt', 'Stop Words\StopWords_Names.txt']
output_file_path = 'Stop Words\Stop_words_all.txt'

#Firstly, combine all the stop words to make a single .txt file
combine(file_paths, output_file_path)

#then remove the stop words from all the text files. 
input_directory = 'text_files'
output_directory = 'updated_text_files'

remove(output_file_path, input_directory, output_directory)