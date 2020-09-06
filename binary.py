# COMPLETED


num = int(input('Input the number ')) 


def binary_decimal(num):
    if (num == 0):
        return 0 
    rem = num % 2
    num = int(num/2)
    
    binary_decimal(num)
    print(rem, end=" ")



binary_decimal(num)

# binary = []
# while(num>0):
#     rem = num % 2       # taking mode by 2 
#     binary.append(rem)  # saving the remainder in our list
#     num = int(num / 2)  # diving by 2, bcoz we hav calculated the first place binary digit

# for i in range(len(binary)-1, -1, -1):
#     print(binary[i], end="")

