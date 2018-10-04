#!/usr/bin/python
import cgi
import cgitb

def doit(a, b, c):
    print "Parameters: ", a, " ", b, " ", c

def main():
    print "Content-type:text/html\n\n"
    cgitb.enable()
    form = cgi.FieldStorage()
    Last = (form.getvalue('lname')).lower()
    First = (form.getvalue('fname')).lower()
    Middle = (form.getvalue('mname')).lower()
    output = doit(Last, First, Middle)

if __name__ == "__main__":
    main()
