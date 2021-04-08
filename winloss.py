# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:40:17 2021

@author: Alex
"""
import pandas as pd

def jeopardy_win(C, D, P, Q, wager_amt_A, wager_amt_B):
#    expectationA = P * (C + wager_amt_A) + (1-P) * (C - wager_amt_A)
#    expectationB =  Q * (D + wager_amt_B) + (1-Q) * (D - wager_amt_B)
##    print(expectationA, expectationB)
#    if expectationA > expectationB:
#        return 1
#    if expectationA == expectationB:
#        return 0.5
#    if expectationA < expectationB:
#        return 0

    winprob = 0
    if (C + wager_amt_A) - (D + wager_amt_B) > 0:
        winprob += P*Q
    if (C + wager_amt_A) - (D - wager_amt_B) > 0:
        winprob += P * (1-Q)
    if (C - wager_amt_A) - (D + wager_amt_B) > 0:
        winprob += (1-P) * Q
    if (C - wager_amt_A) - (D - wager_amt_B) > 0:
        winprob += (1-P) * (1-Q)
    if (C + wager_amt_A) - (D + wager_amt_B) == 0:
        winprob += P*Q/2
    if (C + wager_amt_A) - (D - wager_amt_B) == 0:
        winprob += P * (1-Q)/2
    if (C - wager_amt_A) - (D + wager_amt_B) == 0:
        winprob += (1-P) * Q/2
    if (C - wager_amt_A) - (D - wager_amt_B) == 0:
        winprob += (1-P) * (1-Q)/2
    return winprob
print(jeopardy_win(12000,4000,0.6,0.6,0,4000))


def prob_space(C, D, P, Q):
    probspace = []
    rangelistA = []
    rangelistB = []
    for Abet in range(0,C+1,250):
        rangelistA.append(Abet)
    for Bbet in range(0,D+1,250):
        rangelistB.append(Bbet)
    for Abet in rangelistA:
        probs = []
        for Bbet in rangelistB:
            probs.append(jeopardy_win(C,D,P,Q,Abet,Bbet))
        probspace.append(probs)
    
    df = pd.DataFrame(probspace,rangelistA, rangelistB)
    return df
            
print(prob_space(500,500,.6,.4))
