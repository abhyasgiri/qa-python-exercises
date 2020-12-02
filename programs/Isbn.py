

ISBN = (input("What is the ISBN number? : "))

d_1 = int(ISBN[0]) 
d_2 = int(ISBN[1])*3
d_3 = int(ISBN[2])
d_4 = int(ISBN[3])*3
d_5 = int(ISBN[4])
d_6 = int(ISBN[5])*3
d_7 = int(ISBN[6])
d_8 = int(ISBN[7])*3
d_9 = int(ISBN[8])
d_10 = int(ISBN[9])*3 
d_11 = int(ISBN[10])
d_12 = int(ISBN[11])*3


last_digit = 10 - ((d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7 + d_8 + d_9 + d_10 + d_11 + d_12) % 10)

print(last_digit)



