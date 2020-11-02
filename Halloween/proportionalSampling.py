# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 02:32:21 2020
Proportionate sampling is a sampling strategy (a method for gathering participants for a study) used when the population is composed of several subgroups that are vastly different in number. 
The number of participants from each subgroup is determined by their number relative to the entire population.

Ref: https://towardsdatascience.com/step-by-step-guide-proportional-sampling-for-data-science-with-python-8b2871159ae6

 normalized sum: One of the most common uses of this technique is to turn event counts into probabilities. By definition, probabilities have in [0,1] (i.e., greater than or equal to zero and less than or equal to one). 
 Suppose you have an urn with 10 balls in it, seven of which are red and three of which are blue. You could normalize these counts so that they sum to unity and restate this as the probability that a randomly chosen ball is red, P(ball=red)=77+3=710=0.7 and P(ball=blue)=33+7=310=0.3.

@author: 19240179
"""

import random
A = [1,2,3,4,5,6]
c = {}
d = {}
b = []


def pick_a_number_from_list(A):
# total sum of all elements
    sum = 0
    sum1 = 0
    for i in range(len(A)):
        sum += A[i]
    #normalized sum
    for j in range(len(A)):
        c["d_dash{}".format(j)]=A[j]/sum
    #Cumulative sum A0~ = A0' ; A1~ = A0~+ A1'; 
    for k in range(len(A)):
        sum1 += c["d_dash{}".format(k)]
        d["d_cum{}".format(k)] = sum1
    r=random.uniform(0.0,1.0)
    for l in range(len(A)):
        if r <= d["d_cum{}".format(l)]:
            return(A[l])
       
def sampling_based_on_magnitued():
    for i in range(1,100):
        number = pick_a_number_from_list(A)
        b.append(number)
        
sampling_based_on_magnitued()

c=(sorted(A, reverse=True))
print(c)

for x in c:
    print("count of {} is".format(x),b.count(x))
   
    