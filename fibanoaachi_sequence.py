from itertools import count


def fibonacci(a,b,max_count, counter):
    if counter >= max_count:
        return
    fib = a+b
    counter+=1
    a=b
    b=fib
    fibonacci_list.append(fib)
    fibonacci(a,b,max_count, counter)
    


fibonacci_list = []
first_num = 0
second_num = 1 
fibonacci_list.append(first_num)
fibonacci_list.append(second_num)

fibonacci(first_num,second_num,200,2)
print(fibonacci_list)