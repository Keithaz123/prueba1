Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> country=["Brazil","Russia","India","China","South Africa"]
>>> capitals={"Brazil":"Brasilia","Russia":"Moscow","India":"New Delhi","China":"Beijing","South Africa":["Pretoria","Cape Town","Bloemfontein"]}
>>> print("country")
country
>>> print("capitals")
capitals
>>> print(capitals["South Africa"[1]])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(capitals["South Africa"[1]])
KeyError: 'o'
>>> print(country)
['Brazil', 'Russia', 'India', 'China', 'South Africa']
4
>>> print(country)
['Brazil', 'Russia', 'India', 'China', 'South Africa']
>>> print(capitals)
{'Brazil': 'Brasilia', 'Russia': 'Moscow', 'India': 'New Delhi', 'China': 'Beijing', 'South Africa': ['Pretoria', 'Cape Town', 'Bloemfontein']}
>>> print(capitals["South Africa"][1])
Cape Town
>>> 