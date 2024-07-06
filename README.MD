# Scrape & Sense
A comprehensive script for web scraping and NLP analysis, providing detailed insights from extracted articles. 

# Description
<p><b>Scrape & Sense </b> is a web scraping and NLP project that analyzes sentiment and readability metrics of articles extracted from websites. Using Natural Language Processing techniques, it computes Positive Score, Negative Score, Polarity Score, Subjectivity Score, and readability metrics like Average Sentence Length, Percentage of Complex Words, and Fog Index. </p>

<p>
The workflow includes scripts for data extraction, stop word removal, and analysis, ensuring reproducibility with detailed setup instructions. Results are in CSV format for easy interpretation and further analysis.
</p>

# Getting Started

## Installation

Put the following command in your terminal/cmd after traversing to the designated folder

```bash
```
This repository uses several Python libraries and dependencies. Install all requirements through the command below.

```bash
pip install -r requirements.txt
```

## Usage

This project has two broad functions: 
1. Web Scraping Using BeautifulSoup
2. NLP Analysis

The runnables along with the required input and expected output of each python file is explained in [instructions.md](instructions.md)

## Pre-Requisite Directories/Files
1. Input.xlsx - Contains link for articles hosted on BlackCoffer website.
2. Dict/ - Contains txt files for positive-words and negative-words analysis
3. Stop Words/ - Contains txt files of three different types of Stop_Words

