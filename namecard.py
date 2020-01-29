from flask import Flask, escape, request
app = Flask(__name__) #플라스크를 실행하면, 앱이 만들어진다.
import pickle
import numpy as np
from matplotlib import pyplot as plt
import random
#%matplotlib inline

#set FLASK_APP=<파일명>.py
#flask run
#db가 바뀔때마다 바로바로 쓰면, 안전하지만, 성능은 떨어진다.
#주기적으로 저장,

#db = pickle.load('./db.bin')
db = {}
#db = {
#    "0":{
#        "name" : "bill",
#        "phone":"010-2959-9945"
#    }
#}
id = 0

@app.route('/users', methods = ['POST'])
def create_user():
    global id
    body = request.json

    print(body)
    body ['id'] = id
    #body = ....
    #todo body에 id를 넣어준다.


    db[str(id)]=body
    id = id + 1
    print
   # pickle.dump('./db.bin')
    return body


@app.route('/users/<id>', methods = ['GET'])
def select_user(id):
    if id not in db:
        return {}, 404
    print(db)
    return db[id]

@app.route('/users/<id>', methods = ['DELETE'])
def delete_user(id):
   # pickle.dump('./db.bin')
    del db[str(id)]
    return db

@app.route('/users/<id>', methods = ['PUT'])
def update_user(id):
    body = request.get_json()
    if id in db.keys():
        db[str(id)].update(body)
    else:
        db[str(id)]=body
    return db

@app.route('/')#uri부분
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi', methods = ['GET', 'POST'])
def hi():
    return {
        "version":"2.0",
        "template":{
            "outputs":[
                {
                    "simpleText":{
                        "text":"반가워~(발그레)."
                    }
                }
            ]
        }
    }
@app.route('/nc', methods = ['POST'])
def namecard():
    body = request.json
    pprint = pprint(body)
    url =
    return {
        "version":"2.0",
        "template":{
            "outputs":[
                {
                    "simpleText":{
                        "text":"인식완료"
                    }
                }
            ]
        }
    }
#500에러는 서버에러
#400에러는 본인이 잘못한것

def ocr(file):
    #todo 명함정보 추출
    return ''