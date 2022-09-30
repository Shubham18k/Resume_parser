from fastapi import FastAPI,Request,File,UploadFile
import document
import shutil
from typing import List
from fastapi.templating import Jinja2Templates
from pdfminer.high_level import extract_text
import docx2txt
import os


app=FastAPI()

template= Jinja2Templates(directory="Pages")

@app.get('/')
def hello(request:Request):
    return template.TemplateResponse("home.html",{"request":request})


def file_pdf(file):
    L=[]
    name,ext=file.filename.split('.')
    if ext=='pdf':
        try:
            os.chdir(r'C:\Data')
            f_dest = open(file.filename, 'wb')
            shutil.copyfileobj(file.file,f_dest)
            outfile_name = f"{file.filename}"
            txt=extract_text(outfile_name)
            p=document.main(txt)
            L.append(p)
        except Exception as e:
            print(e)

    elif ext=='docx':
        try:
            os.chdir(r'C:\Data')
            f_dest=open(file.filename,'wb')
            shutil.copyfileobj(file.file,f_dest)
            doc_name=f'{file.filename}'
            txt=docx2txt.process(doc_name)
            d=document.main(txt)
            L.append(d)
        except Exception as e:
                print(e)

    else:
        return 'Invalid format'
    return set(L)




@app.post('/data/')
async def upload(file:UploadFile=File(...)):
    try:
        data=file_pdf(file)
        path=os.getcwd()
        os.chdir(path)
        return data
    except Exception as e:
        print(e)
        return "No data inserted"
    
