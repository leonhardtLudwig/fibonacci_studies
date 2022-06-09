import csv
import sys

from numpy import NaN
sys.stdout = open('report.txt', 'w')

from func import aboveArea, iterFibo, totalAboveArea, totalAboveArea_sequence, totalArea, totalArea_sequence, totalUnderArea, totalUnderArea_sequence, underArea
n = 725
seq = iterFibo(n)

underArea_seq = totalUnderArea_sequence(seq)
aboveArea_seq = totalAboveArea_sequence(seq)
totalArea_seq = totalArea_sequence(seq)

ratio_underAbove = []
ratio_aboveUnder = []
ratio_totalUnder = []
ratio_totalAbove = []
ratio_underTotal = []
ratio_aboveTotal = []


#previous
ratio_prevUnderActUnder = []
ratio_actUnderPrevUnder = []
ratio_prevAboveActAbove = []
ratio_actAbovePrevAbove = []
ratio_prevTotalActTotal = []
ratio_actTotalPrevTotal = []
ratio_prevUnderActAbove = []
ratio_actUnderPrevAbove = []
ratio_prevAboveActUnder = []
ratio_actAbovePrevUnder = []
ratio_prevTotalActUnder = []
ratio_actTotalPrevUnder = []
ratio_prevTotalActAbove = []
ratio_actTotalPrevAbove = []
ratio_prevUnderActTotal = []
ratio_actUnderPrevTotal = []
ratio_prevAboveActTotal = []
ratio_actAbovePrevTotal = []

#next
ratio_nextUnderActUnder = []
ratio_actUnderNextUnder = []
ratio_nextAboveActAbove = []
ratio_actAboveNextAbove = []
ratio_nextTotalActTotal = []
ratio_actTotalNextTotal = []
ratio_nextUnderActAbove = []
ratio_actUnderNextAbove = []
ratio_nextAboveActUnder = []
ratio_actAboveNextUnder = []
ratio_nextTotalActUnder = []
ratio_actTotalNextUnder = []
ratio_nextTotalActAbove = []
ratio_actTotalNextAbove = []
ratio_nextUnderActTotal = []
ratio_actUnderNextTotal = []
ratio_nextAboveActTotal = []
ratio_actAboveNextTotal = []

for i in range(len(seq)):
    ratio_underAbove.append(underArea_seq[i]/aboveArea_seq[i])
    ratio_aboveUnder.append(aboveArea_seq[i]/underArea_seq[i])
    ratio_totalUnder.append(totalArea_seq[i]/underArea_seq[i])
    ratio_totalAbove.append(totalArea_seq[i]/aboveArea_seq[i])
    ratio_underTotal.append(underArea_seq[i]/totalArea_seq[i])
    ratio_aboveTotal.append(aboveArea_seq[i]/totalArea_seq[i])
    
    if(i>0):
        
        ratio_prevUnderActUnder.append(underArea_seq[i-1]/underArea_seq[i])
        ratio_actUnderPrevUnder.append(underArea_seq[i]/underArea_seq[i-1])
        ratio_prevAboveActAbove.append(aboveArea_seq[i-1]/aboveArea_seq[i])
        ratio_actAbovePrevAbove.append(aboveArea_seq[i]/aboveArea_seq[i-1])
        ratio_prevTotalActTotal.append(totalArea_seq[i-1]/totalArea_seq[i])
        ratio_actTotalPrevTotal.append(totalArea_seq[i]/totalArea_seq[i-1])
        ratio_prevUnderActAbove.append(underArea_seq[i-1]/aboveArea_seq[i])
        ratio_actUnderPrevAbove.append(underArea_seq[i]/aboveArea_seq[i-1])
        ratio_prevAboveActUnder.append(aboveArea_seq[i-1]/underArea_seq[i])
        ratio_actAbovePrevUnder.append(aboveArea_seq[i]/underArea_seq[i-1]) 
        ratio_prevTotalActUnder.append(totalArea_seq[i-1]/underArea_seq[i])
        ratio_actTotalPrevUnder.append(totalArea_seq[i]/underArea_seq[i-1])
        ratio_prevTotalActAbove.append(totalArea_seq[i-1]/aboveArea_seq[i])
        ratio_actTotalPrevAbove.append(totalArea_seq[i]/aboveArea_seq[i-1])
        ratio_prevUnderActTotal.append(underArea_seq[i-1]/totalArea_seq[i]) 
        ratio_actUnderPrevTotal.append(underArea_seq[i]/totalArea_seq[i-1])
        ratio_prevAboveActTotal.append(aboveArea_seq[i-1]/totalArea_seq[i])
        ratio_actAbovePrevTotal.append(aboveArea_seq[i]/totalArea_seq[i-1])
        
    if(i<len(seq)-1):
        ratio_nextUnderActUnder.append(underArea_seq[i+1]/underArea_seq[i])
        ratio_actUnderNextUnder.append(underArea_seq[i]/underArea_seq[i+1])
        ratio_nextAboveActAbove.append(aboveArea_seq[i+1]/aboveArea_seq[i])
        ratio_actAboveNextAbove.append(aboveArea_seq[i]/aboveArea_seq[i+1])
        ratio_nextTotalActTotal.append(totalArea_seq[i+1]/totalArea_seq[i])
        ratio_actTotalNextTotal.append(totalArea_seq[i]/totalArea_seq[i+1])
        ratio_nextUnderActAbove.append(underArea_seq[i+1]/aboveArea_seq[i])
        ratio_actUnderNextAbove.append(underArea_seq[i]/aboveArea_seq[i+1])
        ratio_nextAboveActUnder.append(aboveArea_seq[i+1]/underArea_seq[i])
        ratio_actAboveNextUnder.append(aboveArea_seq[i]/underArea_seq[i+1]) 
        ratio_nextTotalActUnder.append(totalArea_seq[i+1]/underArea_seq[i])
        ratio_actTotalNextUnder.append(totalArea_seq[i]/underArea_seq[i+1])
        ratio_nextTotalActAbove.append(totalArea_seq[i+1]/aboveArea_seq[i])
        ratio_actTotalNextAbove.append(totalArea_seq[i]/aboveArea_seq[i+1])
        ratio_nextUnderActTotal.append(underArea_seq[i+1]/totalArea_seq[i]) 
        ratio_actUnderNextTotal.append(underArea_seq[i]/totalArea_seq[i+1])
        ratio_nextAboveActTotal.append(aboveArea_seq[i+1]/totalArea_seq[i])
        ratio_actAboveNextTotal.append(aboveArea_seq[i]/totalArea_seq[i+1])

        

for i in range(len(seq)):
    print("*****************************")
    print("Fibonacci number: {}".format(seq[i]))
    print("Area under the spiral: {:.3f}".format(underArea_seq[i]))
    print("Area above the spiral: {:.3f}".format(aboveArea_seq[i]))
    print("Total area: {:.3f}".format(totalArea_seq[i]))
    print()
    print("--------RATIOS---------")
    print()
    print("Ratio under/above: {:.3f}".format(ratio_underAbove[i]))
    print("Ratio above/under: {:.3f}".format(ratio_aboveUnder[i]))
    print("Ratio total/under: {:.3f}".format(ratio_totalUnder[i]))
    print("Ratio total/above: {:.3f}".format(ratio_totalAbove[i]))
    print("Ratio under/total: {:.3f}".format(ratio_underTotal[i]))
    print("Ratio above/total: {:.3f}".format(ratio_aboveTotal[i]))
    print()
    if(i>0):
        print("++++ WITH PREV ++++")
        print()
        print("Ratio prev_under/act_under: {:.3f}".format(ratio_prevUnderActUnder[i-1]))
        print("Ratio act_under/prev_under: {:.3f}".format(ratio_actUnderPrevUnder[i-1]))
        print("Ratio prev_above/act_above: {:.3f}".format(ratio_prevAboveActAbove[i-1]))
        print("Ratio act_above/prev_above: {:.3f}".format(ratio_actAbovePrevAbove[i-1]))
        print("Ratio prev_total/act_total: {:.3f}".format(ratio_prevTotalActTotal[i-1]))
        print("Ratio act_total/prev_total: {:.3f}".format(ratio_actTotalPrevTotal[i-1]))
        print("Ratio prev_under/act_above: {:.3f}".format(ratio_prevUnderActAbove[i-1]))
        print("Ratio act_under/prev_above: {:.3f}".format(ratio_actUnderPrevAbove[i-1]))
        print("Ratio prev_above/act_under: {:.3f}".format(ratio_prevAboveActUnder[i-1]))
        print("Ratio act_above/prev_under: {:.3f}".format(ratio_actAbovePrevUnder[i-1]))
        print("Ratio prev_total/act_under: {:.3f}".format(ratio_prevTotalActUnder[i-1]))
        print("Ratio act_total/prev_under: {:.3f}".format(ratio_actTotalPrevUnder[i-1]))
        print("Ratio prev_total/act_above: {:.3f}".format(ratio_prevTotalActAbove[i-1]))
        print("Ratio act_total/prev_above: {:.3f}".format(ratio_actTotalPrevAbove[i-1]))
        print("Ratio prev_under/act_total: {:.3f}".format(ratio_prevUnderActTotal[i-1]))
        print("Ratio act_under/prev_total: {:.3f}".format(ratio_actUnderPrevTotal[i-1]))
        print("Ratio prev_above/act_total: {:.3f}".format(ratio_prevAboveActTotal[i-1]))
        print("Ratio act_above/prev_total: {:.3f}".format(ratio_actAbovePrevTotal[i-1]))
        print()
    if(i<len(seq)-1):
        print("++++ WITH NEXT ++++")
        print()
        print("Ratio next_under/act_under: {:.3f}".format(ratio_nextUnderActUnder[i]))
        print("Ratio act_under/next_under: {:.3f}".format(ratio_actUnderNextUnder[i]))
        print("Ratio next_above/act_above: {:.3f}".format(ratio_nextAboveActAbove[i]))
        print("Ratio act_above/next_above: {:.3f}".format(ratio_actAboveNextAbove[i]))
        print("Ratio next_total/act_total: {:.3f}".format(ratio_nextTotalActTotal[i]))
        print("Ratio act_total/next_total: {:.3f}".format(ratio_actTotalNextTotal[i]))
        print("Ratio next_under/act_above: {:.3f}".format(ratio_nextUnderActAbove[i]))
        print("Ratio act_under/next_above: {:.3f}".format(ratio_actUnderNextAbove[i]))
        print("Ratio next_above/act_under: {:.3f}".format(ratio_nextAboveActUnder[i]))
        print("Ratio act_above/next_under: {:.3f}".format(ratio_actAboveNextUnder[i]))
        print("Ratio next_total/act_under: {:.3f}".format(ratio_nextTotalActUnder[i]))
        print("Ratio act_total/next_under: {:.3f}".format(ratio_actTotalNextUnder[i]))
        print("Ratio next_total/act_above: {:.3f}".format(ratio_nextTotalActAbove[i]))
        print("Ratio act_total/next_above: {:.3f}".format(ratio_actTotalNextAbove[i]))
        print("Ratio next_under/act_total: {:.3f}".format(ratio_nextUnderActTotal[i]))
        print("Ratio act_under/next_total: {:.3f}".format(ratio_actUnderNextTotal[i]))
        print("Ratio next_above/act_total: {:.3f}".format(ratio_nextAboveActTotal[i]))
        print("Ratio act_above/next_total: {:.3f}".format(ratio_actAboveNextTotal[i]))
        print()
    print("*****************************")
    print()
    

header = ['sequenceNumber','underArea', 'aboveArea', 'totalArea',
          'ratio_underAbove','ratio_aboveUnder','ratio_totalUnder','ratio_totalAbove','ratio_underTotal','ratio_aboveTotal',
          'ratio_prevUnderActUnder','ratio_actUnderPrevUnder','ratio_prevAboveActAbove','ratio_actAbovePrevAbove','ratio_prevTotalActTotal','ratio_actTotalPrevTotal','ratio_prevUnderActAbove','ratio_actUnderPrevAbove','ratio_prevAboveActUnder','ratio_actAbovePrevUnder','ratio_prevTotalActUnder','ratio_actTotalPrevUnder','ratio_prevTotalActAbove','ratio_actTotalPrevAbove','ratio_prevUnderActTotal','ratio_actUnderPrevTotal','ratio_prevAboveActTotal','ratio_actAbovePrevTotal',
          'ratio_nextUnderActUnder','ratio_actUnderNextUnder','ratio_nextAboveActAbove','ratio_actAboveNextAbove','ratio_nextTotalActTotal','ratio_actTotalNextTotal','ratio_nextUnderActAbove','ratio_actUnderNextAbove','ratio_nextAboveActUnder','ratio_actAboveNextUnder','ratio_nextTotalActUnder','ratio_actTotalNextUnder','ratio_nextTotalActAbove','ratio_actTotalNextAbove','ratio_nextUnderActTotal','ratio_actUnderNextTotal','ratio_nextAboveActTotal','ratio_actAboveNextTotal']

with open('data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(seq)):
        if(i==0):
            writer.writerow([seq[i],underArea_seq[i],aboveArea_seq[i],totalArea_seq[i],
                            ratio_underAbove[i],ratio_aboveUnder[i],ratio_totalUnder[i],ratio_totalAbove[i],ratio_underTotal[i],ratio_aboveTotal[i],
                            NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,
                            ratio_nextUnderActUnder[i],ratio_actUnderNextUnder[i],ratio_nextAboveActAbove[i],ratio_actAboveNextAbove[i],ratio_nextTotalActTotal[i],ratio_actTotalNextTotal[i],ratio_nextUnderActAbove[i],ratio_actUnderNextAbove[i],ratio_nextAboveActUnder[i],ratio_actAboveNextUnder[i],ratio_nextTotalActUnder[i],ratio_actTotalNextUnder[i],ratio_nextTotalActAbove[i],ratio_actTotalNextAbove[i],ratio_nextUnderActTotal[i],ratio_actUnderNextTotal[i],ratio_nextAboveActTotal[i],ratio_actAboveNextTotal[i]])
        #writer.writerow([seq[i],underArea_seq[i],aboveArea_seq[i],totalArea_seq[i]])
        if(i==len(seq)-1):
            writer.writerow([seq[i],underArea_seq[i],aboveArea_seq[i],totalArea_seq[i],
                            ratio_underAbove[i],ratio_aboveUnder[i],ratio_totalUnder[i],ratio_totalAbove[i],ratio_underTotal[i],ratio_aboveTotal[i],
                            ratio_prevUnderActUnder[i-1],ratio_actUnderPrevUnder[i-1],ratio_prevAboveActAbove[i-1],ratio_actAbovePrevAbove[i-1],ratio_prevTotalActTotal[i-1],ratio_actTotalPrevTotal[i-1],ratio_prevUnderActAbove[i-1],ratio_actUnderPrevAbove[i-1],ratio_prevAboveActUnder[i-1],ratio_actAbovePrevUnder[i-1],ratio_prevTotalActUnder[i-1],ratio_actTotalPrevUnder[i-1],ratio_prevTotalActAbove[i-1],ratio_actTotalPrevAbove[i-1],ratio_prevUnderActTotal[i-1],ratio_actUnderPrevTotal[i-1],ratio_prevAboveActTotal[i-1],ratio_actAbovePrevTotal[i-1],
                            NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN])

        if(i!=0 and i!=len(seq)-1):
            writer.writerow([seq[i],underArea_seq[i],aboveArea_seq[i],totalArea_seq[i],
                                ratio_underAbove[i],ratio_aboveUnder[i],ratio_totalUnder[i],ratio_totalAbove[i],ratio_underTotal[i],ratio_aboveTotal[i],
                                ratio_prevUnderActUnder[i-1],ratio_actUnderPrevUnder[i-1],ratio_prevAboveActAbove[i-1],ratio_actAbovePrevAbove[i-1],ratio_prevTotalActTotal[i-1],ratio_actTotalPrevTotal[i-1],ratio_prevUnderActAbove[i-1],ratio_actUnderPrevAbove[i-1],ratio_prevAboveActUnder[i-1],ratio_actAbovePrevUnder[i-1],ratio_prevTotalActUnder[i-1],ratio_actTotalPrevUnder[i-1],ratio_prevTotalActAbove[i-1],ratio_actTotalPrevAbove[i-1],ratio_prevUnderActTotal[i-1],ratio_actUnderPrevTotal[i-1],ratio_prevAboveActTotal[i-1],ratio_actAbovePrevTotal[i-1],
                                ratio_nextUnderActUnder[i-1],ratio_actUnderNextUnder[i-1],ratio_nextAboveActAbove[i-1],ratio_actAboveNextAbove[i-1],ratio_nextTotalActTotal[i-1],ratio_actTotalNextTotal[i-1],ratio_nextUnderActAbove[i-1],ratio_actUnderNextAbove[i-1],ratio_nextAboveActUnder[i-1],ratio_actAboveNextUnder[i-1],ratio_nextTotalActUnder[i-1],ratio_actTotalNextUnder[i-1],ratio_nextTotalActAbove[i-1],ratio_actTotalNextAbove[i-1],ratio_nextUnderActTotal[i-1],ratio_actUnderNextTotal[i-1],ratio_nextAboveActTotal[i-1],ratio_actAboveNextTotal[i-1]])
    
sys.stdout.close()