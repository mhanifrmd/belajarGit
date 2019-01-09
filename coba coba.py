Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> hello
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> print("hello")
hello
>>> nama = 'budi'
>>> print("hello, my name is", nama)
hello, my name is budi
>>> Umur = 22
>>> print("hello, my name is", nama "I am", Umur "years old")
SyntaxError: invalid syntax
>>> print("hello, my name is", nama, "I am", Umur, "years old")
hello, my name is budi I am 22 years old
>>> lastname = "Daya"
>>> fullname = nama+lastname
>>> lastbanget = "ikan"
>>> full = fullname + " " + lastbanget
>>> full
'budiDaya ikan'
>>> fullname
'budiDaya'
>>> 10/3
3.3333333333333335
>>> 10/2
5.0
>>> data = [10,20,30] #mebuat list (array)
>>> data
[10, 20, 30]
>>> tipe = type(data)
>>> tipe
<class 'list'>
>>> data.append = 'python'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    data.append = 'python'
AttributeError: 'list' object attribute 'append' is read-only
>>> data.append('python')
>>> data
[10, 20, 30, 'python']
>>> len(data)
4
>>> data.insert(0, 'anaconda')
>>> data
['anaconda', 10, 20, 30, 'python']
>>> data.extend([90,90,90])
>>> data
['anaconda', 10, 20, 30, 'python', 90, 90, 90]
>>> data
['anaconda', 10, 20, 30, 'python', 90, 90, 90]
>>> data.remove(90)
>>> data
['anaconda', 10, 20, 30, 'python', 90, 90]
>>> data.del[2]
SyntaxError: invalid syntax
>>> data
['anaconda', 10, 20, 30, 'python', 90, 90]
>>> data.del(2)
SyntaxError: invalid syntax
>>> data.del[2]
SyntaxError: invalid syntax
>>> del data [2]
>>> data
['anaconda', 10, 30, 'python', 90, 90]
>>> while 90 indata;
SyntaxError: invalid syntax
>>> while 90 in data:
	data.remove(90)
	;
	
SyntaxError: invalid syntax
>>> while 90 in data:
	data.remove(90):
		
SyntaxError: invalid syntax
>>> while 90 in data:
	data.remove (90)

	
>>> data
['anaconda', 10, 30, 'python']
>>> data3 = [1,2,3,4,5,6,7,8,9,10]
>>> ganjil = []
>>> for i in data3:
	if i%2 == 1:
		ganjil.append(i)

		
>>> ganjil
[1, 3, 5, 7, 9]
>>> genap = [x for x in data3 if x%2 == 0]
>>> genap
[2, 4, 6, 8, 10]
>>> # dictionary
>>> kota = ('jkt':'jakarta', 'bdg':'bandung', 'sby':'surabaya')
SyntaxError: invalid syntax
>>> kota = {'jkt':'jakarta', 'bdg':'bandung', 'sby':'surabaya'}
>>> type(kota)
<class 'dict'>
>>> for k,v in kota.items():
	print("%s -> %s" % (k,v))

	
bdg -> bandung
jkt -> jakarta
sby -> surabaya
>>> dataFroz = (10,20,30)
>>> dataFroz
(10, 20, 30)
>>> a = 'jbKJbhFkISLF'
>>> a.lower()
'jbkjbhfkislf'
>>> def kamus():
a = input('masukan kata:')

dictionary = {'car':'mobil', 'motorcycle':'sepeda motor', 'cat':'kucing', 'dog':'anjing'}

for k,v in dictionary.items():
							if a.lower()==k:
								return(v)
							else:
								return('tidak ditemukan')
							
SyntaxError: expected an indented block
>>> def kamus():
a=input('masukan kata:')

dictionary = {'car':'mobil', 'motorcycle':'sepeda motor', 'cat':'kucing', 'dog':'anjing'}

for k,v in dictionary.items():
							if a.lower()==k:
								return(v)
							else:
								return('tidak ditemukan')
							
SyntaxError: expected an indented block
>>> # set <- list dengan value unique
>>> listA = [1,2,3]
>>> listB = [2,2,3,4,5,6,7]
>>> sl = set(listB)
>>> sl
{2, 3, 4, 5, 6, 7}
>>> il = sl.intersection(listA)
>>> il
{2, 3}
>>> il = sl.intersection(listB)
>>> il
{2, 3, 4, 5, 6, 7}
>>> ul = sl.union(listB)
>>> ul
{2, 3, 4, 5, 6, 7}
>>> listB.append(9)
>>> litB
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    litB
NameError: name 'litB' is not defined
>>> listB
[2, 2, 3, 4, 5, 6, 7, 9]
>>> ul = sl.union(listB)
>>> ul
{2, 3, 4, 5, 6, 7, 9}
>>> 
>>> # string
>>> 
>>> s = 'belajar python'
>>> s[3]
'a'
>>> s[-1]
'n'
>>> s[:2]
'be'
>>> s[:3]
'bel'
>>> # data splitting
>>> 
>>> data = 'p01,pulpen,5000.0'
>>> data.split(',')
['p01', 'pulpen', '5000.0']
>>> kode = data.split(',')[0]
>>> barang = data.split(',')[1]
>>> harga = data.split(',')[2]
>>> kode
'p01'
>>> barang
'pulpen'
>>> harga
'5000.0'
>>> code, item, price = data.split(',')
>>> code
'p01'
>>> item
'pulpen'
>>> price
'5000.0'
>>> 
>>> 
>>> 
>>> 
