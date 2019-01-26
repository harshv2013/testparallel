PyDev
console: starting.
Python
3.5
.2(default, Nov
12
2018, 13: 43:14)
[GCC 5.4.0 20160609]
on
linux
password = "superman"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
NameError: name
'bcrypt' is not defined
import bcrypt

hashed = bcrypt.hashpw(password, bcrypt.gensalt())
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
File
"/home/harsh/testparallel/venv/lib/python3.5/site-packages/bcrypt/__init__.py", line
61, in hashpw
raise TypeError("Unicode-objects must be encoded before hashing")
TypeError: Unicode - objects
must
be
encoded
before
hashing
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
hashed
b'$2b$12$gb8E3.b6iDMzUBjCr9U01.VG65/7vM97SrzLFl4s7zuWsR.hz2F6q'
p = 'superman'
if bcrypt.checkpw(p.encode(), hashed):
    print("It Matches!")
else:
    print("It Does not Match :(")

It
Matches!
