import sys

def readHeroDataBase(fileName):
	heroData = {}

	categories = ['location', 'income', 'powers', 'contact', 'situations']

	inFile = open(fileName, 'r')
	
	for line in inFile:
		lineList = line[:-1].split(';')
		#print(lineList)
		heroName = lineList[0]
		#print(heroName)
		
		adict = {}
		
		infoList = lineList[1:]
		
		for i in range(2):
			adict[categories[i]] = infoList[i]

		for i in range(2, len(categories)):
			info = infoList[i]
			info  = info.split(',')
			adict[categories[i]] = info
			
		heroData[heroName] = adict
	
	return heroData

def generateHeroReport(heroDB):
	categories = ['location', 'income', 'powers', 'contact', 'situations']

	for hero in heroDB:
		print(f'\n-------{hero}-------\n')
		
		data = heroDB[hero]
		
		print(f"{categories[0]} : {data[categories[0]]}\n")
		print(f"{categories[1]} : {data[categories[1]]}\n")
		
		#printing powers
		print('\n')
		powers = data[categories[2]]
		print(categories[2] + ':', powers[0])
		for i in range(1, len(powers)):
			print(' '*(len(categories[2])+1), powers[i])
		
		#printing contacts
		print('\n')
		contact = data[categories[3]]
		print(categories[3] + ':', contact[0])
		for i in range(1, len(contact)):
			print('         ' + str(contact[i]))
		
		#printing situations
		print('\n')
		situations = data[categories[4]]
		print(categories[4] + ':', situations[0])
		
		for i in range(1, len(situations)):
			print(' '*(len(categories[4])+1), situations[i])
		
		
	 
#allow the user to input new hero information   
def enterHero(fileName):
	out_file = open(fileName, 'a') #a is for append. write erases everything but append keeps the old.
	
	dataString = '\n' 
	
	dataString = dataString + input('Name: ') + ';'
	dataString = dataString + input('Location: ') + ';'
	dataString = dataString + input('Income: ') + ';'
	dataString = dataString + input('Powers (comma separated): ') + ';'
	dataString = dataString + input('Contact Methods (comma separated): ') + ';'
	dataString = dataString + input('Situations (comma separated): ')
	dataString = dataString + '\n'
	out_file.write(dataString)
	out_file.close()

#outputs the hero and his/her info depnding on the input of the sitation
def whoYouGonnaCall(heroDB):
	situation = input(f'\nWhat is your situation? ')
	
	for hero in heroDB:
		situations = heroDB[hero]['situations']
		contacts = heroDB[hero]['contact']
		if situation in situations:
			print(f'\nContact {hero} :\n')
			for contact in contacts:
				print(contact)


#takes a hero name and finds it in the file
def getHeroInfo(heroDB, hero):
	categories = ['location', 'income', 'powers', 'contact', 'situations']

	if hero in heroDB:
		print(f'-------{hero}-------\n')

		data = heroDB[hero]
		
		print(f"{categories[0]} : {data[categories[0]]}\n")
		print(f"{categories[1]} : {data[categories[1]]}\n")
		
		#printing powers
		print('\n')
		powers = data[categories[2]]
		print(categories[2] + ':', powers[0])
		for i in range(1, len(powers)):
			print(' '*(len(categories[2])+1), powers[i])
	   
	   	#printing contacts
		print('\n')
		contact = data[categories[3]]
		print(categories[3] + ':', contact[0])
		for i in range(1, len(contact)):
			print('         ' + str(contact[i]))
		   
		#printing situations 
		print('\n')
		situations = data[categories[4]]
		print(categories[4] + ':', situations[0])
		for i in range(1, len(situations)):
			print(' '*(len(categories[4])+1), situations[i])

	else:
		print(f'\n ----- SUPERHERO NOT IN DB. CONSIDER ADDING THEM -----')
		exit()



def main():
	fileName = sys.argv[1]
	
	heroDB = readHeroDataBase(fileName)
	#print(heroDB)
	options = ['Generate Hero Report', 'Add hero', 'Get Hero Info', 'Find Who To Call']
	opt = int(input(f"\nWhat would you like to do? {options} \n Choose by index [0-3]: "))

	if opt == 0:
		generateHeroReport(heroDB)

	elif opt == 1:
		enterHero(fileName)

	elif opt == 2:
		hero = str(input(f"\nWhich hero would you like to see? "))
		getHeroInfo(heroDB, hero)

	elif opt == 3:
		whoYouGonnaCall(heroDB)

main()
