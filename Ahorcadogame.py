import random as rd

words = ['gato','perro','pepino','casa','mecanico','ornitorinco','avion','pantalon']

player_att = 0
max_att = 5
player_letters_corrects = [ ]
word_is = ''
letters_word = []

def select_word ():
	word_index = rd.randint(0,3)
	word_selected = words[word_index]
	return word_selected
	
def now_game ():
	print(f'Tienes {player_att} fallos de {max_att} intentos')
	print(f'Las letras que has adividado son: {player_letters_corrects}')
	print('')
	print('Buena suerte!')

def guess (r):
	for i,e in enumerate(letters_word):
		if e == r:
			player_letters_corrects[i] = e

def victory():
	player_word = ''.join(player_letters_corrects)
	if word_is == player_word and player_att <= max_att:
		print('Felicitaciones adivinaste la palabra, la palabra era: ', player_word)
		return True
	elif max_att == player_att:
		print('Perdiste crack')
		return True

def repeat ():
	print('Para volver a jugar escibe cualquier letra o deja en blanco para salir')
	res = input('Desea volver a jugar?:')
	if res == '':
		return False
	
def game ():
	global player_att
	global word_is
	global player_letters_corrects
	global letters_word
	player_att = 0
	word_is = ''
	player_letters_corrects = []
	
	word_is = select_word()
	letters_word = list(word_is)
	word_len = len(word_is)
	
	for i in range(word_len):
		player_letters_corrects.append('')
		
	while True:
		now_game()
		res = input('Escribe una letra: ')
		
		try:
			letters_word.index(res)
			guess(res)
		except:
			player_att += 1
			
		win = victory()
		if win == True:
			break

def beginner ():
	while True:
		game()
		restar = repeat()
		if restar == False:
			print('ADIOS!')
			break
		
beginner()