
# The threading module is imported to create and utilize threads
import threading

# The math module is imported to utilize built-in math functions.
import math

# The time module is imported to create time intervals for context switching.

import time

# This function prints the minimum value of the list.
def list_min(list_items):
    # This allows the threads to execute concurrently via a time interval.
    time.sleep(1)
    # Minimum calculation
    minimum = min(list_items)
    print(f'minimum value: {minimum}\n')

# This function prints the maximun value of the list.
def list_max(list_items):
    # This allows the threads to execute concurrently via a time interval.
    time.sleep(1)
    # Maxiimum calculation
    maximum = max(list_items)
    print(f'maximum value: {maximum}\n')

# This function calculates the average of the list and prints it.
def list_average(list_items):
    # This allows the threads to execute concurrently via a time interval
    time.sleep(1)
    # Average calculation
    average = sum(list_items) / len(list_items)
    print(f'average: {average}\n')

# This calculate the standard deviation of the list and prints it.
def list_standard_dev(list_items):
    # This allows the threads to execute concurrently via a time interval.
    time.sleep(1)
    index = 0
    index2 = 0
    original_avg = sum(list_items) / len(list_items)

    # This for-loop updates each element in the list with itself subtracted by the average.
    for item in list_items:
        list_items[index] = item - original_avg
        index = index + 1

    # This for-loop updates each element in the list with its value squared.
    for item in list_items:
        list_items[index2] = pow(item, 2)
        index2 = index2 + 1

    # This calculates the value of the radicand in the standard deviation formula.
    radicand = sum(list_items) / len(list_items)
    # This calculates the standard of deviation (completes formula).
    standard_dev = math.sqrt(radicand)

    print(f'standard of deviation: {standard_dev}\n')


# This generates an empty list.
input_list = []

# This populates the list with 12 values inputed by the user.
while len(input_list) < 12:
    num = input('enter a number: ')
    input_list.append(int(num))

# This prints the list.
print(f'list of values: {input_list}\n')

# This creates a newline that delineates between the input prompt and the thread output (improves readability).
print()

# This creates thread 1, which executes the list_max function.
thread1 = threading.Thread(target = list_max, args = (input_list,))
# This creates thread 2, which executes the list_min function.
thread2 = threading.Thread(target = list_min, args = (input_list,))
# This creates thread 3, which executes the list_average function.
thread3 = threading.Thread(target = list_average, args = (input_list,))
# This creates thread 4, which executes the list_standard_dev function.
thread4 = threading.Thread(target = list_standard_dev, args = (input_list,))



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