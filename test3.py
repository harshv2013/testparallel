from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'test2'

mysql = MySQL(app)


@app.route('/sqlqr', methods =['POST','GET'])
def users():
    # con = mysql.connect()
    # cur = con.cursor()
    #cur = mysql.connection.cursor()
    conn = mysql.connect
    cur = conn.cursor()
    q = 'select * from details;'
    q1 = 'select * from student;'
    q2 = 'select * from marks;'
    q3 = 'delete from details where address_city = "Ahmedabad" ;'
    q4a = 'delete from details where address_city = "Chennai" ;'
    q4b = 'insert into details values("Ahmedabad", "itachi@geeks.com",1172, "Code Jam finalist");'
    q4c = ("INSERT INTO details VALUES('%s','%s', '%d', '%s')" % ("Allahabad", "ald@geeks.com", int(9248), "Code Jam finalist" ))

    q4 = " CREATE TABLE Persons ( PersonID int, LastName varchar(255), FirstName varchar(255)," \
         " Address varchar(255), City varchar(255) );"
    q5 = 'show tables;'
    q6 = 'select * from Persons'

    #cur.execute('''show databases;''')
    # cur.execute(q3)
    cur.execute(q)
    conn.commit()
    rv = cur.fetchall()
    #print('We are getting ',type((rv[0])) )
    payload = []
    content = {}
    for result in rv:
        content = {'address_city': result[0], 'email_ID': result[1], 'school_id': result[2], 'accomplishments': result[3] }
        payload.append(content)
        #content = {}

    return jsonify(payload)

    #return str(rv)



if __name__ == '__main__':
    app.run(debug=True)