Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=3
>>> print("This value of x is" +x)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print("This value of x is" +x)
TypeError: can only concatenate str (not "int") to str
>>> print("This value of x is" + str(x))
This value of x is3
>>> print("This value of x is "+str(x))
This value of x is 3
>>> type(x)
<class 'int'>
>>> x=str(x)
>>> type(x)
<class 'str'>
>>> print("This value of x is "+str(x))
This value of x is 3
>>> type(x)
<class 'str'>
>>> num=22/7
>>> print(num)
3.142857142857143
ç
>>> print(num)
3.142857142857143
>>> print("{:.2f}".format(num))
3.14
>>> hostnames=["R1","R2","R3","S1","S2"]
>>> type(hostnames)
<class 'list'>
>>> len(hostnames)
5
>>> hostnames
['R1', 'R2', 'R3', 'S1', 'S2']
>>> hostnames[0]
'R1'
>>> hostnames[1]
'R2'
>>> hostnames[2]
'R3'
>>> hostnames[3]
'S1'
>>> hostnames[4]
'S2'
>>> hostnames[-1]
'S2'
>>> hostnames[0]="RTR1"
>>> hostnames
['RTR1', 'R2', 'R3', 'S1', 'S2']
>>> del hostnames[3]
>>> hostnames
['RTR1', 'R2', 'R3', 'S2']
>>> 