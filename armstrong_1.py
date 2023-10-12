def isArmstrong(user_input, result):
    length_of_the_number = len(str(user_input))
    for eachDigit in str(user_input):
        #print ("eachDigit: ",eachDigit, "length: ", length_of_the_number)
        result = result + pow(int(eachDigit),length_of_the_number)
    return (result==user_input)

def generate_Armstrong_Numbers(start, end):
    for input_num in range(start, end):
        result=0
        if (isArmstrong(input_num, result)):
            print (input_num, " is Armstrong")
        #else:
         #   print(user_input, "is not Armstrong")
