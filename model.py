# Filename: model.py
#
# Author: Justine Lee
#
# Description: Wrapper fro the melody class that allows user to compare the differences between
# to melodies

from melody_2 import Melody

class Model:
	def __init__(self, training_filename):
		self.name = training_filename.split(".")
		self.name = self.name[:-4]

		model_melody = Melody(training_filename,True,2)
		model_melody.get_notes()
		model_melody.get_transitions()
		model_melody.count_transitions()

		transitions = model_melody.transition_dictionary
		total = 0
		for transition in transitions:
			total += transitions[transition]
		

		self.transition_likelihoods = {}
		for transition in transitions:
			self.transition_likelihoods[transition] = float(transitions[transition])/float(total)

	# Given another model as input, computes the squared difference between the transition probability
	# dictionaries of the two inputs. Returns an integer value
	def compare_models(self, other_model):
		difference = 0
		for transition in self.transition_likelihoods:
			if transition in other_model.transition_likelihoods:
				other_transition_prob = other_model.transition_likelihoods[transition]
				difference += (self.transition_likelihoods[transition]-other_transition_prob)**2
			else:
				difference += (self.transition_likelihoods[transition])**2

		return difference

	def __str__(self):
		return self.name