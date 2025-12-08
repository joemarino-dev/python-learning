# inefficient
band_1 = 'Devin Townsend'
band_2 = 'Anthrax'
band_3 = 'Morbid Angel'
band_4 = 'Death'
band_5 = 'At The Gates'

 # this is where lists (container/collection data type) come into play
empty_list = []
 
top_bands = ['Devin Townsend', 'Anthrax', 'Morbid Angel', 'Death', 'At The Gates']
print(top_bands)

print(top_bands[0])
print(top_bands[1])

# since lists are indexed from 0 to n-1, this will produce a list index out of range error
# print(top_bands[5])

# unique in Python - you can reference negative indices which flips to starting from end of list and working way to left
print(top_bands[-1])
print(top_bands[-2])

# note that since the negative indices start w/-1 to represent the last item, this time list will go up to -n
print(top_bands[-5])

# slicing can take parts of list based on index range
# get 0 to index 2
print(top_bands[0:2])

# get 0 to index 3 alternate method
print(top_bands[:3])

# get 3 to end of list
print(top_bands[3:])

# unlike a specific index out of range getting error, slicing out of range does not produce error you just get empty list or empty for the portion that does not exist

print(top_bands[10:15])
print(top_bands[3:15])
