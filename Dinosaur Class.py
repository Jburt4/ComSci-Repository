class Dinosaur:

	def __init__(self, name):
		self.name = name
		self.fullness = 50
		self.hydration = 50
		self.energy = 50
		self.rideability = 20
		self.friendliness = 20

	def stats(self):
		print('Fullness: '+ str(self.fullness))
		print('Hydration: '+ str(self.hydration))
		print('Energy: '+ str(self.energy))
		print('Rideability: '+ str(self.rideability))
		print('Friendliness: '+ str(self.friendliness))

	def fetch(self):
		global name
		if self.energy <= 0:
			print('Too Tired. I cannot fetch.')
		elif self.energy <= 20 or self.hydration <= 20 or self.fullness <= 20:
			print('LOOK OUT!' + name + ' is not feeling right. It must need something.\n')
		if self.energy > 0:
			print(name + ' caught the ball and brought it back.')
			self.energy -= 5
			self.friendliness += 5
			self.fullness -= 5
			self.hydration -= 10
			self.rideability += 10

	def eat(self):
		global name
		if self.fullness>= 100:
			print(name + ' is full and cannot eat anymore')
		else:
			print(name + ' munched on the delicious food that you gave it. It looks happier now.')
			self.fullness += 50
			self.friendliness += 10
			self.rideability += 15
			self.energy += 30
			if self.fullness < 80:
				print(name + ' is still hungry an would like to eat more')

	def drink(self):
		global name
		if self.hydration>= 100:
			print(name + ' is no longer thirsty and does not want to drink anymore.')
		else:
			print(name + ' sips some yummy water from its bowl. It looks happier now.')
			self.hydration += 50
			self.friendliness += 10
			self.rideability += 15
			self.energy += 30
			if self.hydration < 80:
				print(name + ' is still thirsty an would like to drink more.\n')

	def nap(self):
		global name
		if self.energy >=100:
			print(name + ' has too much energy and cannot sleep right now.')
		else:
			print(name + ' curled up in a ball and slept for a good 2 hours.')
			self.energy += 50
			self.rideability +=15
			self.fullness -= 20
			self.hydration -= 15
			self.friendliness += 20
			if self.energy < 80:
				print(name + ' is still tired and would like to sleep more.')

	def ride(self):
		global name
		if self.rideability >= 50:
			print(' You hop on ' + name + ' and ride arond the forrest for a while.')
			self.fullness -=20
			self.hydration -=30
			self.rideability += 10
			self.energy -= 20
			self.friendliness +=5
		elif self.energy <= 20 or self.hydration <= 20 or self.fullness <= 20:
			print('Look Out!' + name + ' is not feeling right. It must need something.')
			dinosaur.stats()
		if self.rideability < 50:
			print('Your dinosaur throw you off, bites you, then runs away because your rideability is not high enough.')
			self.energy = 0
	def loop(self):
		while self.energy > 0 and self.fullness > 0 and self.hydration > 0:
			print('Would you like your dinosaur to play fetch, eat, drink, nap, or let you ride it?')
			next = int(input('Print 1 for fetch, 2 to eat, 3 to drink, 4 for nap, 5 for a ride?'))
			while next != 1 and next != 2 and next != 3 and next != 4 and next != 5:
				print('That is not an option. Try again.')
				next = int(input('Print 1 for fetch, 2 to eat, 3 to drink, 4 for nap, 5 for a ride?'))
			if next == 1:
				dinosaur.fetch()
			if next == 2:
				dinosaur.eat()
			if next == 3:
				dinosaur.drink()
			if next == 4:
				dinosaur.nap()
			if next == 5:
				dinosaur.ride()
			dinosaur.stats()
			dinosaur.loop()
while 1==1:
	name = input('What would you like to name your dinosaur?')
	dinosaur = Dinosaur(name)
	dinosaur.stats()
	dinosaur.loop()
	print('Your dinosaur ended up dying because of you.')
	print('You go to the store and get another.')