import numpy as np

#main reliability sequence (32 Bit)
reliability_sequence = np.array ([0, 1, 2, 4, 8, 16, 3, 5, 9, 6, 17, 10, 18, 12, 20, 24, 7, 11, 19, 13, 14, 21, 26, 25, 22, 28, 15, 23, 27, 29, 30, 31])

#create length of the codeword, kronecker multiplier, and message length
#codeword_length = int(input("Please enter the length of the codeword: ")) #if you wanted to input the codeword length manually
codeword_length = 15
kronecker_multiplier = np.log2(codeword_length + 1)
message_length = 8

#create reliability sequence for N codeword length
reliability_sequence_1 = np.delete(reliability_sequence, np.where(reliability_sequence > codeword_length))

#create the message in randomized manner
message = np.random.randint(2, size=message_length)

#insert message into non-frozen position based on reliability sequence for N codeword length
for index, value in zip(reliability_sequence_1[8:], message):
    codeword[index] = value #credit to deanhystad of python-forum.io
    
"""#this script has same result as previous, I am writing this one for respect the answer of my fellow forum member.
x = len(reliability_sequence_1)-len(message)
for n, i in enumerate(reliability_sequence_1[x:]):
    if message[n]: codeword[i] = message[n] #credit to naughtyCat of python-forum.io"""

"""#this script also has same result in codeword and I got it from my senior Wei Lantian in Kamabe Laboratory. ありがとうございます, Wei さん.
message_list = list(message)
non_frozen = (reliability_sequence_1 + 1)[(codeword_length + 1)-message_length:]
for i in non_frozen:
    codeword[i - 1] = message_list.pop(0)"""

#Create generator matrix
generator_matrix = np.array([[1, 0], [1, 1]])
generator_matrix_multiplier = np.array([[1, 0], [1, 1]])
minimum_kronecker = 2

#Calculate the generator matrix based on the kronecker multiplier
while minimum_kronecker <= kronecker_multiplier:
    generator_matrix = np.kron(generator_matrix, generator_matrix_multiplier)
    minimum_kronecker = minimum_kronecker + 1

#Generate polar codes from codeword and generator matrix
polar_codes = np.mod(np.matmul(codeword, generator_matrix), 2) #From Arikan's paper about polar code, it should be XOR operation, and here I am using a mod of 2 because it has similarity with XOR which is if the number of zeros or ones is even, the result is 0. And in this mod 2, if the number is even, the result will be 0, and vice versa.

print (polar_codes)
