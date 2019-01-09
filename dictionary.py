def kamus(word):
	dictionary = {'butterfly':'kupu2', 'elephant':'Gajah', 'girrafe':'Jerapah'}

	while word.lower() not in dictionary.keys():
		print("kata tidak ditemukan")
		word = input("Masukan kata lainnya: ")

	if word.lower() in dictionary.keys():
		print("Terjemahan: ", dictionary[word.lower()])

a = input("Masukan kata inggris: ")

kamus(a)