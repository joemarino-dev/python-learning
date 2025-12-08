# Requirements: given a list of english words, return the german equivalent based on user input

sample_dict = {
	"mouth": "Mund",
	"finger": "Finger",
	"leg": "Bein",
	"hand": "Hand",
	"face": "Gesicht",
	"nose": "Nase"
}

english_word = ''

while english_word != 'EXIT':
	english_word = input('Enter a word in English or EXIT: ')
	if english_word == 'EXIT':
		print('Bye!')
		break
	elif english_word in sample_dict:
		print('Translation:', sample_dict[english_word])
	else:
		print('No match!')

# While the above does work, we can de-clutter the code a bit with this

while True:
	english_word = input('Enter a word in English or EXIT: ')
	if english_word == 'EXIT':
		break
	if english_word in sample_dict:
		print('Translation:', sample_dict[english_word])
	else:
		print('No match!')
		
print('Bye!')
