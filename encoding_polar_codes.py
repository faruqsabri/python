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
