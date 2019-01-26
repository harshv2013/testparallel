
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask import Flask, jsonify, request,  session
from flask_mysqldb import MySQL
import bcrypt
from werkzeug.security import check_password_hash, generate_password_hash

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


@app.route('/createtable', methods =['POST', 'GET'])
def createtable():
        conn = mysql.connect
        cur = conn.cursor()
        q = 'select * from userDetail;'
        q1 = 'create table userDetail( id INT NOT NULL AUTO_INCREMENT, name varchar(255) ,email varchar(255), password varchar(255), PRIMARY KEY (id) ) '
        # q2 = 'describe userDetail'



        cur.execute(q1)
        conn.commit()
        rv = cur.fetchall()

        return str(rv)



# @app.route('/usersignup', methods =['POST','GET'])
# def usersignup():
#     a = request.form.get('name')
#     b = request.form.get('email')
#     c = request.form.get('password')
#
#     print(a,b,c)
#
#     password = c.encode()
#     hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")
#
#     print('hashed password is :',hashed)
#
#     conn = mysql.connect
#     cur = conn.cursor()
#     q = 'select * from userDetail;'
#     # q1 = 'create table userDetail(name varchar(50) ,email varchar(50), password varchar(20)) '
#     q2 = 'describe userDetail'
#     qd = 'DROP TABLE userDetail;'
#
#     q4c = ("INSERT INTO userDetail VALUES('%s','%s', '%s')" % (a, b, hashed))
#
#
#     cur.execute(q4c)
#     conn.commit()
#
#     print('hasssssssssssssssssssss',cur)
#
#     #cur.execute(q)
#
#     rv = cur.fetchall()
#     print('Haaaaeeeeooolllllllooooooooo')
#     payload = []
#     content = {}
#     for result in rv:
#         content = {'name': result[0], 'email': result[1], 'password': result[2]}
#         payload.append(content)
#         #content = {}
#     # print('cooollllllll',payload)
#
#     return jsonify(payload)
#
#     # return jsonify({ 'name': a,'email': b, 'password': c})
#     # return str(rv)

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pas = request.form['password']

        message = None

        conn = mysql.connect
        cur = conn.cursor()
        q = ("select id from userDetail where email = '%s' ") % email

        cur.execute(q)
        rv = cur.fetchall()
        print('GGGGGGoooooonnnnn',rv)
        if rv:
            message = 'Already registered'
            print('Already registered')
        else :
            password = pas.encode()
            hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")
            q1 = ("INSERT INTO userDetail(name, email, password)  VALUES('%s','%s', '%s')" % (name, email, hashed))

            cur.execute(q1)
            conn.commit()
            message = 'You are now registered'

            print('You are now registered')


    return jsonify({ 'message': message,})




@app.route('/usersignin', methods=['POST'])
def usersignin():

    email = request.form.get('email')
    pas = request.form.get('password')

    error = None

    # print('name is :',name)
    # print('email id',email)
    # print('hashed password is :',pas)
    conn = mysql.connect
    cur = conn.cursor()
    q = ("select name, email, password from userDetail where email = '%s' ") % email
    cur.execute(q)
    rv=cur.fetchone()
    # rv = cur.fetchall()
    print(rv)
    print('Coollllll',type(rv))

    # print(rv[0])
    # print(rv[1])
    # print(rv[2])
    if  not rv:
        message = 'Your details does not exist ! Please register.'
        print('Your details does not exist !')
    else:

        if bcrypt.checkpw(pas.encode(),rv[2].encode()) ==True  :
            message = 'You are permitted to login !'
            print(message)

        else:
            message = "Enter your correct password !"
            print(message)


    # return  "Permitted"

    return jsonify({ 'message': message,})


#########COOKIE SETTING ##############################################################

#
# @app.route('/cookie/')
# def cookie():
#     res = make_response("Setting a cookie")
#     res.set_cookie('foo', 'bar', max_age=60*60*2)
#     return res

@app.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*2)  # max_age is cookie time in second
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
    return res

@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res


@app.route('/article/', methods=['POST', 'GET'])
def article():
    if request.method == 'POST':
        print('Harsh......cool',request.form)
        res = make_response("")
        res.set_cookie("font", request.form.get('font'), 60 * 60 * 24 * 15)
        res.headers['location'] = url_for('article')
        return res, 302

    return render_template('article.html')


@app.route('/visitcount')
def visitcount():
    count = int(request.cookies.get('visit-count',0))
    count +=1
    message = 'You have visited this page ' + str(count) + ' times'

    # make a response, set cookie, return
    resp = make_response(message)
    resp.set_cookie('visit-count', str(count))

    return resp

############################################################################################





if __name__ == '__main__':
    app.run(debug=True)