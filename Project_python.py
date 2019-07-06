import random
import os

class Project:
	def __init__(self, file):
		self.fileName = file

	def open_file(self):
		file = open(self.fileName, "r")
		return file

	def read_file(self):
		descriptions = self.open_file().read().split("\n\n")
		
		each_descriptions = list()
		for each in descriptions:
			each_descriptions.append(each.split("\n"))
		return each_descriptions

	def calculate(self, correct_number, count):
		return (correct_number * 100) / count


	def start(self):
		questions = self.read_file()
		random.shuffle(questions)

		print("=======================================================================\n")
		print("WELCOME TO {} QUIZ!".format(self.fileName[:(len(self.fileName) - 4)]))
		print("_______________________________________________________________________")

		count = 1
		correct_count = 0
		for each in questions:
			if len(each) == 2:
				description = each[0].replace("{blank}", "______")
				print(str(count) + ". " + description)
				print("-----------------------------------")
				answer = input('Type your answer: ')
				if (answer.lower() == each[1].lower()):
					correct_count += 1
					print("Correct!")
				else:
					print("Incorrect!")
				print("_______________________________________________________________________\n")
			else:
				print(str(count) + ". " + each[0])

				#print options and split into variants
				options = list()
				for i in range(1, len(each)):
					options.append(each[i])
				random.shuffle(options)

				new_option = dict()
				variants = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
				for i in range(0, len(options)):
					new_option[variants[i]] = options[i]

				for key, value in new_option.items():
					print(key + ") " + value)
				print("-----------------------------------")
				answer = input("Enter the correct choice: ")
				while (len(answer) != 1 or answer.islower()):
					answer = input("Invalid choice! Try again (Ex: A, B, ...): ")

				if (new_option[answer] == each[1]):
					correct_count += 1
					print("Correct!")
				else:
					print("Incorrect!") 
				print("_______________________________________________________________________\n")

			count += 1

		"""calculate results"""
		print("Correct answers: {}/{} ({:.2f}%)".format(correct_count, count - 1, self.calculate(correct_count, count - 1)))

project = Project("quiz.txt")
project.start()
