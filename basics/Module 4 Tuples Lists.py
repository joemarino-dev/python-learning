band_1 = ('Devin Townsend', 'Progressive Metal', 1)
band_2 = ('Metallica', 'Thrash Metal', 4)
band_3 = ('Nirvana', 'Grunge', 3)

# given the tuples above, you could have these stored in a list
bands = [('Devin Townsend', 'Progressive Metal', 1), ('Metallica', 'Thrash Metal', 4), ('Nirvana', 'Grunge', 3)]

for band in bands:
	print('Name:', band[0], ', Genre:', band[1], ', # Members:', band[2])
	
# you can have lists in tuples too e.g., bands want to track annual record sales
band_data = ('Devin Townsend', 'Progressive Metal', 1, [22.5, 25.3, 12.4])
print(band_data)
band_data[3].append(51.2)
print(band_data)
