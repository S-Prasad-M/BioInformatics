import random

def mermer(seq, k):
    L = []
    for i in range(len(seq)-k-1):
        L.append(seq[i:i+k])
    return sorted(L)
 
def reconstruct(L):
    temp_L = [i for i in L]
    seq=temp_L[random.randint(0,len(temp_L)-1)]
    print(seq)
    temp_L.remove(seq)
    for i in range(20):
        pre = [k[:2] for k in temp_L]
        suf = [k[1:] for k in temp_L]
        print(temp_L)
        ch = random.randint(0,1)
        if (ch == 0):
            if seq[-2:] in pre:
                mer = pre.index(seq[-2:])
                seq =seq + temp_L[mer][2]
                temp_L.pop(mer)
        elif (ch == 1):
            if seq[:2] in suf:
                mer = suf.index(seq[:2])
                seq = temp_L[mer][0] + seq
                temp_L.pop(mer)
        print(seq, end = "\t")

k = int(input("Ënter k:"))
k_mers = mermer("ATAGGCTACATGCG",k)
print(k_mers)
# print(sorted(k_mers))
reconstruct(k_mers)
