# # # 1  

# # # 2 2  

# # # 3 3 3  

# # # 4 4 4 4  

# # # 5 5 5 5 5

# # for i in range(1,6):
# #     for j in range(i):
# #         print (i,end=" ")
# #     print("\n")

# # 1 1 1 1 1 

# # 2 2 2 2 

# # 3 3 3 

# # 4 4 

# # 5

# for i in range(1,6):
#     for j in range(i,6):
#         print(i,end=" ")
#     print()


# 1 

# 1 2 

# 1 2 3 

# 1 2 3 4 

# 1 2 3 4 5

# for i in range(1,6):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()

# 5 5 5 5 5 

# 4 4 4 4 

# 3 3 3 

# 2 2 

# 1

# for i in range(1,6):
#     for j in range(i,6):
#         print(6-i, end=" ")
#     print()
    
# 5 5 5 5 5 

# 5 5 5 5 

# 5 5 5 

# 5 5 

# 5

# for i in range(1,6):
#     for j in range(i,6):
#         print(5,end=" ")
#     print("\n")

# 1 

# 2 1 

# 3 2 1 

# 4 3 2 1 

# 5 4 3 2 1

# for i in range(1,6):
#     for j in range(i):
#         print(i-j,end=" ")
#     print("\n")

# 0 1 2 3 4 5 

# 0 1 2 3 4 

# 0 1 2 3 

# 0 1 2 

# 0 1

# for i in range(0,5):
#     for j in range(0,6-i):
#         print(j,end=" ")
#     print()

# 1 

# 2 3 4 

# 5 6 7 8 9
# a=1
# b=2
# for i in range(3):
#     for j in range(1,b):
#         print(a,end=" ")
#         a+=1
#     print()
#     b+=2

# 1

# 3 2

# 6 5 4

# 10 9 8 7
# a=1
# for i in range (1,5):
#     for j in range(0,i):
#         print(a-j,end=" ")      
#     print()
#     a+=i+1

# 1 

# 1 2 1 

# 1 2 3 2 1 

# 1 2 3 4 3 2 1 

# 1 2 3 4 5 4 3 2 1
a=1
for i in range (1,6):
    for j in range(1,i+i):
        if j<=i:
            print(j,end=" ")
            
        else:
            print(j-i,end=" ")
            
            
    print()
    
# 5 4 3 2 1 1 2 3 4 5 

# 5 4 3 2 2 3 4 5 

# 5 4 3 3 4 5 

# 5 4 4 5 

# 5 5
ows = 6

for i in range(0, rows):

    for j in range(rows – 1, i, -1):

        print(j, ”, end=”)

    for l in range(i):

        print(‘ ‘, end=”)

    for k in range(i + 1, rows):

        print(k, ”, end=”)

    print(‘\n’)
# 10 

# 10 8 

# 10 8 6 

# 10 8 6 4 

# 10 8 6 4 2

rows = 5

LastEvenNumber = 2 * rows

evenNumber = LastEvenNumber

for i in range(1, rows+1):

    evenNumber = LastEvenNumber

    for j in range(i):

        print(evenNumber, end=’ ‘)

        evenNumber -= 2

    print(“\r”)
# 0  

# 0 1  

# 0 2 4  

# 0 3 6 9  

# 0 4 8 12 16  

# 0 5 10 15 20 25  

# 0 6 12 18 24 30 36
rows = 7

for i in range(0, rows):

    for j in range(0, i + 1):

        print(i * j, end=’ ‘)

    print()
# 1 

# 3 3 

# 5 5 5 

# 7 7 7 7 

# 9 9 9 9 9
rows = 5

i = 1

while i <= rows:

    j = 1

    while j <= i:

        print((i * 2 – 1), end=” “)

        j = j + 1

    i = i + 1

    print()

