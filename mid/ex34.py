from fastapi import FastAPI

app = FastAPI() 

# 문제 2
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 문제 1
@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
    return {"item_id": item_id, "name": name, "age": age}

from fastapi.staticfiles import StaticFiles
# 문제 4
app.mount("/", StaticFiles(directory="static", html=True), name="static")

from fastapi import Form

@app.post("/user")
# 문제 3
async def read_user_form(name: str = Form(...), studentcode: str = Form(...), major: str = Form(...)):
    return {"msg": "f{major} {name}님 ({studentcode}) 반갑습니다."}

# 0. FastAPI를 사용하기 위해서 FastAPI 라이브러리를 설치하는 명령문을 쓰시오
# pip install fastapi 
# pip install "uvicorn"

# 1. http://127.0.0.1:8000/item?item_id=20000&name=홍길동&age=20 로 실행되는 API 코드 부분을 완성하시오 (빈칸 문제)

# 2. http://127.0.0.1:8000 로 실행되는 API코드 부분을 완성하시오 (빈칸 문제)

# 3. user.html내 form에서 이름, 전공, 학번을 입력하고 제출 버튼을 누르면 {"msg": "의정과 홍길동님 (20000)"}

# 출력된다고 했을 때 빈 부분에 들어갈 코드를 완성하시오. (빈칸 문제)

# 4. 정적 html 파일을 서비스 하기위한 코드를 완성하시오. (빈칸 문제)

# 5. user.html을 만들어서 FastAPI로 서비스 하고자 한다. 어떤 폴더에 user.html 파일을 두어야 하는가?
# static 폴더 안에 user.html 파일을 두어야 한다 