#user_input = int(input("Enter the number: "))


for user_input in range(1,1001):
    result = 0
    length_of_the_number = len(str(user_input))
    for i in str(user_input):
        result = result + pow(int(i),length_of_the_number)
        

    if ( user_input == result):
        print (result, ", ")
