# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from timeit import default_timer

# configuration
DATABASE = '/Users/subramanian/Desktop/DDOSproject/EMPLOYEEFINAL.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app= Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schemaEmployees.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def hello_world():
	return 'Welcome to our employee database'

@app.route('/getEmployees/<userid>')
def all(userid):
	if userid == "gooduser" or userid == "baduser" or userid== "baduser1" or userid=="baduser2" or userid=="baduser3" or userid== "baduser4":
		g.db = connect_db()
		cur=g.db.execute('select * from employees')
		employees=[dict(emp_no=row[0],birth_date=row[1],first_name=row[2],last_name=row[3],gender=row[4],hire_date=row[5]) for row in cur.fetchall()]
		g.db.close()
		#return 'Working'
		#return render_template('index.html', employees=employees)
		return str(employees)

	else:
		return "You are not allowed to access"

	

@app.route('/getEmployees/<userid>/<emp_no>')
def byempno(userid,emp_no):
	if userid == "gooduser" or userid == "baduser" or userid== "baduser1" or userid=="baduser2" or userid=="baduser3" or userid=="baduser4":
		g.db = connect_db()
		cur=g.db.execute('select * from employees where emp_no ='+ emp_no)
		employees=[ dict(emp_no=row[0],birth_date=row[1],first_name=row[2],last_name=row[3],gender=row[4],hire_date=row[5]) for row in cur.fetchall()]
		g.db.close()
		return str(employees)
		#return render_template('index.html', employees=employees)


	else:
		return "you are not allowed to access"

@app.route('/getEmployeesWildcard/<userid>/<wildcard>')
def wildcard(userid,wildcard):
	if userid == "gooduser" or userid == "baduser" or userid== "baduser1" or userid=="baduser2" or userid== "baduser3" or userid=="baduser4":
		g.db =connect_db()
		cur=g.db.execute('select * from employees where first_name Like'+"'%" + wildcard + "%'")
		employees=[ dict(emp_no=row[0],birth_date=row[1],first_name=row[2],last_name=row[3],gender=row[4],hire_date=row[5]) for row in cur.fetchall()]
		g.db.close()
		return str(employees)
		#return render_template('index.html', employees=employees)

	else :
		return "you are not aloowed to access"

@app.route('/getEmployeesOrderBy/<userid>/<column>')
def orderby(userid,column):
	if userid == "gooduser" or userid == "baduser" or userid == "baduser1" or userid=="baduser2" or userid=="baduser3" or userid=="baduser4":
		g.db = connect_db()
		cur=g.db.execute("select * from employees ORDER BY "+column)
		employees=[dict(emp_no=row[0],birth_date=row[1],first_name=row[2],last_name=row[3],gender=row[4],hire_date=row[5]) for row in cur.fetchall()]
		g.db.close()
		#return 'Working'
		#return render_template('index.html', employees=employees)
		return str(employees)

	else:
		return "You are not allowed to access"

@app.route('/getEmployeesGroupBy/<userid>/<column1>')
def groupby(userid,column1):
	if userid == "gooduser" or userid == "baduser" or userid == "baduser1" or userid=="baduser2" or userid=="baduser3" or userid=="baduser4":
		g.db = connect_db()
		cur=g.db.execute("select * from employees GROUP BY "+column1)
		employees=[dict(emp_no=row[0],birth_date=row[1],first_name=row[2],last_name=row[3],gender=row[4],hire_date=row[5]) for row in cur.fetchall()]
		g.db.close()
		#return 'Working'
		#return render_template('index.html', employees=employees)
		return str(employees)

	else:
		return "You are not allowed to access"

@app.route('/getEmployeesAge/<userid>/<age>')
def agesort(userid,age):
	if userid == "gooduser" or userid == "baduser" or userid == "baduser1" or userid=="baduser2" or userid== "baduser3" or userid=="baduser4":

		g.db = connect_db()
		cur=g.db.execute("select * from employees where date('now') - birth_date > "+ age)
		employees=[dict(emp_no=row[0],birth_date=row[1],first_name=row[2],last_name=row[3],gender=row[4],hire_date=row[5]) for row in cur.fetchall()]
		g.db.close()
		
		#return 'Working'
		return render_template('index.html', employees=employees)

	else:
		return "You are not allowed to access"

@app.route('/insertEmployees/<userid>/<emp_no>/<birth_date>/<first_name>/<last_name>/<gender>/<hire_date>')
def insert(userid,emp_no,birth_date,first_name,last_name,gender,hire_date):
	if userid == "gooduser" or userid == "baduser" or userid == "baduser1" or userid=="baduser2" or userid=="baduser3" or userid=="baduser4":

		g.db = connect_db()
		cur=g.db.execute("insert into employees values ("+ emp_no + ',' + "'"+birth_date+"'"+','+"'"+first_name+"'"+','+"'"+last_name+"'"+','+"'"+gender+"'"+','+"'"+hire_date+"')" )
		#cur=g.db.execute("insert into employees values (3,'1994-03-12','Slow','Yo','M','2016-03-28')")
		g.db.commit()
		g.db.close()
		
		#return 'Working'
		#return render_template('index.html', employees=employees)
		return "Value inserted"

	else:
		return "You are not allowed to access"


	

if __name__=='__main__':
	app.run(host ='0.0.0.0')
	



        
