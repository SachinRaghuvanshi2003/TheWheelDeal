from flask import Flask,request,render_template,redirect
import random
import string
import sqlite3
from datetime import date,datetime
app=Flask(__name__)
name={'username':'xyz'}
carbook={'type':'xyz','location':'xyz','dlocation':'xyz','date':'xyz','cid':101}
driver1={'carnum':'xyz','name':'xyz','num':123,'model':'xyz'}
@app.route('/',methods=['GET','POST'])
def search():
        if(request.method=='GET'): 
              return render_template('home.html')
        else:
            import sqlite3
            conn=sqlite3.connect('wheeldeal.db')
            c=conn.cursor()
            columns=['CARID','CARTYPE']
            cartype=request.form.get('location')
            c.execute(f"""SELECT * FROM cardetails WHERE cartype LIKE '%{cartype}'""")
            results=c.fetchall()
            conn.close()
            return render_template('search_results.html',headings=columns,results=results)
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

        
@app.route('/team',methods=['GET','POST'])
def get():
    if(request.method=='GET'):
        return render_template('team.html')
    else:
        return 'placeholder'
@app.route('/login',methods=['GET','POST'])
def getlogin():
    if(request.method=='GET'):
        return render_template('login.html')
    else:
        import sqlite3
        conn=sqlite3.connect('wheeldeal.db')
        c=conn.cursor()
        username=request.form['Uname']
        password=request.form['Pass']
        name['username']=username
        c.execute('SELECT username FROM userlogin WHERE username=? AND password=?',(username,password))
        results=c.fetchone()
        conn.close()
        if results is not None:
              return redirect("/valid_login", code=302)
        else:
             return redirect('/signup')
             
        
@app.route('/signup',methods=['GET','POST'])
def getSIGNUP():
    if(request.method=='GET'):
        return render_template('signup.html')
    else:
        import sqlite3
        conn=sqlite3.connect('wheeldeal.db')
        c=conn.cursor()
        name1=request.form.get('name')
        username=request.form.get('uname')
        dob=request.form.get('dob')
        address=request.form.get('address')
        phone=request.form.get('phone')
        password=request.form['password']
        phone=int(phone)
        c.execute('INSERT INTO userlogin VALUES(?,?,?,?,?,?)',(name1,username,phone,password,address,dob))
        conn.commit()
        conn.close()
        return redirect('/login')

@app.route('/valid_login',methods=['GET','POST'])
def searchcar():
        if(request.method=='GET'): 
              return render_template('valid_login.html')
        else:
            import sqlite3
            conn=sqlite3.connect('wheeldeal.db')
            c=conn.cursor()
            d=conn.cursor()
            e=conn.cursor()
            columns=['CAR TYPE','AVAILABLE']
            cartype=request.form['cartype']
            location=request.form['location']
            droplocation=request.form['dlocation']
            date1=request.form['date']
            date_object = datetime.strptime(date1, '%Y-%m-%d').date()
            if(date_object<date.today()):
                 conn.close()
                 return render_template('internal_server_error.html')
            else:
                    carbook['type']=cartype
                    carbook['location']=location
                    carbook['dlocation']=droplocation
                    carbook['date']=date1
                    c.execute(f"""SELECT carid FROM cardetails WHERE cartype LIKE '%{cartype}'""")
                    results=c.fetchall()
                    for x in results:
                            result=x[0]
                    carbook['cid']=result
                    d.execute(f"""SELECT COUNT(*) FROM driverdetails WHERE carid={result} AND available='YES' AND city like'%{location}'""")
                    results1=d.fetchall()
            
                    for y in results1:
                     results1=y[0]
                    conn.close()
                    return render_template('search_results.html',headings=columns,results=[cartype,results1])

@app.route('/Profile',methods=['GET'])
def searchProfile():
        if(request.method=='GET'): 
            import sqlite3
            conn=sqlite3.connect('wheeldeal.db')
            c=conn.cursor()
            d=conn.cursor()
            columns=['User Name','User Id','Phone Number','Address','Date of Birth']
            
            c.execute('SELECT name,username,phonenum,address,dob FROM userlogin WHERE username=?',(name['username'],))
            results=c.fetchone()
            final_result = list(results)
            conn.close()
            return render_template('Profile.html',results=final_result,headings=columns)
                 
@app.route('/contact',methods=['GET','POST'])
def contactus():
        if(request.method=='GET'): 
            return render_template('contact.html')
        else:
            import sqlite3
            conn=sqlite3.connect('wheeldeal.db')
            c=conn.cursor()
            fname=request.form.get('fname')
            lname=request.form.get('lname')
            email=request.form.get('email')
            phone=request.form.get('phone')
            phone=int(phone)
            c.execute('INSERT INTO contactus VALUES (?,?,?,?)',(fname,lname,email,phone))
            conn.commit()
            conn.close()
            return render_template('thankyou.html')
@app.route('/book',methods=['GET','POST'])   
def booknow():
     if (request.method=='GET'):
          import sqlite3
          conn=sqlite3.connect('wheeldeal.db')
          e=conn.cursor()
          d=conn.cursor()
          c=conn.cursor()
          avail='YES'
          notavail="NO"
          cid=int(carbook['cid'])
          loc=carbook['location']
          e.execute(f"""SELECT name,phnum,carmodel,carnum FROM driverdetails WHERE carid={cid} AND available='YES' AND city LIKE '%{loc}'""")
          resultdriver=e.fetchone()
          driver=list(resultdriver)
          driver1['name']=driver[0]
          driver1['num']=int(driver[1])
          driver1['model']=driver[2]
          driver1['carnum']=driver[3]
          drivernum=int(driver1['num'])
          bid=random.randint(1345698389398,17273984787349)
          d.execute('INSERT INTO booking VALUES(?,?,?,?,?,?,?,?,?,?)',(bid,name['username'],carbook['date'],carbook['location'],carbook['dlocation'],carbook['type'],driver1['carnum'],driver1['name'],drivernum,driver1['model']))
          c.execute(f"""UPDATE driverdetails SET available='NO' WHERE carnum LIKE '%{driver[3]}'""")
          conn.commit()
          conn.close()
          return render_template('book.html',location=carbook['location'],droplocation=carbook['dlocation'],cartype=carbook['type'],driverdetails=driver)  
@app.route('/bookings',methods=['GET'])
def bookings():
     if(request.method=='GET'):
          import sqlite3
          conn=sqlite3.connect('wheeldeal.db')
          c=conn.cursor()
          c.execute(f"""SELECT * FROM booking WHERE username LIKE '%{name['username']}'""")
          columns1=['Booking Id','User Name','Date','Pick Up Location','Drop off Location','Car Type','Car Number','Driver Name','Driver Number','Car Model']
          results=c.fetchall()
          return render_template('bookings.html',headings=columns1,results=results)    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404 
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('internal_server_error.html'), 500
