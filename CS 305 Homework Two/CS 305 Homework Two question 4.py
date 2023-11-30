
# The threading module is imported to create and utilize threads
import threading

# The math module is imported to utilize built-in math functions.
import math

# The time module is imported to create time intervals for context switching.

import time

# This function calculates and prints the minimum, maximum, average, and standard deviation values
def calculations(list_items):
    # This allows the threads to execute concurrently via a time interval.
    time.sleep(1)

    # This assigns each subset element to a variable (to be used in later calculations).
    print(f'subset: {list_items}\n')
    first_num = list_items[0]
    second_num = list_items[1]
    third_num = list_items[2]

    # This allows the threads to execute concurrently via a time interval (again, for conceptual purposes).
    minimum = min(list_items)
    print(f'minimum value: {minimum}\n')

    # This allows the threads to execute concurrently via a time interval (again, for conceptual purposes).
    maximum = max(list_items)
    print(f'maximum value: {maximum}\n')

    # This function calculates the average of the list and prints it.
    average = sum(list_items) / len(list_items)
    print(f'average: {average}\n')

    # This squares the value of each subset element.
    elem1 = (first_num - average)
    square1 = pow(elem1, 2)
    elem2 = (second_num - average)
    square2 = pow(elem2, 2)
    elem3 = (third_num - average)
    square3 = pow(elem3, 2)

    # This calculates the sum of the subset elements.
    st_sum = square1 + square2 + square3

    # This calculates the value of the radicand in the standard deviation formula.
    radicand = st_sum / len(list_items)

    # This calculates the standard of deviation (completes formula).
    standard_dev = math.sqrt(radicand)
    print(f'standard deviation: {standard_dev}\n')

    # This creates a newline that improves readability in the output.
    print()

# This generates an empty list.
input_list = []

# This populates the list with 12 values inputed by the user.
while len(input_list) < 12:
    num = input('enter a number: ')
    input_list.append(int(num))

# This creates a newline that delineates between the input prompt and the thread output (improves readability).
print()

# This separates the list into 4 subsets.

sublist1 = input_list[0:len(input_list) // 4]
sublist2 = input_list[len(input_list) // 4: 2*len(input_list) // 4]
sublist3 = input_list[2*len(input_list) // 4: 3*len(input_list) // 4]
sublist4 = input_list[3*len(input_list) // 4: 4*len(input_list) // 4]



# This creates thread 1, which executes the calculations function.
thread1 = threading.Thread(target = calculations, args = (sublist1,))
# This creates thread 2, which executes the calculations function.
thread2 = threading.Thread(target = calculations, args = (sublist2,))
# This creates thread 3, which executes the calculations function.
thread3 = threading.Thread(target = calculations, args = (sublist3,))
# This creates thread 4, which executes the calculations function.
thread4 = threading.Thread(target = calculations, args = (sublist4,))


# This runs thread1.
thread1.start()
# This runs thread2.
thread2.start()
# This runs thread3.
thread3.start()
# This runs thread4.
thread4.start()

# This tells the main program to wait until thread1 terminates.
thread1.join()
# This tells the main program to wait until thread2 terminates.
thread2.join()
# This tells the main program to wait until thread3 terminates.
thread3.join()
# This tells the main program to wait until thread4 terminates.
thread4.join()

# This signifies the end of the program
print('done')
