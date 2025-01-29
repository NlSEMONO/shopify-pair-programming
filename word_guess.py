import random

class WordGuess:
    # choices = all possible target words for the guessing game
	choices = ["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"]
	target = ""
	def choose_target(self):
		self.target = random.choice(self.choices)

	def verify_guess(self, guess: str):
		return guess == self.target

wg = WordGuess()
wg.choose_target()
print(wg.target)
a=input()
print(wg.verify_guess(a))
