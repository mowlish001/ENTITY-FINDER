EntityFinder is a Python-based tool that extracts and categorizes named entities from text. This project uses SpaCy, a popular Natural Language Processing (NLP) library, to recognize and classify entities like people, organizations, locations, dates, and more.

****Tools and Technologies Used*****
Python 3.x: The primary programming language used to develop the project.
SpaCy: A pre-trained NLP model (en_core_web_sm) used for Named Entity Recognition (NER) to extract named entities.
termcolor: A Python library used to colorize the output for better visibility in the terminal (Note: works well in a local environment or Jupyter/IDE, but not in Google Colab).
Regular Expressions (re): Used for simple text preprocessing to clean and remove unwanted characters from input text.
About the Model
The project leverages SpaCy's pre-trained NER model (en_core_web_sm) which is capable of recognizing various entities, such as:

*PERSON: Names of people.
*GPE (Geopolitical Entity): Countries, cities, states, etc.
*ORG: Organizations (companies, schools, etc.).
*DATE: Dates and time expressions.
*TIME: Time expressions.
*MONEY: Monetary values.
*PRODUCT: Products, items, etc.
*LOC: Other locations like landmarks, rivers, etc.
In this project, a custom labeling system is applied to these categories, where:

*GPE is categorized as LAND.
*PERSON is left unchanged as PERSON.
*ORG is categorized as COMPANY.
*LOC is categorized as PLACE.
*DATE, TIME, MONEY, and PRODUCT are given more human-readable labels.
The model can be used to detect and label entities from sentences, paragraphs, or larger text bodies.

****Dataset*****
This project doesn’t require any specific dataset for training, as it uses a pre-trained model from SpaCy. However, users can input custom sentences,We used the dataset The Cornell Movie-Dialogs Corpus which a is collection of fictional movie conversations that researchers at Cornell University created and the system will extract named entities from that text.

*****Problem and Problem Definition*****
Problem: Many applications need to extract useful information from textual data in the form of entities. These entities can include people's names, locations, organizations, dates, and more. For example, extracting organizations from a news article or detecting locations in a conversation can help build more intelligent systems that understand text better.

Goal: The goal of EntityFinder is to provide a simple tool to identify and categorize named entities from input text. The project aims to:

Automatically identify and label named entities from text.
Highlight entities in a color-coded manner for easy interpretation.
Provide labeled entities with their respective types.
What We Did
Text Preprocessing:

*****Cleaned the input text by removing non-alphanumeric characters while keeping punctuation and numbers.***********
Named Entity Recognition (NER):

Used SpaCy’s pre-trained NER model to detect named entities in the cleaned text.
Implemented a custom labeling system for the detected entities.
Color-Coding Entities:

Integrated the termcolor library (for local environments) to colorize the output and make the detected entities more visible in the terminal.
Output:

The final output includes a color-coded version of the text with named entities highlighted, as well as a list of detected entities with their custom labels.
Customization:

The system is flexible, allowing users to input their own sentences and receive the detected entities along with their types.
