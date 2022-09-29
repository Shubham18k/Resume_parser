from fastapi import FastAPI,Request,File,UploadFile
import pdf
import document
import shutil
from typing import List
from tempfile import NamedTemporaryFile
from fastapi.templating import Jinja2Templates
from pdfminer.high_level import extract_text
import docx2txt

from search import name

app=FastAPI()

template= Jinja2Templates(directory="Pages")

@app.get('/')
def hello(request:Request):
    return template.TemplateResponse("home.html",{"request":request})


L=[]
@app.post('/data/')
def upload(file:List[UploadFile]=File(...)):
    for i in file:
        name,ext=i.filename.split('.')
        if ext=='pdf':
            try:
                f_dest = open(i.filename, 'wb')
                shutil.copyfileobj(i.file, f_dest)
                outfile_name = f"{i.filename}"
                txt=extract_text(outfile_name)
                p=pdf.main(txt)
                L.append(p)
            except Exception as e:
                print(e)

        elif ext=='docx':
            try:
                f_dest=open(i.filename,'wb')
                shutil.copyfileobj(i.file,f_dest)
                doc_name=f'{i.filename}'
                txt=docx2txt.process(doc_name)
                d=document.main(txt)
                L.append(d)
            except Exception as e:
                print(e)

        else:
            return 'Invalid format'


    return set(L)
