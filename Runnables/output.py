import pandas as pd
from function import sort_csv, compare_to_overwrite
import csv

#to arrange in ascending order:
file1 = '../Analysis.csv'
file2 = '../input.csv'
sort_csv(file1, file1)
sort_csv(file2, file2)

#to compare and to overwrite

file1_path = '../Input.csv'
file2_path = '../Analysis.csv'
output_path = '../Analysis.csv'

compare_to_overwrite(file1_path, file2_path, output_path)

