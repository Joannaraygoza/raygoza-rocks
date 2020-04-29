import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

class WOFPlayer:
	def __init__(self, name):
		self.name = name
		self.prizeMoney = 0
		self.prizes = []

	def addMoney(self, amt):
		self.prizeMoney += amt

	def goBankrupt(self):
		self.prizeMoney = 0

	def addPrize(self, prize):
		self.prizes.append(prize)

	def __str__(self):
		return '{} (${})'.format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
	def getMove(self, category, obscuredPhrase, guessed):
		move = input(
			"""{} has ${}
			Category: {}
			Phrase: {}
			Guessed: {}

			Guess a letter, phrase, or type 'exit' or 'pass':
			""".format(self.name, self.prizeMoney, category, obscuredPhrase, guessed))
		return move

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
	SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

	def __init__(self, name, difficulty):
		WOFPlayer.__init__(self, name)
		self.difficulty = difficulty

	def smartCoinFlip(self):
		value = random.randint(1,10)
		if value > self.difficulty:
			return True
		else:
			return False

	def getPossibleLetters(self, guessed):
		possible = []
		for letter in LETTERS:
			if letter in guessed:
				pass
			elif letter in VOWELS:
				if self.prizeMoney >= VOWEL_COST:
					possible.append(letter)
			else:
				possible.append(letter)
		return possible
		
	def getMove(self, category, obscuredPhrase, guessed):
		possible = self.getPossibleLetters(guessed)
		if possible == []:
			return 'pass'
		
		if self.smartCoinFlip():
			for letter in self.SORTED_FREQUENCIES:
				if letter in possible:
					return letter
		else:
			return random.choice(possible)

bob = WOFComputerPlayer('Bob', 2)
print(bob.getMove('hello', '__a__we__', 'A, B, E, H, V, W'))
