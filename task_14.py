max_length = 0

for n in range(2,1000000):

    seq = [n]
    i = 0
    while seq[-1] != 1:
        if (seq[i]) % 2 == 0:
            seq.append(int((seq[i])/2))
        else:
            seq.append(int((3*(seq[i]))+1))
        i += 1

    if len(seq) > max_length:
        max_length = len(seq)
        max_seq = seq

print(max_seq)
print(max_length)
