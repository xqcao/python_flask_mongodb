import os
from flask import Flask,render_template,request,redirect
from pymongo import MongoClient



app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017
)
# client = MongoClient()

db = client.mydata


@app.route("/")
def mainpage():
    _items = db.person.find()
    items = [item for item in _items]
    return render_template('mainpage.html',msg="hhhhgggg",items=items)

@app.route('/setup', methods=["POST"])
def dosetup():
    _name = request.form['inName']
    _email = request.form['inEmail']
    _address = request.form['inAddress']
    print(_name,_email,_address)
    print(request)
    item_doc={
    "name":_name,
    "email":_email,
    "address":_address
    }
    db.person.insert_one(item_doc)
    return render_template('sucess.html')

@app.route('/abc', methods=["POST"])
def doabc():
    print("address :",request.form['inAddress'])
    return redirect('/cctv')

@app.route('/cctv')
def docctv():
    return render_template('cctvpage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
