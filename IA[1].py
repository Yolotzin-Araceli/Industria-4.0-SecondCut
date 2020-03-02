username = 'Pal'
level = 0
gossip = None
music= None
book=None
major= None

print(f'Hello, {username}' )

# Ask user input
print("I will ask for some questions to rate your level of How interestig are you (leave it blank if you don't want to tell me)")
print(" ")
print("Let's start")
print(" ")
gossip=input('Gossip is my passion, so if you have a good gossip write it here (if not press enter to continue): ')
if(gossip != ''):
	level = level + 1
print(" ")
music = input('Everybody loves music, if you have to choose between pop, rock or reggaeton What would you choose (if you do not like any of this kind of music press enter to continue): ')
if(music != ''):
	if music == 'pop':
		level = level + 1
	elif music == 'rock':
		level = level + 1
	elif music == 'reggaeton':
		print(f'Come on({str_gender})! you need to listen more kind of music')
	else:
		print(f'({music}) does not exist in my database ')
print(" ")
book= input('Reading is important in our lifes, write down Which was the book that change your life:')
if book != '':
	level = level + 1
print(" ")
major= input('What major do you study? (if you do not study press enter to finish with this Awkward questionnaire):')
if major != '':
	level = level + 1
print(" ")
# Selection of the response
if level == 0:
	print( f'Whitout offending you, you are really bored, Come back when you have some interesting stuff to tell me ')
elif level <4:
	print( f' You are interesting but it is not enought, sorry :c ')
else:
	print( f"Thx {username}. You are a crack and you are very interesting, i need to meet you right now." 