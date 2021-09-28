Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> naam = Rico
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    naam = Rico
NameError: name 'Rico' is not defined
>>> naam = 'Rico'
>>> print(naam)
Rico
>>> print(naam.upper())
RICO
>>> print(naam[0:2])
Ri
>>> print(naam[::-1])
ociR
>>> leeftijd = 16
>>> print(leeftijd)
16
>>> hoelang_tot18jaar = 18 - leeftijd
>>> print('over ' + str(hoelang_tot18jaar) + ' jaar word je 18')
over 2 jaar word je 18
>>> randint(0,1000)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    randint(0,1000)
NameError: name 'randint' is not defined
>>> willegeurig_getal = randint(0,1000)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    willegeurig_getal = randint(0,1000)
NameError: name 'randint' is not defined
>>> datum = datetime.now()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    datum = datetime.now()
NameError: name 'datetime' is not defined
>>> locale.setlocalw(locale.LC_TIME. 'nl_NL'
		 
SyntaxError: invalid syntax
>>> locale.setlocalw(locale.LC_TIME. 'nl_NL')
SyntaxError: invalid syntax
>>> 