from fastapi import FastAPI,Request,File,UploadFile
import pdf
import document
import shutil
from pathlib import Path
from typing import List
from tempfile import NamedTemporaryFile


app=FastAPI()

@app.get('/')
def hello():
    return "Hello world"

L=[]
@app.post('/data')
async def upload(file:List[UploadFile]=File(...)):
    for i in file:
        name,ext=i.filename.split('.')
        if ext=='pdf':
            try:
                suffix = Path(i.filename).suffix
                with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                    shutil.copyfileobj(i.file, tmp)
                tmp_path = Path(tmp.name)
                p=pdf.main(tmp_path)
                L.append(p)
            except Exception as e:
                return e
        elif ext=='docx':
            try:
                suffix = Path(i.filename).suffix
                with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                    shutil.copyfileobj(i.file, tmp)
                tmp_path = Path(tmp.name)
                d=document.main(tmp_path)
                L.append(d)
            except Exception as e:
                return e
        else:
            print(ext)
            print('Improper format')

    return set(L)
