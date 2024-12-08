n = 14

seq = [n]

i = 0
while seq[-1] != 1:
    if (seq[i]) % 2 == 0:
        seq.append(int((seq[i])/2))
    else:
        seq.append(int((3*(seq[i]))+1))
    i += 1

print(seq)