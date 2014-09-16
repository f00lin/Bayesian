##example Bayesian calculations (from Ferdinand and Zuidema)


import random
from math import log
from math import exp



prior = [0.7, 0.2, 0.1]

hypotheses = [[0.6, 0.3, 0.1], [0.2, 0.6, 0.2], [0.1, 0.3, 0.6]]

data = [0, 1, 2]

data_length = 3



##creates a random data set from the three possible data types

def data_create(dat):
    d = []
    for i in range(data_length):
        d.append(random.choice(dat))
    return d

#print(data_create(data))



##returns a list of the probabilities of each data point under each hypothesis
## e. g. if data = [0, 2, 2]; hypotheses = [[0.6, 0.3, 0.1], [0.2, 0.6, 0.2], [0.1, 0.3, 0.6]]
##then the probability of the first data point '0' is [0.6, 0.2, 0.1], a list of this sort
##is produced for the other data points too.  In this case both are '2s', so list is
##[0.1, 0.2, 0.6]

##the overall output would thus look like: [[0.6, 0.2, 0.1], [0.1, 0.2, 0.6], [0.1, 0.2, 0.6]]

def prob_dat_points(dat, hyp):
    data = data_create(dat)
    print(data)
    prob_string = []
    for i in data:
        dat = []
        for index, object in enumerate(hyp):
            dat.append(round(hyp[index][i], 4))
        prob_string.append(dat)
    return prob_string

#print(prob_dat_points(data, hypotheses))




##takes the list of data point likelihoods from above function and calculates the likelihood 
##of each of the hypotheses given the data.   To continue the above example:
##the output of [[0.6, 0.2, 0.1], [0.1, 0.2, 0.6], [0.1, 0.2, 0.6]] is used to calculate the
##likelihood of hyp0 by adding the logs of each of the likelihoods in position 0
##i. e. log(0.6)+log(0.1)+log(0.1), this is repeated for each till an output of one list with
##the likelihoods of each hypothesis expressed as a log is produced

def prob_dat_given_hyp(dat, hyp):
    data_points = prob_dat_points(dat, hyp)
    pdgth = []
    for i in range(data_length):
        tot = 0
        for index, object in enumerate(data_points):
            tot += log(data_points[index][i])
        pdgth.append(tot)
    return pdgth

#print(prob_dat_given_hyp(data, hypotheses))




##returns the priors as logs

def prior_as_log(p):
    p_logs = []
    for i in p:
        l = log(i)
        p_logs.append(l)
    return p_logs

#print(prior_as_log(prior))





##normalizes the probabilities by making them sum to 1
#test = [0.0021, 0.0048, 0.0108]

def normalize(lst):
    norm = []
    tot = sum(lst)
    for i in lst:
        temp = ((i*100)/tot)/100
        norm.append(temp*1)
    return norm
        
#print(normalize(test))




##returns the set of posterior probabilities

def posterior_prob(dat, hyp, p):
    data_prob = prob_dat_given_hyp(dat, hyp)
    prior = prior_as_log(p)
    post_prob = []
    for i in range(data_length):
        post_prob.append(exp(data_prob[i]+prior[i]))
    return normalize(post_prob)
        
print(posterior_prob(data, hypotheses, prior))








        


    
   

