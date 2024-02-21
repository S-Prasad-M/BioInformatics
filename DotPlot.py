seq1 = "ATGCA"
seq2 = "ATTGGCA"
n1 = len(seq1); n2 = len(seq2)
matrix = [[0]*n2 for _ in range(n1)]
for i in range(n1):
    for j in range(n2):
        if seq1[i]==seq2[j]:
            matrix[i][j] = 1
for i in matrix:
    print(i)

i = n1 - 1; j = n2 - 1
s1 = ""; s2 = ""
while i >= 0 or j >= 0:
    if i >= 0 and j >= 0 and seq1[i - 1] == seq2[j - 1]:
        s1 = seq1[i] + s1
        s2 = seq2[j] + s2
        i -= 1; j -= 1
    elif i >= 0 and (j == 0 or matrix[i][j] == matrix[i - 1][j] -2):
        s1 = '_' + s1
        s2 = seq2[j - 1] + s2
        i -= 1
    else:
        s1 = seq1[i - 1] + s1
        s2 = '_' + s2
        j -= 1
    

print("Sequence 1:", s1)
print("Sequence 2:", s2)

score = 0
for i in range(len(s1)):
    if s1[i] == s2[i]:
        score += 2
    elif s1[i]=="_" or s2[i]=="_":
        score -= 2
    elif s1[i] != s2[i]:
        score -= 1
    
print("Score:",score)
