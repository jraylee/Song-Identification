import math

class Melody:
	
	def __init__(self, csv_path, uncertainty_on,num_octaves):
		#Open csv file
		csv_file = open(csv_path,'r')

		self.frequencies = []
		self.notes = []
		self.transitions = []
		self.transition_dictionary = {}

		for line in csv_file:
			line_split=line.split(",")
			frequency = int(math.floor(round(float(line_split[1].strip()))))
			if (frequency>0 or uncertainty_on) and frequency != 0:
				self.frequencies.append(abs(frequency))


		csv_file.close()

	def get_notes(self):
		i = 0
		while i<len(self.frequencies):
			note = 12*math.log((float(self.frequencies[i])/440.0),2)
			self.notes.append(round(note)%12)
			i+=1

	def get_transitions(self):
		i = 0
		while i < len(self.notes)-1:
			transition = int(self.notes[i+1]-self.notes[i])
			if transition != 0:
				self.transitions.append(transition)
			i += 1

	def count_transitions(self):
		for transition in self.transitions:
			if transition not in self.transition_dictionary:
				self.transition_dictionary[transition] = 0

		for transition in self.transitions:
			self.transition_dictionary[transition] += 1

	def write_transitions(self,outfile):
		transition_file = open(outfile, 'w')

		i = 0
		while i < len(self.transitions):
			transition_file.write(str(self.transitions[i])+"\n")
			i += 1

		transition_file.close()