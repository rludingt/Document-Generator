from docxtpl import DocxTemplate
from datetime import datetime, timedelta


def generate_document(context_dict, doc_path, generated_file_name):
    doc = DocxTemplate(doc_path)
    doc.render(context_dict)
    doc.save(f"./generated_documents/{generated_file_name}.docx")
    return doc


# Grab the correct template 
doc_path = "./templates/job_offer_letter.docx"

# Use the datetime library to dynamically important dates
today = datetime.now()
next_monday = today + timedelta(days=-today.weekday(), weeks=2)
offer_expiry_date = next_monday + timedelta(days=-1)

# Create the context dictionary to provide values for the template
context = {
    'CompanyName': 'ABQ Consulting LLC',
    'CurrentDate': str(today.date()),
    'EmployeeFirstName': 'Jane',
    'EmployeeLastName': 'Smith',
    'PositionTitle': 'Applications Developer',
    'StartDate': str(next_monday.date()),
    'ManagerName': 'Robert Holmes',
    'YearlyCompensation': '$60,000',
    'StandardHours': '40',
    'BonusAmount': '$5,000',
    'CommisionAmount': '$1,000',
    'StocksNumber': '100',
    'AdditionalTerms': 'N/A',
    'ExpiryDate': str(offer_expiry_date.date()),
    'NameOfSignatory': 'Ellen Ellens',
    'TitleOfSignatory': 'IT Director'
    }

# Generate the document, it will appear in the generated_documents folder
generated_document = generate_document(context_dict=context, doc_path=doc_path, generated_file_name='job_offer_letter')