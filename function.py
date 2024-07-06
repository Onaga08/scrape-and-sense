import os
import re
import csv
import nltk
import pandas as pd
from nltk.corpus import cmudict, stopwords
from nltk import word_tokenize
import string
nltk.download('punkt')  
nltk.download('stopwords')
nltk.download('cmudict')

#Function to find no. of sentences
def count_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        text = file.read()

    sentences = nltk.sent_tokenize(text)
    return len(sentences)

def calculate_total_words(file_path):
    with open(file_path, 'r', encoding='UTF-8', errors='replace') as file:
        text = file.read()
    tokens = nltk.word_tokenize(text)
    total_words = len(tokens)
    return total_words

def combine(file_paths, output_file_path):
    #to read the first word from each line in a text file
    def read_first_words_from_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.split()[0].strip() for line in file]

    all_first_words = []

    for file_path in file_paths:
        first_words = read_first_words_from_file(file_path)
        all_first_words.extend(first_words)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for word in all_first_words:
            output_file.write(word + '\n')

    print(f"First words combined and written to '{output_file_path}'.")

def read(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        return [line.strip() for line in file]

def remove(word_list_file, input_directory, output_directory):
    #to remove the stopwords
    words_to_remove = read(word_list_file)
    os.makedirs(output_directory, exist_ok=True)
    input_files = os.listdir(input_directory)

    for input_file in input_files:
        input_file_path = os.path.join(input_directory, input_file)
        output_file_path = os.path.join(output_directory, input_file)

        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        #to remove the specified words from the text using regular expressions
        for word in words_to_remove:
            pattern = re.compile(r'\b' + re.escape(word) + r'\b')
            text = pattern.sub('', text)

        #write the cleaned text in new directory
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Processed file: '{output_file_path}'")

    print(f"Words removed from all files and saved in the '{output_directory}' directory.")
    
def syllable(word, pronouncing_dict):
    
    #I have used the CMU Pronouncing Dict. to count syllables in one word.
    if word.lower() in pronouncing_dict:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in pronouncing_dict[word.lower()]])
    else:
        return 0

def count_complex_words(file_path):
    with open(file_path, 'r', encoding='UTF-8', errors='replace') as file:
        text = file.read()   
    words = word_tokenize(text)

    pronouncing_dict = cmudict.dict()
    complex_word_count = sum(1 for word in words if syllable(word, pronouncing_dict) >= 3)
    return complex_word_count

def count_syllable(file_path):
    with open(file_path, 'r', encoding='UTF-8', errors='replace') as file:
        text = file.read()   
    words = word_tokenize(text)

    pronouncing_dict = cmudict.dict()
    Syllables = sum(1 for word in words if syllable(word, pronouncing_dict))
    return Syllables

def read_positive_negative_words(positive_file_path, negative_file_path):
    positive_words = read(positive_file_path)
    negative_words = read(negative_file_path)
    return positive_words, negative_words

def calculate_custom_sentiment_score(text, positive_words, negative_words):
    tokens = nltk.word_tokenize(text)

    #counting the occurrences of positive and negative words
    positive_count = sum(1 for token in tokens if token.lower() in positive_words)
    negative_count = sum(1 for token in tokens if token.lower() in negative_words)
    total_words = len(tokens)
    if total_words == 0:
        return 0.0, 0.0

    positive_score = positive_count 
    negative_score = negative_count

    return positive_score, negative_score, total_words

def process_file(file_path, positive_words, negative_words):
    with open(file_path, 'r', encoding='UTF-8', errors='replace') as file:
        text = file.read()

    #calculate custom sentiment scores
    positive_score, negative_score, total_words = calculate_custom_sentiment_score(text, positive_words, negative_words)

    return positive_score, negative_score, total_words

def count_words_without_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        text = file.read()    
    
    words = word_tokenize(text)

    #Remove stopwords using dict
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words and word not in string.punctuation]
    word_count = len(words)

    return word_count

def count_personal_pronouns(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        text = file.read()
    
    words = word_tokenize(text)

    #lowercase for case-insensitive matching
    words_lower = [word.lower() for word in words]
    personal_pronouns = ['i', 'we', 'my', 'ours', 'us']
    stop_words = set(stopwords.words('english'))
    words_filtered = [word for word in words_lower if word not in stop_words]
    pronoun_count = sum(1 for word in words_filtered if word in personal_pronouns)

    return pronoun_count

def characters(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        text = file.read()
        return len(text)
    
def extract_url(csv_file_path):
    second_column = []

    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            if len(row) >= 2:  
                second_column.append(row[1])

    return second_column

def sort_csv(input_path, output_path):
    df = pd.read_csv(input_path)
    df_sorted = df.sort_values(by=df.columns[0])
    df_sorted.to_csv(output_path, index=False)
    
def compare_to_overwrite(file1_path, file2_path, output_path):
    with open(file1_path, 'r', newline='') as file1:
        reader1 = csv.reader(file1)
        data1 = {row[0]: row[1] for row in reader1}

    with open(file2_path, 'r', newline='') as file2:
        reader2 = csv.reader(file2)
        data2 = list(reader2)

    #Compare and overwrite
    for row2 in data2:
        value_to_compare = row2[0]
        if value_to_compare in data1:
            row2[1] = data1[value_to_compare]

    #To write the output
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(data2)