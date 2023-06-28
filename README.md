# Intent Extraction using Natural Language Processing

The proposed system will accept text or csv file as an input from user for further extraction process. 

## Pre-Process:
Pre-processing aims to process and present the reviews in an organized format and increase the machine understanding on the text, as most reviews are in the form of unstructured text. It includes Stopwords, Empty Spaces, repeated words, multiple special characters. Removal of Stop Words and Empty Spaces are removed from the text as they do not carry meanings. Repeated words and multiple special characters are removed from the text to avoid confusion. Sentence and Word Separation is done as system receive multiple sentence as an input. So, to process each sentence and Word separation is done.

## Sentiment Classification:
Sentiment Classification aims on sentiment analysis and extract keywords based on the analysis. POS [Parts of Speech] identification is done of every word in the sentence and tokenization is carried out each word will get tokenized and tagged with verb, noun, adjective, etc. attenuations. Based on the tokenized attenuations finally analysis is done and keywords are extracted from the sentence. The final output is displayed and saved into the CSV file with appropriate column name.
