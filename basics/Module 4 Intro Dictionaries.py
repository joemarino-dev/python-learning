# dictionaries are key value pairs that are looked up by referencing the name and getting the value

emails = {
	'Joe Marino': 'joe@test1.test',
	'Devin Townsend': 'devin@test2.test',
	'Wilma Flintstone': 'wilma@test3.test'
}

print(emails['Joe Marino'])

translator = {
	'bird': 'Pájaro',
	'dog': 'Perro',
	'horse': 'Caballo',
	'cat': 'Gato',
}

print(translator['dog'])

# given the key value nature of dictionaires - keys must be unique!
# dictionary is a one way tool - you can't reference a value and expect a name
# integers floats and tuples can be keys within a dictionary too - but not lists as they are mutable!
# however, lists could become values

album_sales = {
	'Devin Townsend': [22.5, 31.2, 44.3],
	'Metallica': [151.6, 190, 200],
	'Morbid Angel': [13.3, 6.66, 12]
}

print(album_sales['Devin Townsend'])
