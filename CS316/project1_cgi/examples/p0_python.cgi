#!/usr/bin/python
import cgi

def doit(a, b, c):
    print "Parameters: ", a, " ", b, " ", c

def main():
    form = cgi.FieldStorage()
    Last = (form.getvalue('lname')).lower()
    First = (form.getvalue('fname')).lower()
    Middle = (form.getvalue('mname')).lower()
    print "Content-type:text/html\n\n"
    output = doit(Last, First, Middle)

if __name__ == "__main__":
    main()
