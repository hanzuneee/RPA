from fastapi import FastAPI, Form, File, UploadFile
from pathlib import Path
import shutil

from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO

app = FastAPI()

def loginDB(userId, userPassword):
    import sqlite3
    
    conn = sqlite3.connect('education.db')
    cursor = conn.cursor()
        
    query = 'SELECT * FROM user WHERE userId = ? AND userPassword = ?'
    cursor.execute(query, (userId, userPassword))
    result = cursor.fetchone()
    conn.close()
        
    if result:
        print("Login successful!")
        print("User Info:", result) 
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False

@app.post("/login")
def login_form(userid: str = Form(...), userpassword: str = Form(...)):
    result = loginDB (userid, userpassword)
        
    if result == True :
        return {"msg": f"{userid}님 반갑습니다."}
    else :
        return {"msg": f"로그인에 실패했습니다."}
    
def makeXL(filename) :
    from faker import Faker 
    from openpyxl import Workbook

    fake = Faker('ko_KR')

    wb = Workbook()
    ws = wb.active

    ws.append(['이름', '성별', "이메일", "전화번호", "주소"])

    for i in range(1000):
        name = fake.name()
        gender = fake.random_element(elements=('남', '여'))
        email = fake.email()
        phone_number = fake.phone_number()
        address = fake.address()
        ws.append([name, gender, email, phone_number, address])
        
        print(filename)
        wb.save('filename')
    
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")
