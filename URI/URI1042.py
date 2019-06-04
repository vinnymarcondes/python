A, B, C =input().split(' ')
A = int(A)
B = int(B)
C = int(C)

if A < B and B < C:
 print (A)
 print (B)
 print (C)
elif B < A and A < C:
 print (B)
 print (A)
 print (C)
elif B < C and C < A:
 print (B)
 print (C)
 print (A)
elif C < B and B < A:
 print (C)
 print (B)
 print (A)
elif A< C and C < B:
 print (A)
 print (B)
 print (C)
else:
 print (C)
 print (A)
 print (B)

print ()

print (A)
print (B)
print (C)