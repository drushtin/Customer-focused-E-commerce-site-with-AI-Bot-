from flask import Flask, render_template,request,make_response
import plotly
import plotly.graph_objs as go
import mysql.connector
from mysql.connector import Error
import sys

import pandas as pd
import numpy as np
import json  #json request
from werkzeug.utils import secure_filename
import os
import csv #reading csv
import geocoder
from random import randint
import math
from chatterbot import responder
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import date


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/index')
def indexnew():    
    return render_template('index.html')

@app.route('/register')
def register():    
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/doctorreg')
def doctorreg():
    return render_template('docreg.html')

@app.route('/doctor')
def doctor():
    return render_template('doclogin.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')
    
@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgotpassword.html')

@app.route('/admin')
def admin():
    return render_template('adminlogin.html')

@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

""" REGISTER CODE  """
rcount = 0
@app.route('/regdata', methods =  ['GET','POST'])
def regdata():
    connection = mysql.connector.connect(host='localhost',database='flaskchatbotdb',user='root',password='')
    cursor = connection.cursor()
    email = request.args['email']
    sq_query="select count(*) from userdata where Email='"+email+"'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = int(data[0][0])
    if(rcount==0):
        fname = request.args['fname']
        lname = request.args['lname']
        email = request.args['email']
        pswd = request.args['pswd']
        phone = request.args['phone']
        addr = request.args['addr']
        pcode = request.args['pcode']
        value = randint(123, 99999)
        uid="User"+str(value)
        print(addr)
            
        #cursor = connection.cursor()
        sql_Query = "insert into userdata(Userid,Fname,Lname,Email,Pswd,Phone,Addr,Pcode) values('"+uid+"','"+fname+"','"+lname+"','"+email+"','"+pswd+"','"+phone+"','"+addr+"','"+pcode+"')"
            
        cursor.execute(sql_Query)
        connection.commit() 
        connection.close()
        cursor.close()
        msg="Data stored successfully"
        #msg = json.dumps(msg)
        resp = make_response(json.dumps(msg))
        
        print(msg, flush=True)
        #return render_template('register.html',data=msg)
        #return render_template('login.html')
        return resp
    else:
        msg="User Already Exists"
        resp = make_response(json.dumps(msg))
        
        print(msg, flush=True)
        #return render_template('register.html',data=msg)
        return resp
       
@app.route('/fpassword1')
def fpassword1():
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaa')
    import smtplib 
      
    connection=mysql.connector.connect(host='localhost',database='flaskchatbotdb',user='root',password='')
    lgemail=request.args['email']
    print(lgemail, flush=True)
    cursor = connection.cursor()
    sq_query="select Pswd from userdata where Email='"+lgemail+"'"
    print(sq_query)
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    pswd = data[0][0]
    print(pswd)
    connection.commit() 
    connection.close()
    cursor.close()
    print('cccccccccc')
    # message to be sent 
    strval = "Your password is :"+str(pswd)
    
    import smtplib
    recipient=lgemail
    FROM = "collegechatbot98@gmail.com"
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = "Password email"
    TEXT = strval

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("collegechatbot98@gmail.com", "idhrfuuuzaualrqd")
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")
    '''
    print('cccccccccc')
    # message to be sent 
    strval = "Your password is :"+str(pswd)
    print(strval)
    # sending the mail 
    s.sendmail("collegechatbot98@gmail.com", lgemail, strval) 
    
    # terminating the session 
    s.quit()
    '''



    msg='Mail Sent Successfully'
    resp = make_response(json.dumps(msg))
    
    print(msg, flush=True)
    return resp


@app.route('/regddata', methods =  ['GET','POST'])
def regddata():
    connection = mysql.connector.connect(host='localhost',database='flaskchatbotdb',user='root',password='')
    print(request.args['darea'])
    darea = request.args['darea']
    name = request.args['name']
    pswd = request.args['pswd']
    email = request.args['email']
    phone = request.args['phone']
    dtype = request.args['dtype']
    value = randint(123, 99999)
    uid="Doc"+str(value)

        
    today = str(date.today())
    print(today)
    year=today.split("-")    
    year=int(year[0])  

    if year<=2021:   
        cursor = connection.cursor()
        sql_Query = "insert into doctordata values('"+uid+"','"+name+"','"+pswd+"','"+email+"','"+phone+"','"+dtype+"','"+darea+"')"
            
        cursor.execute(sql_Query)
        print(sql_Query)
        connection.commit() 
        connection.close()
        cursor.close()
        msg="Data stored successfully"
        #msg = json.dumps(msg)
        resp = make_response(json.dumps(msg))
        print(resp)
        print(msg, flush=True)
        #return render_template('register.html',data=msg)
        return resp
    else:
        msg="Exception in code"
        resp = make_response(json.dumps(msg))
        return resp



"""LOGIN CODE """

@app.route('/logdata', methods =  ['GET','POST'])
def logdata():
    connection=mysql.connector.connect(host='localhost',database='flaskchatbotdb',user='root',password='')
    phone=request.args['phone']
    lgpssword=request.args['pswd']
    print(phone, flush=True)
    print(lgpssword, flush=True)
    '''global email_id
    email_id=lgemail'''
    cursor = connection.cursor()
    sq_query="select count(*) from userdata where Phone='"+phone+"' and Pswd='"+lgpssword+"'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = int(data[0][0])
    print(rcount, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    
    if rcount>0:
        msg="Success"
        resp = make_response(json.dumps(msg))
        return resp
    else:
        msg="Failure"
        resp = make_response(json.dumps(msg))
        return resp



@app.route('/logddata', methods =  ['GET','POST'])
def logddata():
    connection = mysql.connector.connect(host='localhost',database='flaskchatbotdb',user='root',password='')
    lgemail=request.args['email']
    lgpssword=request.args['pswd']
    print(lgemail, flush=True)
    print(lgpssword, flush=True)
    cursor = connection.cursor()

    
    global docid
    docid =lgemail
    sq_query="select count(*) from doctordata where name='"+lgemail+"' and pswd='"+lgpssword+"'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = int(data[0][0])
    print(rcount, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    
    if rcount>0:
        msg="Success"
        print(msg)
        resp = make_response(json.dumps(msg))
        return resp
    else:
        msg="Failure"
        resp = make_response(json.dumps(msg))
        return resp
        


@app.route('/dochome')
def dochome():
    try:        
        g = geocoder.ip('me')
        print(g.latlng[0])
        print(g.latlng[1])
    except:
        print("Done")
    try:        
        connection = mysql.connector.connect(host='localhost',database='flaskchatbotdb',user='root',password='')
        cursor = connection.cursor()
        sq_query="select count(*) from doctordata"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        patcount = int(data[0][0])
        print(patcount, flush=True)

        sq_query="select count(*) from appointments"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        appcount = int(data[0][0])
        print(appcount, flush=True)

        '''sq_query="select count(*) from edoc20_doctordata"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        doccount = int(data[0][0])
        print(doccount, flush=True)

        today = str(date.today())
        print(today)

        sq_query="select count(*) from edoc20_appointments where dated='"+today+"'"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        tacount = int(data[0][0])
        print(tacount, flush=True)'''

        
        sq_query="select dated,Count(*)as aa from edoc20_appointments group by dated"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        print(data)
        gdata=[]
        for i in range(len(data)):
            datasetval=[]
            datasetval.append(data[i][0])
            datasetval.append(round(data[i][1],2))
            gdata.append(datasetval)
        print(gdata)
            
        #gdata = data
        #print(gdata, flush=True)
        
        connection.commit() 
        connection.close()
        cursor.close()
        return render_template('dochome.html',patcount=patcount,appcount=appcount,doccount=doccount,tacount=tacount,gdata=gdata)
    except:
        print("No Data to be Displayed")
        return render_template('dochome.html')


@app.route('/myapp')
def myapp():            
    connection = mysql.connector.connect(host='localhost',database='flaskchatbotdb',user='root',password='')
    cursor = connection.cursor()
    global docid
    sq_query="select * from appointments where Doc='"+docid+"'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    gdata=[]
    for i in range(len(data)):
        datasetval=[]
        datasetval.append(data[i][1])
        datasetval.append(data[i][2])
        datasetval.append(data[i][3])
        datasetval.append(data[i][4])
        gdata.append(datasetval)
    print(gdata)
        
    #gdata = data
    print(gdata, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    return render_template('myapp.html',gdata=gdata)

@app.route('/alldoctors')
def alldoctors():            
    connection = mysql.connector.connect(host='localhost',database='flaskchatbotdb',user='root',password='')
    cursor = connection.cursor()
    
    global userid
    sq_query="select * from doctordata"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    gdata=[]
    for i in range(len(data)):
        datasetval=[]
        datasetval.append(data[i][0])
        datasetval.append(data[i][1])
        datasetval.append(data[i][2])
        datasetval.append(data[i][3])
        datasetval.append(data[i][4])
        datasetval.append(data[i][5])
        datasetval.append(data[i][6])
        gdata.append(datasetval)
    print(gdata)
        
    #gdata = data
    print(gdata, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    return render_template('alldoctors.html',gdata=gdata)



@app.route('/allpatients')
def allpatients():            
    connection = mysql.connector.connect(host='localhost',database='flaskchatbotdb',user='root',password='')
    cursor = connection.cursor()
    
    global userid
    sq_query="select * from userdata"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    gdata=[]
    for i in range(len(data)):
        datasetval=[]
        datasetval.append(data[i][0])
        datasetval.append(data[i][1])
        datasetval.append(data[i][2])
        datasetval.append(data[i][3])
        datasetval.append(data[i][4])
        datasetval.append(data[i][5])
        datasetval.append(data[i][6])
        gdata.append(datasetval)
    print(gdata)
        
    #gdata = data
    print(gdata, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    return render_template('allpatients.html',gdata=gdata)


filenumber=int(os.listdir('saved_conversations')[-1])
filenumber=filenumber+1
file= open('saved_conversations/'+str(filenumber),"w+")
file.write('bot : Hi There! I am a chatbot. You can begin conversation by typing in a message and pressing enter.\n')
file.close()

english_bot = ChatBot('Bot',
             storage_adapter='chatterbot.storage.SQLStorageAdapter',
             logic_adapters=[
   {
       'import_path': 'chatterbot.logic.BestMatch'
   },
   
],
trainer='chatterbot.trainers.ListTrainer')
english_bot.set_trainer(ListTrainer)

@app.route('/chatbox')
def indexnew1():     
    return render_template('chatbox.html')

@app.route("/get")
def get_bot_response():
    val=1
    if val==0:
        response ="Not able to process"
        return response
    else:        
        userText = request.args.get('msg')
        response = str(english_bot.get_response(userText))
        appendfile=os.listdir('saved_conversations')[-1]
        appendfile= open('saved_conversations/'+str(filenumber),"a")
        print("demo")
        model="collegedunia.pkl"
        response=responder.response(userText,model)
        appendfile.write('user : '+userText+'\n')
        appendfile.write('bot : '+response+'\n')
        return response


if __name__ == '__main__':
    UPLOAD_FOLDER = 'D:/Upload'
    app.secret_key = "secret key"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
