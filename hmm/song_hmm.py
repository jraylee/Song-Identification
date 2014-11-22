'''
Created on Nov 16, 2014

@author: Jacob Utter
'''

import hmm_faster
import math



def initial_obs(song_file):
    finput = open(song_file, 'r')
    observations = []
    
    for line in finput:
        line = line.replace("\n","")
        if observations.__contains__(line) != True:
            observations.append(line)
            
        
    finput.close()
    return observations

def obs_array(song_file):
    finput = open(song_file, 'r')
    observations = []
    first_time = True
    
    for line in finput:
        line = line.replace("\n","")
        if first_time == True:
            observations.append(line)
            first_time = False
        elif line != observations[len(observations)-1] and abs(int(line) - int(observations[len(observations)-1])) > 20:
            print(abs(int(line) - int(observations[len(observations)-1])))
            observations.append(line)
        #if len(observations) > 30:
            #break
            
        
    finput.close()
    return observations

def markov_trainer(song_file, model):
    finput = open(song_file, 'r')
    observations = []
    prev_line = ""
    line_num = 1
    first_time = True
    
    for line in finput:
        line = line.replace("\n","")
        observations.append(line)
        if prev_line.__eq__(line) and len(observations) == 1:
            observations = []
        elif prev_line.__eq__(line) and len(observations) >= 30:
            print(observations)
            model.train(observations, 100, 0.00001)
            #print("trained")
            #print(line_num)
            print(str(model.get_transition_matrix()))
            
            observations = []
        prev_line = line
        line.replace
        line_num = line_num + 1
        
    finput.close()

def setup(inputfile, modelfile):
    
    #observation_set = initial_obs(inputfile)
    observation_set = [str(x) for x in xrange(-12,0)]
    for i in range(1,13):
        observation_set.append(str(i)) 
    observations = []
    finput = open(inputfile, 'r')

    for line in finput:
        line = line.replace("\n", "")
        observations.append(line)
        line.replace
    finput.close()
    hmm_cups = hmm_faster.HMM()
    hmm_cups.set_states([str(x) for x in xrange(0,13)])
    hmm_cups.set_observations(observation_set)
    hmm_cups.randomize_matrices(20)
    hmm_cups.train(observations, 30, 0.00001)
    print(hmm_cups.get_transition_matrix())
    #output = hmm_cups.viterbi(test_data)
    #print(output)
    hmm_cups.write_to_file(modelfile)
        
def main():
    setup("ALL.txt", "./ALLmodel.hmm")
    setup("CUPS_REDUCED.txt", "./CUPSmodel.hmm")
    setup("DEMONS.txt", "./DMNmodel.hmm")
    setup("DIAMONDS_REDUCED.txt", "./DIMmodel.hmm")
    setup("HABITS_REDUCED.txt", "./HABmodel.hmm")
    setup("HALLELUJAH.txt", "./HLJmodel.hmm")
    setup("I_KNEW_YOU_WERE_TROUBLE_REDUCED.txt", "./TRUBmodel.hmm")
    setup("JUST_GIVE_ME_A_REASON_REDUCED.txt", "./RSNmodel.hmm")
    setup("RAINBOW.txt", "./RANmodel.hmm")
    setup("ROYALS.txt", "./ROYmodel.hmm")
    setup("WAKE_ME_UP.txt", "./WAKmodel.hmm")



    
main()


