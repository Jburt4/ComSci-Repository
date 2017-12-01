#Clases
#Doge: Diet, Hunger, Thirst, Obedience, Energetic, Name, Asthetics
#Actions: Walk, Fetch, Pet, Run, Eat, Bark, Sleep, Potty, Drink

class Puppy:

	#constructor
	def __init__(self, name):
		self.name = name
		self.hunger = 50
		self.thirst = 50
		self.obedience = 50
		self.energy = 50

	def stats(self):
		print('Dog Stats:')
		print('Name: '+ str(self.name))
		print('Hunger: '+ str(self.hunger))
		print('Thirst: '+ str(self.thirst))
		print('Obedience: '+ str(self.obedience))
		print('Energy: '+ str(self.energy), end='\n\n')

	def fetch(self):
		if self.energy <= 0:
			print('Too Tired. I cannot fetch.')
		elif self.energy < 20:
			print('Look Out the Dog is tired')
		if self.hunger > 0:
			self.energy -= 5
			self.obedience += 5
			self.hunger += 5
			self.thirst += 10



mydog1 = Puppy('Wrex')
mydog1.stats()
mydog1.fetch()
mydog1.fetch()
mydog1.fetch()
mydog1.fetch()
mydog1.stats()