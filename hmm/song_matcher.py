'''
Created on Nov 18, 2014

@author: Jacob
'''
from __future__ import division
import hmm_faster
import math


def obs_create(inputfile):
    finput = open(inputfile, 'r')
    observations = []
    
    for line in finput:
        line = line.replace("\n","")
        #if observations == []:
        observations.append(line)
        #elif line != observations[len(observations)-1]:
         #   observations.append(line)
            
        line.replace
    finput.close()
    return observations

def transitions(modelfile, inputarr):
    hmm_test = hmm_faster.HMM()
    hmm_test.read_from_file(modelfile)
    logprob = 0
    div = 0
    for i in range(1,len(inputarr)):
        logprob += hmm_test.get_transition(inputarr[i-1], inputarr[i])
        div = i
    return logprob/div

def viterbify(modelfile, inputarr):
    hmm_test = hmm_faster.HMM()
    hmm_test.read_from_file(modelfile)
    viter = hmm_test.viterbi(inputarr)
    return viter

def compare(viter, inputarr):
    int_input = inputarr
    comparator = 0
    for i in range(0,len(int_input)):
        int_input[i] = int(int_input[i])
        viter[i] = int(viter[i])
        comparator += abs(viter[i] - int_input[i])
        
    return comparator

def normalizer(viter):
    summer = 0
    for i in range(0, len(viter)):
        summer += abs(int(viter[i]))
    return summer
    
def equalizer(modelfile, input):
    logprob = transitions(modelfile, input)
    hmm_test = hmm_faster.HMM()
    hmm_test.read_from_file(modelfile)
    states = hmm_test.get_observations()
    normval = 0
    for i in range(0,len(states)-1):
        normval += hmm_test.get_transition(states[i], states[i+1])
    return abs(float(logprob))/(abs(float(normval))**0.9)
    
def emission(modelfile, input):
    #logprob = transitions(modelfile, input)
    hmm_test = hmm_faster.HMM()
    hmm_test.read_from_file(modelfile)
    #hmm_test.remove_state('0')
    #hmm_test.add_state('12')
    viter = hmm_test.viterbi(input)
    obval = 0
    #observations = hmm_test.get_observations()
    #for i in range(0, len(input)-1):
        #obval += -hmm_test.get_transition(input[i], input[i+1])
    div = 0
    eprob = 0
    for i in range(0,len(viter)):
        emission = hmm_test.get_emission(viter[i], input[i])
        eprob += emission
        div += 1
    return (eprob/div) #/ (abs(logprob)**1)

def lister(inputfile):
    input = obs_create(inputfile)

    ctrans = emission('./CUPSmodel.hmm',input)
    dtrans = emission('./DIMmodel.hmm',input)
    htrans = emission('./HABmodel.hmm',input)
    itrans = emission('./TRUBmodel.hmm',input)
    jtrans = emission('./RSNmodel.hmm',input)
    atrans = emission('./ALLmodel.hmm',input)
    dmtrans = emission('./DMNmodel.hmm',input)
    hjtrans = emission('./HLJmodel.hmm',input)
    rtrans = emission('./ROYmodel.hmm',input)
    wtrans = emission('./WAKmodel.hmm',input)
    ratrans = emission('./RANmodel.hmm', input)
    #cviter = viterbify('./CUPSmodel.hmm',input)
    #dviter = viterbify('./DIMmodel.hmm',input)
    #hviter = viterbify('./HABmodel.hmm',input)
    #iviter = viterbify('./TRUBmodel.hmm',input)
    #jviter = viterbify('./RSNmodel.hmm',input)

    
    
    transarray = [ctrans, dtrans, htrans, itrans, jtrans, atrans, dmtrans, hjtrans, rtrans, wtrans, ratrans]
    #viterray = [cviter, dviter, hviter, iviter, jviter]


    songlist = ["Cups", "Diamonds", "Habits", "I Knew You Were Trouble", "Just Give Me a Reason", "All Of Me", "Demons", "Hallelujah", "Royals", "Wake Me Up", "Somewhere Over the Rainbow"]
    ord_list = []
        #norm = float(compare(viterray[i], input)) * float(normalizer(viterray[i]))
        #compval = compval/(norm**2)
    temparray = []
    for i in range(0, len(transarray)):
        temparray.append(transarray[i])
    #print(transarray)
    #print(temparray)    
    while len(temparray) != 0:
        tempind = 0
        compval = -10
        for i in range(0, len(temparray)):
            if temparray[i] > compval:
                compval = temparray[i]
                indexed = transarray.index(compval)
                #print(indexed)
                tempind = i
        ord_list.append(songlist[indexed])
        #print(ord_list)
        temparray.pop(tempind)
        #print(compval)
        
    
    print(ord_list)
    

def main():            
    print("Training Data")
    print("All Of Me")
    lister("All.txt")
    print("Cups")
    lister("CUPS_REDUCED.txt")
    print("Demons")
    lister("DEMONS.txt")
    print("Diamonds")
    lister("DIAMONDS_REDUCED.txt")
    print("Habits")
    lister("HABITS_REDUCED.txt")
    print("Hallelujah")
    lister("HALLELUJAH.txt")
    print("I Knew You Were Trouble")
    lister("I_KNEW_YOU_WERE_TROUBLE_REDUCED.txt")
    print("Just Give Me A Reason")
    lister("JUST_GIVE_ME_A_REASON_REDUCED.txt")
    print("Somewhere Over The Rainbow")
    lister("RAINBOW.txt")
    print("Royals")
    lister("ROYALS.txt")
    print("Wake Me Up")
    lister("WAKE_ME_UP.txt")
    print("\n")
    print("Test Data")
    print("Cups 1")
    lister("CUPS_TEST_1.txt")
    print("Cups 2")
    lister("CUPS_TEST_2.txt")
    print("Diamonds 1")
    lister("DIAMONDS_TEST_1.txt")
    print("Diamonds 2")
    lister("DIAMONDS_TEST_2.txt")
    print("Diamonds 3")
    lister("DIAMONDS_TEST_3.txt")
    print("Habits 1")
    lister("HABITS_TEST_1.txt")
    print("Habits 2")
    lister("HABITS_TEST_2.txt")
    print("Habits 3")
    lister("HABITS_TEST_3.txt")
    print("I Knew You Were Trouble 1")
    lister("I_KNEW_YOU_WERE_TROUBLE_TEST_1.txt")
    print("I Knew You Were Trouble 2")
    lister("I_KNEW_YOU_WERE_TROUBLE_TEST_2.txt")
    print("I Knew You Were Trouble 3")
    lister("I_KNEW_YOU_WERE_TROUBLE_TEST_3.txt")
    print("Just Give Me A Reason 1")
    lister("JUST_GIVE_ME_A_REASON_TEST_1.txt")
    print("Just Give Me A Reason 2")
    lister("JUST_GIVE_ME_A_REASON_TEST_2.txt")
    print("Just Give Me A Reason 3")
    lister("JUST_GIVE_ME_A_REASON_TEST_3.txt")
    print("\n")
    lister('All of Me (John Legend cover) by GAC (Gamaliel Audrey Cantika)_vamp_mtg-melodia_melodia_melody.txt')
    lister('All Of Me (John Legend Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('All of me (John Legend) Acoustic Cover - Ruth Anna_vamp_mtg-melodia_melodia_melody.txt')
    lister('All Of Me (John Legend) Cover ft dianpalupi13_vamp_mtg-melodia_melodia_melody.txt')
    lister('All Of Me - John Legend (Acoustic Cover AlmaunNBA )_vamp_mtg-melodia_melodia_melody.txt')
    lister('All Of Me - John Legend (Cover by Daiyan Trisha)_vamp_mtg-melodia_melodia_melody.txt')
    lister('All Of Me - John Legend (cover) by Carmella Ravanilla_vamp_mtg-melodia_melodia_melody.txt')
    lister('All Of Me - John Legend (cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('All Of Me - John Legend Cover - Luciana Zogbi_vamp_mtg-melodia_melodia_melody.txt')
    lister('All of me - John Legend Cover By Jannina W_vamp_mtg-melodia_melodia_melody.txt')
    lister('All Of Me - John Legend Cover_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Avicii - Wake Me Up (Gareth Bush Cover)_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Bailey McConnell and Luciee Closier - Demons (Imagine Dragons Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons  Imagine Dragons Cover_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons (Imagine Dragons Cover) (Solo Demo Version)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons (Imagine Dragons Cover) by Kai and Kim_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons (Imagine Dragons Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons (Imagine Dragons) - Kim Rivera Cover_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons - Imagine Dragons (Cover by Cartoon)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons - Imagine Dragons (Cover by Christina Grimmie)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons - Imagine Dragons (Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons - Imagine Dragons Cover by Habiba Zahran (EL7AFLA)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons - Imagine Dragons Cover By Luciana Zogbi_vamp_mtg-melodia_melodia_melody.txt')
    lister('Demons Imagine Dragons - Cover by Musa Eyaz_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Habits (Stay High) (Tove Lo cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Habits (Tove Lo Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Habits - Tove Lo (cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('habits - tove lo cover_vamp_mtg-melodia_melodia_melody.txt')
    lister('Habits Tove Lo Cover by Casandra Ashe_vamp_mtg-melodia_melodia_melody.txt')
    lister('Habits Tove Lo- Cover by Mish and Fran_vamp_mtg-melodia_melodia_melody.txt')
    lister('Habits- Tove Lo (cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Habits- Tove Lo- Cover Karo Garay_vamp_mtg-melodia_melodia_melody.txt')
    lister('HABITS_FULL.txt')
    print('\n')
    lister('Hallelujah (Cover) - Krissha Viaje_vamp_mtg-melodia_melodia_melody.txt')
    lister('Hallelujah (Cover) Bamboo_vamp_mtg-melodia_melodia_melody.txt')
    lister('Hallelujah (cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Hallelujah (Jeff Buckley cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Hallelujah (One Take Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('hallelujah 2 cover by Shawn Mendes_vamp_mtg-melodia_melodia_melody.txt')
    lister('Hallelujah Cover - Amanda Rowe_vamp_mtg-melodia_melodia_melody.txt')
    lister('Hallelujah Cover by Barrio_vamp_mtg-melodia_melodia_melody.txt')
    lister('Hallelujah Cover-Totty_vamp_mtg-melodia_melodia_melody.txt')
    lister('Hallelujah Cover_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Ibnu Feat Enos - Just Give Me A Reason (Pink Cover)_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Il Divo - Hallelujah (Cover by Alejandro P)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Imogen Heap - Hallelujah (cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Jeff Buckley - Hallelujah - Cover_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Judy Garland-Somewhere Over The Rainbow Cover_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Just Give Me A Reason (Pink Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Just Give Me A Reason (Pink ft Nate Ruess) Cover Ruth Anna_vamp_mtg-melodia_melodia_melody.txt')
    lister('Just Give Me A Reason - Pink ( AlmaunNBA Acoustic Cover )_vamp_mtg-melodia_melodia_melody.txt')
    lister('Just Give Me A Reason - Pink cover - Unplugged - Acoustic guitar_vamp_mtg-melodia_melodia_melody.txt')
    lister('Just Give Me a Reason - Pink Cover_vamp_mtg-melodia_melodia_melody.txt')
    lister('Just Give Me A Reason-Pink (cover by) Lexi Shea_vamp_mtg-melodia_melodia_melody.txt')
    lister('Just Give Me A Reason-Pink (cover w Ardie Manrique)_vamp_mtg-melodia_melodia_melody.txt')
    lister('LUNAFLY - Just Give Me A Reason (Pink Cover)_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Md - Hallelujah (Cover Acoustic Live)_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Michael Maloney - Habits (Tove Lo Cover)_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Pixie Lott - Royals (Lorde Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals ( Lorde )_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals (Lorde Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals (Lorde) Acoustic Cover - Ruth Anna_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals (Lorde) Cover_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals - Lorde ( Cover ) Cajon Aditya Pradana_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals - Lorde ( cover ) feat Frangky Mutji_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals - Lorde ( Cover )_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals - Lorde (Cover By Maria Zarate  Maria Camila Posada)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals - Lorde (cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals - Lorde Cover by Jannina W_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals - Lorde Cover_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals - Lorde_vamp_mtg-melodia_melodia_melody.txt')
    lister('Royals-Lorde (COVER) by VictoriaMonet__vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Somewhere Over The Rainbow (Cover - In the style of Katharine McPhee)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Somewhere Over The Rainbow (cover Ft Jonathan Gaus)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Somewhere Over The Rainbow (cover)-Roseanna_vamp_mtg-melodia_melodia_melody.txt')
    lister('Somewhere Over The Rainbow (Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Somewhere Over The Rainbow - Cover_vamp_mtg-melodia_melodia_melody.txt')
    lister('Somewhere Over The Rainbow cover by Beyazit Karabulut_vamp_mtg-melodia_melodia_melody.txt')
    lister('Somewhere Over The Rainbow Cover by Janel Gibson_vamp_mtg-melodia_melodia_melody.txt')
    lister('Somewhere Over The Rainbow Cover_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Tove Lo - Habits (Stay High) Cover by Brandon Skeie_vamp_mtg-melodia_melodia_melody.txt')
    lister('Tove Lo - Stay High (Habits Remix) Guitar Cover_vamp_mtg-melodia_melodia_melody.txt')
    print('\n')
    lister('Wake Me Up (Avicii Cover) FREE DOWNLOAD_vamp_mtg-melodia_melodia_melody.txt')
    lister('Wake Me Up (Avicii Cover) TEASER_vamp_mtg-melodia_melodia_melody.txt')
    lister('Wake Me Up (AVICII Cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('wake me up - avicii ( cover)_vamp_mtg-melodia_melodia_melody.txt')
    lister('Wake Me Up -Avicii (cover by Bea Miller )_vamp_mtg-melodia_melodia_melody.txt')
    lister('Wake Me Up -avicii (cover) Chorus_vamp_mtg-melodia_melodia_melody.txt')
    lister('Wake Me Up Avicii Cover by ULRIKA_vamp_mtg-melodia_melodia_melody.txt')
    lister('Wake Me Up Avicii Cover by Vince Boyer_vamp_mtg-melodia_melodia_melody.txt')
    lister('Wake me upAvicii cover by Laurens and Olivier_vamp_mtg-melodia_melodia_melody.txt')

    
    
    
    
    
    
    
    
    
    


main()
import fileinput
import os
import glob 
#print(os.listdir('C:\\Users\\Jacob\\Downloads\\txtfiles\\txtfiles\\Test'))
#input = fileinput.input(glob.glob('C:\\Users\\Jacob\\Downloads\\txtfiles\\txtfiles\\Test\\*.txt'))
#for line in input:
    #print(line)


