# -*- coding: utf-8 -*-
"""EntityFinder.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R3-3y_W8vv7JYhi9v8g5sUGdhnvsz3Oy
"""

!pip install spacy
!python -m spacy download en_core_web_sm

import spacy
import pandas as pd
import re

# Load the SpaCy pre-trained English NER model
nlp = spacy.load("en_core_web_sm")

# Load the dataset (assuming it's a txt file)
with open('/content/dialog.txt', 'r', encoding='ISO-8859-1')  as file:
    dialogues = file.readlines()

# Simple cleaning function
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    text = text.lower().strip()  # Convert to lowercase and remove leading/trailing spaces
    return text

# Clean dialogues
cleaned_dialogues = [clean_text(dialogue) for dialogue in dialogues]

# Preview cleaned dialogues
print(cleaned_dialogues[:5])

import spacy
import re

# Load the SpaCy pre-trained English NER model
nlp = spacy.load("en_core_web_sm")

# Load the dataset (assuming it's a txt file)
with open('/content/dialog.txt', 'r', encoding='ISO-8859-1') as file:
    dialogues = file.readlines()

# Simple cleaning function
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    text = text.lower().strip()  # Convert to lowercase and remove leading/trailing spaces
    return text

# Clean dialogues
cleaned_dialogues = [clean_text(dialogue) for dialogue in dialogues]

# Function to process a batch of texts
def batch_extract_entities(dialogues):
    # Process all dialogues in a single batch
    docs = list(nlp.pipe(dialogues, batch_size=50))  # Process 50 dialogues at once (adjust the batch size if necessary)

    # Extract named entities
    all_entities = []
    for doc in docs:
        entities = [ent.text for ent in doc.ents]
        all_entities.append(entities)

    return all_entities

# Apply batch NER to all cleaned dialogues
named_entities_batch = batch_extract_entities(cleaned_dialogues)

# Display the first 5 dialogues with extracted named entities
for i in range(5):
    print(f"Dialogue: {cleaned_dialogues[i]}")
    print(f"Named Entities: {named_entities_batch[i]}")
    print()

import spacy
import re

# Load the SpaCy pre-trained English NER model
nlp = spacy.load("en_core_web_sm")

# Load the dataset (assuming it's a txt file)
with open('/content/dialog.txt', 'r', encoding='ISO-8859-1') as file:
    dialogues = file.readlines()

# Simple cleaning function
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    text = text.lower().strip()  # Convert to lowercase and remove leading/trailing spaces
    return text

# Clean dialogues
cleaned_dialogues = [clean_text(dialogue) for dialogue in dialogues]

# Function to process a batch of texts and extract entities with their types
def batch_extract_entities_with_types(dialogues):
    # Process all dialogues in a single batch
    docs = list(nlp.pipe(dialogues, batch_size=50))  # Process 50 dialogues at once (adjust the batch size if necessary)

    # Extract named entities and their types
    all_entities_with_types = []
    for doc in docs:
        entities_with_types = [(ent.text, ent.label_) for ent in doc.ents]
        all_entities_with_types.append(entities_with_types)

    return all_entities_with_types

# Apply batch NER with types to all cleaned dialogues
entities_with_types_batch = batch_extract_entities_with_types(cleaned_dialogues)

# Display the first 5 dialogues with extracted named entities and their types
for i in range(5):
    print(f"Dialogue: {cleaned_dialogues[i]}")
    print(f"Named Entities with Types: {entities_with_types_batch[i]}")
    print()

import spacy

# Load the SpaCy pre-trained English NER model
nlp = spacy.load("en_core_web_sm")

# Function to extract entities with types from custom text
def extract_entities_from_text(text):
    # Process the input text
    doc = nlp(text)
    # Extract named entities and their types
    entities_with_types = [(ent.text, ent.label_) for ent in doc.ents]
    return entities_with_types

# Example custom text for testing
custom_text = "Barack Obama, the former president of the United States, visited Microsoft headquarters in Redmond."

# Test the custom text
entities_with_types = extract_entities_from_text(custom_text)

# Display the named entities and their types
print(f"Custom Text: {custom_text}")
print(f"Named Entities with Types: {entities_with_types}")

import spacy
import re
from termcolor import colored  # To add color to the terminal output

# Load the SpaCy pre-trained English NER model
nlp = spacy.load("en_core_web_sm")

# Simple cleaning function (without removing capitalization)
def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s,.\-]', '', text)  # Keep punctuation and alphanumeric
    text = text.strip()  # Remove leading/trailing spaces
    return text

# Function to extract named entities with custom labels and color them
def extract_entities_with_custom_labels(text):
    # Clean the input text
    cleaned_text = clean_text(text)

    # Process the text with SpaCy's NER model
    doc = nlp(cleaned_text)

    # Custom mapping of entity labels
    entities = []
    highlighted_text = cleaned_text  # Start with the cleaned text to add color to it

    for ent in doc.ents:
        # Custom labels based on the entity type
        entity_type = ""
        if ent.label_ == "GPE":
            entity_type = "LAND"
        elif ent.label_ == "PERSON":
            entity_type = "PERSON"
        elif ent.label_ == "ORG":
            entity_type = "COMPANY"
        elif ent.label_ == "LOC":
            entity_type = "PLACE"
        elif ent.label_ == "TIME":
            entity_type = "DURATION"
        elif ent.label_ == "DATE":
            entity_type = "DATE"
        elif ent.label_ == "MONEY":
            entity_type = "CURRENCY"
        elif ent.label_ == "PRODUCT":
            entity_type = "ITEM"
        else:
            entity_type = ent.label_

        # Color the extracted entity
        highlighted_entity = colored(ent.text, 'blue')
        highlighted_text = highlighted_text.replace(ent.text, highlighted_entity)

        # Append the entity and its type to the list
        entities.append((ent.text, entity_type))

    return highlighted_text, entities

# Input a custom sentence
custom_sentence = input("Enter a custom sentence: ")

# Extract entities with custom labels and highlight them
highlighted_text, entities_with_custom_labels = extract_entities_with_custom_labels(custom_sentence)

# Display the extracted named entities with their custom labels
print("\nHighlighted Text with Entities:")
print(highlighted_text)

print("\nExtracted Entities with Custom Labels:")
for entity, label in entities_with_custom_labels:
    print(f"Entity: {entity}, Label: {label}")

import spacy
import re
from IPython.display import display, HTML

# Load the SpaCy pre-trained English NER model
nlp = spacy.load("en_core_web_sm")

# Simple cleaning function (without removing capitalization)
def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s,.\-]', '', text)  # Keep punctuation and alphanumeric
    text = text.strip()  # Remove leading/trailing spaces
    return text

# Function to extract named entities with custom labels and color them
def extract_entities_with_custom_labels(text):
    # Clean the input text
    cleaned_text = clean_text(text)

    # Process the text with SpaCy's NER model
    doc = nlp(cleaned_text)

    # Custom mapping of entity labels
    entities = []
    highlighted_text = cleaned_text  # Start with the cleaned text to add color to it

    for ent in doc.ents:
        # Custom labels based on the entity type
        entity_type = ""
        if ent.label_ == "GPE":
            entity_type = "LAND"
        elif ent.label_ == "PERSON":
            entity_type = "PERSON"
        elif ent.label_ == "ORG":
            entity_type = "COMPANY"
        elif ent.label_ == "LOC":
            entity_type = "PLACE"
        elif ent.label_ == "TIME":
            entity_type = "DURATION"
        elif ent.label_ == "DATE":
            entity_type = "DATE"
        elif ent.label_ == "MONEY":
            entity_type = "CURRENCY"
        elif ent.label_ == "PRODUCT":
            entity_type = "ITEM"
        else:
            entity_type = ent.label_

        # Color the extracted entity (HTML formatting for Colab)
        highlighted_entity = f'<span style="color: blue; font-weight: bold;">{ent.text}</span>'
        highlighted_text = highlighted_text.replace(ent.text, highlighted_entity)

        # Append the entity and its type to the list
        entities.append((ent.text, entity_type))

    return highlighted_text, entities

# Input a custom sentence
custom_sentence = input("Enter a custom sentence: ")

# Extract entities with custom labels and highlight them
highlighted_text, entities_with_custom_labels = extract_entities_with_custom_labels(custom_sentence)

# Display the extracted named entities with their custom labels in HTML format
display(HTML(f"<h3>Highlighted Text with Entities:</h3><p>{highlighted_text}</p>"))

# Display the extracted entities with labels
print("\nExtracted Entities with Custom Labels:")
for entity, label in entities_with_custom_labels:
    print(f"Entity: {entity}, Label: {label}")

