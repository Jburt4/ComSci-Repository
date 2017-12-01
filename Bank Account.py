import random
class Account:
	def __init__(self):
		self.balance = 0
		self.interest = 0.1
		self.pin = 0
		self.accountnumber = int(random.uniform(10000000,99999999))
		self.open = 0

	def stats(self):
		print('Current Balance: $' + self.balance)
		print('Interest: ' + self.interest)
		print('Account Number: ' + self.accountnumber)

	def open(self):
		opening = input('Would you like to open an account?Y/N')
		if opening == 'Y':
			self.open += 1
			userpin = int(input('What would you like your pin to be?\n'))
			self.pin = userpin
			initialDeposit = int(input('How much money would you like to deposit?\n'))
			self.balance = initialDeposit
			print('You will earn 10% Interest.\n')
			print(str(self.accountnumber) + ' is your account number')
			account1.stats()
		else:
			print('Okay bye!')

	def deposit(self):
		userpin = int(input('What is your pin number?'))
		if userpin == self.pin:
			newdeposit = int(input('How much would you like to deposit?'))
			self.balance += newdeposit
			account1.stats()
		else:
			print('Wrong pin')

	def withdrawal(self):
		userpin = int(input('What is your pin number?'))
		if userpin == self.pin:
			newwithdrawal = int(input('How much would you like to withraw?'))
			while newwithdrawal > self.balance:
				print('Sorry you do not have enough money in your account')
				account1.stats()
				newwithdrawal = int(input('How much would you like to withraw?'))
		else:
			print('Wrong pin')

	def close(self):
		userpin = int(input('What is your pin number?'))
		if userpin == self.pin:
			self.close -= 1
			print('You get $' + self.balance + ' back from the bank')
			self.balance -= self.balance
		else:
			print('Wrong pin')

account1 = Account()
x = 1
while x==1:
	account1.open()
	action= int(input('1 for deposit, 2 for withdrawal, or 3 for close.'))
	if action == 1:
		account1.deposit()
	elif action == 2:
		account1.withdrawal()
	elif action ==3:
		account1.close()
		x-=1
		print('Okay Bye!')
	else:
		print('That is not an option')
