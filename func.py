from math import pi

gamma = (8-pi)/8

def iterFibo(n):
    prev_prev = 0
    prev = 0
    act = 1
    seq = [1]
    for i in range(n-1):
        prev_prev= prev
        prev = act
        act = prev_prev + prev 
        seq.append(act)
    return seq   

def underArea(a):
    return (pi*(a**2))/8 

def aboveArea(a):
    return (a**2)*gamma

def underArea_tillNow(prev,a):
    return prev+underArea(a)

def aboveArea_tillNow(prev,a):
    return prev+aboveArea(a)

def totalUnderArea(seq):
    area = underArea(1)
    for i in range (1,len(seq)):
        area = underArea_tillNow(area,seq[i])
    return area

def totalAboveArea(seq):
    area = aboveArea(1)
    for i in range(1, len(seq)):
        area = aboveArea_tillNow(area,seq[i])
    return area

def totalArea(seq):
    return totalUnderArea(seq)+totalAboveArea(seq)

def totalUnderArea_sequence(seq):
    sequence = []
    for i in range(len(seq)):
        sequence.append(totalUnderArea(seq[0:i+1]))
    return sequence

def totalAboveArea_sequence(seq):
    sequence = []
    for i in range(len(seq)):
        sequence.append(totalAboveArea(seq[0:i+1]))
    return sequence

def totalArea_sequence(seq):
    sequence = []
    for i in range(len(seq)):
        sequence.append(totalArea(seq[0:i+1]))
    return sequence