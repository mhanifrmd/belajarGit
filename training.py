
dictionary = {'car':'mobil', 'motorcycle':'sepeda motor', 'cat':'kucing', 'dog':'anjing'}

a = input('masukan kata:')

for k,v in dictionary.items():
	if a.lower()==k:
		print(v)