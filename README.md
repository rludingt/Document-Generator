# TLDR
Do you have Word Document templates? Are you mindlessly filling out the same template over and over? Use this. 

# What's inside
Clone this repo to test a basic document generation script! generator.py contains basic code using docxtpl to fill out a Word document (.docx). 

# How do I use it?
Step 1) Run generator.py
Step 2) View your newly generated document in the folder generated_documents
Step 3) Add your own document templates

This script is perfect to nest inside of a Flask or Django application to generate word documents that have defined formats. To dynamically 
generate the content of the document, you might opt to query a dataset and put it's values in the context_dictionary or perhaps
provide a .csv file that has the values you want to populate the in the .docx template
