Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/Keith/Desktop/Phyton/01_hello-world.py ===========
Hello World!
>>> 
=========== RESTART: C:/Users/Keith/Desktop/Phyton/01_hello-world.py ===========
Hello World!
>>> type(98)
<class 'int'>
>>> type(98.6)
<class 'float'>
>>> type("Hi!")
<class 'str'>
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> 1<2
True
>>> 1>2
False
>>> 1==1
True
>>> 1!=1
False
>>> 1>=1
True
>>> 1<=1
True
>>> x=3
>>> x*5
15
>>> "cisco"*x
'ciscociscocisco'
>>> "cisco"*x+2
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    "cisco"*x+2
TypeError: can only concatenate str (not "int") to str
>>> str1="cisco"
>>> str2="Networking"
>>> str3="Academy"
>>> space=" "
>>> print(str1+space+str2+space+str3)
cisco Networking Academy
>>> 
=========== RESTART: C:/Users/Keith/Desktop/Phyton/01_hello-world.py ===========
Hello World!
Traceback (most recent call last):
  File "C:/Users/Keith/Desktop/Phyton/01_hello-world.py", line 4, in <module>
    Print(str1+ +str2+ +str3)
NameError: name 'Print' is not defined
>>> 
=========== RESTART: C:/Users/Keith/Desktop/Phyton/01_hello-world.py ===========
Hello World!
Traceback (most recent call last):
  File "C:/Users/Keith/Desktop/Phyton/01_hello-world.py", line 4, in <module>
    Print(str1+ +str2+ +str3)
NameError: name 'Print' is not defined
>>> 
=========== RESTART: C:/Users/Keith/Desktop/Phyton/01_hello-world.py ===========
Hello World!
Traceback (most recent call last):
  File "C:/Users/Keith/Desktop/Phyton/01_hello-world.py", line 4, in <module>
    Print(str1+ +str2+ +str3)
NameError: name 'Print' is not defined
>>> 
=========== RESTART: C:/Users/Keith/Desktop/Phyton/01_hello-world.py ===========
Hello World!
srt1
>>> 
=========== RESTART: C:/Users/Keith/Desktop/Phyton/01_hello-world.py ===========
Hello World!
Traceback (most recent call last):
  File "C:/Users/Keith/Desktop/Phyton/01_hello-world.py", line 2, in <module>
    print(srt1)
NameError: name 'srt1' is not defined
>>> 
=========== RESTART: C:/Users/Keith/Desktop/Phyton/01_hello-world.py ===========
Hello World!
Traceback (most recent call last):
  File "C:/Users/Keith/Desktop/Phyton/01_hello-world.py", line 3, in <module>
    print(str1)
NameError: name 'str1' is not defined
>>> print(str1+ str2+ str3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(str1+ str2+ str3)
NameError: name 'str1' is not defined
>>> str1="cisco"
>>> str2=" Networking"
>>> str3=" Academy"
>>> print=(str1+str2+str3)
>>> 
>>> print(str1+str2+str3)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(str1+str2+str3)
TypeError: 'str' object is not callable
>>> print(str2)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(str2)
TypeError: 'str' object is not callable
>>> str2="Networking"
>>> print(str2)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(str2)
TypeError: 'str' object is not callable
>>> print(str1+space+str2+space+str3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(str1+space+str2+space+str3)
NameError: name 'space' is not defined
>>> str1="cisco"
>>> str2="Networking"
>>> str3="Academy"
>>> space=" "
SyntaxError: multiple statements found while compiling a single statement
>>> str1="cisco"
>>> str2="Networking"
>>> str3="Academy"
>>> space=" "
>>> print(str1+space+str2+space+str3)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(str1+space+str2+space+str3)
TypeError: 'str' object is not callable
>>> 