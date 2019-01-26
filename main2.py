from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'test2'

mysql = MySQL(app)


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

if __name__ == '__main__':
    app.run(debug=True)