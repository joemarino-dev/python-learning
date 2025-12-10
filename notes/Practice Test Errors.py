# practice questions I got wrong
# answered three but it was simple I just didn't count all the transitions correctly
dict = {'one':'two', 'three':'one', 'two':'three'}
v = dict['three']

for k in range(len(dict)):
	v = dict[v]

print(v)

# answered asepbsepcsep but I screwed up diff between sep and end keyword arguments
print("a", "b", "c", sep="sep")

# index wasn't in any of my study materials so I had no clue on this - turns out index function attempts to find the position, given the value - since 0 (which is a legit type for this argument) does not appear in the tuple you get a value error
foo = (1, 2, 3)
#foo.index(0)

# didn't understand that inserting at last position would not actually be the last position, it would be the second to last because it pushed existing value to the right
my_list = [1, 2]

for v in range(2):
	my_list.insert(-1, my_list[v])
	
print (my_list)

# for some reason I thought I remembered that you cannot have the generic except block before the spefic one but I guess that's not true - ACTUALLY - turns out that the problem was a syntax error due to the break appearing outside the context of a loop - I completely missed that. (and for the record I was right the default does need to be last)
# try:
	 # print(5/0)
#	break
# except:
	# print('Sorry, something went wrong...')
# except (ValueError, ZeroDivisionError, ):
	# print('Too bad...')

# thought this would be a type error for sure but I guess it is because Python thought these were variables and not defined ones	
# print(Hello, World!)

# this tricked me because I didn't realize vals was not the right method name - it is values. If this were using values my answer I gave was correct at any rate...
dd = {"1":"0", "0":"1"}
for x in dd.vals():
	print(x, end="")
