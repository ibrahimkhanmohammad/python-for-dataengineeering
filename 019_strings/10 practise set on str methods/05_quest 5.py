#    Take a filename as input (like report.pdf). Check if it ends with .pdf, .docx, or . txt and print the file type

def file_type(file:str):
    if file.endswith('.pdf'):
        print(f'{file} is in a PDF format')
    elif file.endswith('.docx'):
        print(f'{file} is in a DOCX format')
    elif file.endswith('.txt'):
        print(f'{file} is in a TXT format')
    else:
        print(f'{file} is invalid to upload')

file = 'report.pdf'
file_type(file)