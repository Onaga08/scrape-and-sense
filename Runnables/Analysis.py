import os
import csv
import nltk
from nltk import word_tokenize
from nltk.corpus import cmudict, stopwords
from function import count_sentences, calculate_total_words, count_complex_words, read_positive_negative_words
from function import process_file, count_words_without_stopwords, count_personal_pronouns, characters, extract_url
from function import count_syllable

#code wont work without downloading the Punkt Tokenizer Model
nltk.download('punkt')  
nltk.download('stopwords')
nltk.download('cmudict')

def analyze_files(directory_path, positive_file_path, negative_file_path, output_csv_path):
    positive_words, negative_words = read_positive_negative_words(positive_file_path, negative_file_path)
    

    files = os.listdir(directory_path)

    with open(output_csv_path, 'w', newline='', encoding='UTF-8', errors='replace') as csv_file:
        fieldnames = ['URL_ID','URL', 'Positive Score', 'Negative Score', 'Polarity Score', 'Subjectivity Score', 'Average Sentence Length'
                      ,'Percentage of Complex words', 'Fog Index', 'Avg Number of Words', 'Complex Word Count', 'Word Count', 
                      'Syllable per Word', 'Personal Pronouns', 'Avg Word Length']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        #This is the main processing portion of all variables.
        for file_name in files:
            file_path = os.path.join(directory_path, file_name)
            name = file_name.rsplit('.',1)[0]
            positive_score, negative_score, total_words = process_file(file_path, positive_words, negative_words)
            polarity_score = (positive_score - negative_score)/ ((positive_score + negative_score) + 0.000001)
            subjectivity_score = (positive_score + negative_score)/((total_words)+0.000001)
            sentence_count = count_sentences(file_path)
            total_words_in_OG = calculate_total_words(file_path)
            avg_sentence_length = total_words_in_OG/sentence_count
            complex_words = count_complex_words(file_path)
            percent_complex_words = (complex_words/total_words_in_OG)*100
            fog_index = 0.4*(avg_sentence_length + percent_complex_words)
            avg_words_per_sentence = total_words_in_OG/sentence_count
            word_count = count_words_without_stopwords(file_path)
            
            #for Syllable count 
            syllables = count_syllable(file_path)
            
            #to count personal pronouns 
            personal_pronouns = count_personal_pronouns(file_path)
            
            #For Avg Word Length
            character = characters(file_path)
            avg_word_length = character/total_words_in_OG
            
            
            
            writer.writerow({
                'URL_ID': name,
                'URL': "-",
                'Positive Score': positive_score,
                'Negative Score': negative_score,
                'Polarity Score': polarity_score,
                'Subjectivity Score': subjectivity_score,
                'Average Sentence Length': avg_sentence_length,
                'Percentage of Complex words': percent_complex_words,
                'Fog Index': fog_index,
                'Avg Number of Words': avg_words_per_sentence,
                'Complex Word Count': complex_words,
                'Word Count': word_count,
                'Syllable per Word': syllables,
                'Personal Pronouns': personal_pronouns,
                'Avg Word Length': avg_word_length,
            })

#driver function
directory_path = 'updated_text_files'
positive_file_path = 'Dict\positive-words.txt'
negative_file_path = 'Dict\negative-words.txt'
output_csv_path = 'Analysis.csv'

analyze_files(directory_path, positive_file_path, negative_file_path, output_csv_path)
