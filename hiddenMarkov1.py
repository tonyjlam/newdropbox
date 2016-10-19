from sys import argv
from numpy import zeros, argmax

# viterbi will return the most likely hiden state sequence. 

def viterbi(initial, transition, emission, observed) :
    
    # infer hidden states
    
    #list in alphabetical order
    states = (initial.keys())

    #hard coded error
    #states = ['F','B']

    # initialize matrices
     
    score = zeros([len(states), len(observed)])
    trace = zeros([len(states), len(observed)], dtype=int)
    
    # forward pass
    for i, obs in enumerate (observed) :
        for j, st in enumerate (states) :
            ### Insert your code here
            ### Goal : implement forward pass of Viterbi algorithm
            ### Fill the score and trace matrices

            #if on the first state then do following
	    if i == 0 :
		#double dictionary, look up outter dictionary and store in hold
		hold = emission[st]
                ### Fill the first column here
		#fills score matrix 
                score[j,i] = (initial[st]) * hold[obs]
				
                trace[j,i] = 0

 	
            else :
                ### Fill the rest of the columns here
		#alot of dictionary stores.
		hold1 = transition[states[0]]
		hold2 = transition[states[1]]
		hold3 = transition[states[2]]
		hold4 = emission[states[j]]

		#find max if coming from first or second state.
		score[j,i] = max([(score[0,i-1] * float(hold1[states[j]]) * hold4[obs]), 
				 (score[1,i-1] * hold2[states[j]] * hold4[obs]), 
				 (score[2,i-1] * hold3[states[j]] * hold4[obs])])
		#fill trace matrix from first or second state

		trace[j,i] = argmax([(score[0,i-1] * hold1[states[j]]), 
				     (score[1,i-1] * hold2[states[j]]),
				     (score[2,i-1] * hold2[states[j]])])

    print 'score mtx'		
    print score
    print 'trace mtx'
    print trace

    # trace back
    z = argmax(score[:,-1])
    hidden = states[z]

    for i in range(1,len(observed))[::-1] :
        z = trace[z,i]
        hidden += states[z]

    # return REVERSED traceback sequence
    return hidden[::-1]

if __name__ == '__main__' :

    # initial probabilities of (F)air and (B)iased coins
    initial = {'F':0.4, 'B':0.4, 'D':0.2}

    # transition probabilities btw (F)air and (B)iased coins
    transition = {'F':{'F':0.2, 'B':0.3, 'D':0.5}, 'B':{'F':0.3, 'B':0.2, 'D':'0.5'}, 'D':{'F':0.5, 'B':0.5, 'D':0}}

    # emmision probabilites from (F)air and (B)iased coins
    emission = {'F':{'H':0.5, 'T':0.5}, 'B':{'H':0.2, 'T':0.8}, 'D':{'H':0.8, 'T':0.2}}

    # observed sequence is the only input to the program
    sequence = argv[1]

    print viterbi (initial, transition, emission, sequence)
  

