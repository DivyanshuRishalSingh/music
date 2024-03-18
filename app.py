import pymongo
from flask import Flask,render_template,request
client=pymongo.MongoClient('mongodb+srv://pwskills:pwskills@cluster0.ormss9s.mongodb.net/?retryWrites=true&w=majority')
mydb=client['collection']
coll=mydb['record']
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def fun1():  
    return render_template('login.html')
       
@app.route('/reg.html',methods=['GET','POST'])
def fun6():
    return render_template('reg.html')

@app.route('/page1',methods=['POST'])
def fun2():
    text=request.form['text']
    email=request.form['email']
    return render_template('index.html',text=text,email=email)
    
@app.route('/page2',methods=['POST'])
def fun3():
    if request.method=='POST':   
        name=request.form['name']
        number=request.form['number']      
        email=request.form['email']
        date=request.form['date']
        gendar=request.form['gendar'] 
        address=request.form['address']
        identity=request.form['identity']
        card=request.form['card']
        data={"NAME":name,"PHONE":number,"EMAIL":email,"DATE OF BIRTH":date,"GENDAR":gendar,"ADDRESS":address,identity:card}
        coll.insert_one(data)
        return render_template('results.html',name=name,mail=email)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=False,port=4200)

