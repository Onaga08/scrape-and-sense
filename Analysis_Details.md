# Detailed Analysis of NLP Metrics

This document provides a detailed description of the formulas and logic used in the NLP analysis for this project.

## Positive Score
- **Formula:** +1 for every word found in [Positive Dictionary](Dict/negative-words.txt).

## Negative Score
- **Formula:** +1 for every word found in [Negative Dictionary](Dict/negative-words.txt).

## Polarity Score
- **Definition:** Determines if a given text is positive or negative in nature. Range is -1 to +1 
- **Formula:** (Positive Score - Negative Score) / ((Positive Score + Negative Score) + 0.000001)

## Subjectivity Score
- **Definition:** Determines if a given text is objective or subjective in nature. Range is 0 to +1
- **Formula:** (Positive Score + Negative Score) / (Total Word Count + 0.000001)

## Average Sentence Length
- **Formula:** Total Number of Words / Total Number of Sentences

## Percentage of Complex Words
- **Formula:** (Number of Complex Words / Total Number of Words) * 100

## Fog Index
1 **Definition:** Determines the level of text difficulty, or how easy it is to read.
- **Formula:** 0.4 * (Average Sentence Length + Percentage of Complex Words)

## Average Number of Words per Sentence
- **Formula:** Total Number of Words / Total Number of Sentences

## Complex Word Count
- **Logic:** Words with two or more syllables are considered complex words.

## Word Count
- **Formula:** Total number of words in the text after removing stop words, and punctuations

## Syllables per Word
- **Formula:** Total Number of Syllables / Total Number of Words

## Personal Pronouns
- **Logic:** Count of personal pronouns (e.g., I, we, you, he, she, they). Emit country name like "US", etc.

## Average Word Length
- **Formula:** Total Number of Characters / Total Number of Words

### The runnables along with the required input and expected output of each python file is explained in [instructions.md](instructions.md)

