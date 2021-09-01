from matplotlib.colors import is_color_like
import numpy as np

#declaration of the parity-check matrix
H = np.array([[1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1]])

#setting the input and output of the LDPC
c = np.array([0, 0, 1, 0, 1, 1])
y = np.array([0, 1, 1, 0, 1, 1])

#initialization of bit flipping decoding
w_r = 2 #constraints for the number of ones in each row of the parity-check matrix
w_c = 3 #constraints for the number of ones in each column of the parity-check matrix
m = np.size(H,0) #the number of row in the parity-check matrix
N = np.size(H,1) #the number of column in the parity-check matrix
M = y[::].copy() #from the initialization, M = y
Mj = np.zeros((6), dtype=int) #matrix for the majority
s = np.zeros((4), dtype=int) #matrix for checking wether parity-check equations are satisfied.
E = np.zeros((m, N), dtype=int) #matrix for the result of check message
l_max = 150 #maximum iteration

#initializing value of B
B_j,B_i = np.where(H == 1) #B_j is the value for rows, B_i is the value for column of matrix B.
B = [[],[],[],[]] #defining matrix B as empty set.
for temp_index in range(B_j.size):
    B[B_j[temp_index]].append(B_i[temp_index]) #append the value from B_i into each row based on value of B_j

#Iteration count
l = 0
while l <= l_max:

#Step 1: Check messages
    for j in range (m):
        for i in range (N):
            for i_prime in B[j]: #for condition of algorithm, i_prime is element of B[j]
                if i != i_prime: #for condition i is not equal with i_prime
                    E[j][i] ^= M[i_prime] #calculation for line 11

#Step 2: Bit messages
    for i in range (N):
        Mj[i] = (E[:, i] == 1). sum() #this equation is used because in line 16 of algorithm, we check the majority of messages E[j][i] not majority of messages E[j][i_prime]
        if y[i] == 1 and Mj[i] < 2: #this condition means that if the i-th column of the received message = 1, and if sum of the first column < 2 (which means that there are 3 of zeros and 1 of ones), so the majority will be zeros and y[i] mod2 with 1
            M[i] = y[i] ^ 1
        elif y[i] == 0 and Mj[i] > 2: #for this condition if the sum > 2 means that there are 3 of ones and 1 of zeros. if the received message at the i-th column = 0 is not the same with the majority.
            M[i] = y[i] ^ 1

#Stopping criteria
    for j in range (m):
        for i_prime in B[j]:
            s[j] ^= M[i_prime]

    count = np.sum(s)

    if count == 0:
        print ("The codeword is: ", M)
        print ("Found at step: ", l)
        break
    elif l == l_max:
        print ("The codeword is failed to obtain since Maximum iteration has achieved.")
        break
    elif count != 0:
        l = l + 1
        continue