from fastapi import FastAPI,Request,File,UploadFile
import uvicorn
import document
import shutil
from typing import List
from fastapi.templating import Jinja2Templates
from pdfminer.high_level import extract_text
import docx2txt
import os
import json


app=FastAPI()

template= Jinja2Templates(directory="Pages")
'''
@app.get('/')
def hello(request:Request):
    return template.TemplateResponse("home.html",{"request":request})
'''

def file_pdf(files,c):
    L=[]
    for file in files:
        name,ext=file.filename.split('.')
        #c=os.getcwd()
        if ext=='pdf':
            try:
                os.chdir(os.path.join(c,'Data'))
                f_dest = open(file.filename, 'wb')
                shutil.copyfileobj(file.file,f_dest)
                outfile_name = f"{file.filename}"
                txt=extract_text(outfile_name)
                p=document.main(txt)
                L.append(p)
                os.chdir('../')
            except Exception as e:
                print(e)

        elif ext=='docx':
            try:
                os.chdir(os.path.join(c,'Data'))
                f_dest=open(file.filename,'wb')
                shutil.copyfileobj(file.file,f_dest)
                doc_name=f'{file.filename}'
                txt=docx2txt.process(doc_name)
                d=document.main(txt)
                L.append(d)
                os.chdir('../')
            except Exception as e:
                    print(e)

        else:
            print('Invalid format')
    
    return set(L)




@app.post('/')
async def upload(file:List[UploadFile]=File(...)):
    try:
        path=os.getcwd()
        data=file_pdf(file,path)
        os.chdir(path)
        return data
    except Exception as e:
        print(e)
        return "No data inserted"
    
