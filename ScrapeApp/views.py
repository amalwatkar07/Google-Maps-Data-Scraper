from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
import os
import pymysql
from serpapi import GoogleSearch

def getDB(query):
    flag = False
    qry = query.strip().lower()
    output='<table border=1 align=center width=100%><tr><th><font size="3" color="black">Business Name</th><th><font size="3" color="black">Reviews</th>'
    output += '<th><font size="3" color="black">Ratings</th><th><font size="3" color="black">Address</th><th><font size="3" color="black">Description</th>'
    output += '<th><font size="3" color="black">Business Website</th></tr>'
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'scrape',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select * FROM search where query='"+qry+"'")
        rows = cur.fetchall()
        for row in rows:
            flag = True
            output += '<td><font size="3" color="black">'+row[1]+'</td><td><font size="3" color="black">'+str(row[2])+'</td><td><font size="3" color="black">'+str(row[3])+'</td>'
            output += '<td><font size="3" color="black">'+str(row[4])+'</td><td><font size="3" color="black">'+str(row[5])+'</td>'
            output += '<td><a href="https://www.google.com/search?q='+row[1]+'" target="_blank"><font size="3" color="blue">Visit Website</td></tr>'
    if flag:
        output+= "</table></br></br></br></br>"
    return output, flag

def saveDB(query, name, reviews, ratings, address, desc, url):
    name = name.replace("'","")
    address = address.replace("'","")
    desc = desc.replace("'","")
    qry = query.strip().lower()
    db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'scrape',charset='utf8')
    db_cursor = db_connection.cursor()
    student_sql_query = "INSERT INTO search VALUES('"+qry+"','"+name+"','"+reviews+"','"+ratings+"','"+address+"','"+desc+"','"+url+"')"
    db_cursor.execute(student_sql_query)
    db_connection.commit()

def ScrapeMapAction(request):
    if request.method == 'POST':
        query = request.POST.get('t1', False)
        output, flag = getDB(query)
        if flag:
            print("db")
        if flag == False:
            print("maps")
            params = {"api_key": "343dc2f4d4d9d8fba073f0cb762579018da863d81d23b6cb1a4e2604944458d3", "engine": "google","q": query,"gl": "in","hl": "en"}
            search = GoogleSearch(params)
            results = search.get_dict()
            data = results['local_results']['places']
            for i in range(len(data)):
                value = data[i]
                if 'title' in value:
                    name = value['title']
                else:
                    name = "NA"
                if 'reviews' in value:    
                    reviews = str(value['reviews'])
                else:
                    reviews = "NA"    
                if 'rating' in value:
                    ratings = str(value['rating'])
                else:
                    ratings = "NA"    
                if 'address' in value:
                    address = value['address']
                else:
                    address = "NA"    
                if 'description' in value:
                    desc = value['description']
                else:
                    desc = "NA"    
                if 'place_id_search' in value:
                    url = value['place_id_search']
                else:
                    url = "NA"    
                output += '<td><font size="3" color="black">'+name+'</td><td><font size="3" color="black">'+str(reviews)+'</td><td><font size="3" color="black">'+str(ratings)+'</td>'
                output += '<td><font size="3" color="black">'+str(address)+'</td><td><font size="3" color="black">'+str(desc)+'</td>'
                if url == "NA":
                    output += '<td><font size="3" color="black">'+str(url)+'</td></tr>'
                else:
                    output += '<td><a href="https://www.google.com/search?q='+name+'" target="_blank"><font size="3" color="blue">Visit Website</td></tr>'
                saveDB(query, name, str(reviews), str(ratings), address, desc, url)
        output+= "</table></br></br></br></br>"
        context= {'data':output}
        return render(request, 'UserScreen.html', context)

def ScrapeMap(request):
    if request.method == 'GET':
       return render(request, 'ScrapeMap.html', {})

def RegisterAction(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        contact = request.POST.get('t3', False)
        email = request.POST.get('t4', False)
        address = request.POST.get('t5', False)
        
        output = "none"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'scrape',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username:
                    output = username+" Username already exists"
                    break                
        if output == "none":
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'scrape',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO register(username,password,contact,email,address) VALUES('"+username+"','"+password+"','"+contact+"','"+email+"','"+address+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                output = "Signup process completed. Login to perform Google Maps scraping"
        context= {'data':output}
        return render(request, 'Register.html', context)    

def UserLoginAction(request):
    global username
    if request.method == 'POST':
        global username, email_id
        status = "none"
        users = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'scrape',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username,password,email FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == users and row[1] == password:
                    email_id = row[2]
                    username = users
                    status = "success"
                    break
        if status == 'success':
            context= {'data':'Welcome '+username}
            return render(request, "UserScreen.html", context)
        else:
            context= {'data':'Invalid username'}
            return render(request, 'UserLogin.html', context)

def UserLogin(request):
    if request.method == 'GET':
       return render(request, 'UserLogin.html', {})

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def Register(request):
    if request.method == 'GET':
       return render(request, 'Register.html', {})
