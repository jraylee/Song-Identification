# Filename: Classifier.py
#
# Author: Justine Lee
#
# Description: Take in user input at the command line and given a training directory containing
# the csv files of the training examples (1 csv file per song) it generates a dictionary of 
# Model objects. Will then ask for a user specified test directory containing test csv files
# and generates a model for each file and compares it against each Model object in the model 
# dictionary and returns an ordered list of best matches and writes these results to a  csv file

from model import Model
import os
from os.path import basename, abspath
from operator import itemgetter

class Classifier:
	def __init__(self, training_directory):

		self.models = {}
		for file in os.listdir(training_directory):
			if file.endswith(".csv"):
				print basename(file)
				name = basename(file).split('.')
				self.models[name[0]] = Model(training_directory+"/"+file)
				print self.models[name[0]].transition_likelihoods
				print

	def top_matches(self, test_file, num_matches, write_out = False):
		other_model = Model(test_file)

		differences = {}

		for model in self.models:
			differences[model] = self.models[model].compare_models(other_model)

		matches = sorted(differences.items(), key=itemgetter(1))
		
		i=0
		while i<num_matches and i<len(matches):
			print matches[i]
			i+=1

		return differences


training = raw_input("Please enter path to training directory: ")

classifier_1 = Classifier(training)

test_directory = " "
while 1:
	test_directory = raw_input("Please enter path to test directory: ")
	continue_on = 0
	if os.path.exists(test_directory):
		while continue_on == 0:
			outfilename = raw_input("Please enter name for output file: ")

			if os.path.isfile(outfilename):
				overwrite = raw_input(outfilename + " exists, enter 1 to proceed and 0 to cancel: ")
				if int(overwrite) != 0:
					continue_on = 1

			else:
				continue_on = 1

		outfile = open(outfilename,'w')
		correct = 0
		total = 0
		for file in os.listdir(test_directory):
			if file.endswith(".csv"):
				print file
				outfile.write(file+"\n")
				name = basename(file).split('.')
				differences = classifier_1.top_matches(test_directory+"/"+file,2,True)

				matches = sorted(differences.items(), key=itemgetter(1))

				match0,difference = matches[0]
				match1,difference = matches[1]
				# print "match 0: " + str(match0)
				if match0 in str(file).upper() or match1 in str(file).upper():
					correct += 1

				matches = sorted(differences.items(),key=itemgetter(0))

				for item in matches:
					match,difference = item
					outfile.write(str(match) +","+str(difference) + "\n")
				outfile.write("\n")
				print
				total += 1
		print "NUMBER CORRECT MATCHES: " + str(correct)
		print "TOTAL: " + str(total)
		if total != 0:
			print "Error: " + str(1-float(correct)/float(total))
		outfile.close()
	else:
		print "Please select an existing directory\n"

