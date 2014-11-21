from melody_2 import Melody
import os


csv_path = "/Users/justinelee/Projects/Song_Identifier/UNCOMPILED_TRAIN/"

for file in os.listdir(csv_path):
	outname = str(file)[:-4]
	if file.endswith(".csv"):
		model_melody = Melody(csv_path+file,True,1)

		model_melody.get_notes()
		model_melody.get_transitions()

		model_melody.write_transitions("./txtfiles/"+outname+".txt")