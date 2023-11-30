#CS 305 producer consumer bounded buffer
import threading
import time
n = 20
empty = threading.Semaphore(n)
full = threading.Semaphore(0) #0, going to wait for a process to increment it
mutex = threading.Semaphore(1) 

buffer = []
for i in range(n):
    buffer.append(-1)
    
in_index = 0    #global variable
out_index = 0   #global variable

#now time to create the producer and consumer threads

#producer fxn
def producer():
    counter = 0
    global in_index, buffer, full, empty, mutex
    while (counter < 100):
        print(f"Producer is waitng for an empty spot.")
        empty.acquire() #wait fxn
        print(f"Producer has acquired an empty spot.")
        print(f"Producer is waiting to get access to the buffer.")
        mutex.acquire() #wait fxn
        print(f"Producer got access to the buffer.")
        buffer[in_index] = counter
        print(f"Producer added {counter} at index value {in_index}.")
        in_index = (in_index + 1) % n
        counter += 1
        mutex.release() #signal fxn
        print(f"Producer released the buffer.")
        full.release()  #signal fxn
        print(f"Producer notifies Consumer that it has added an item to the buffer.")
        time.sleep(1)

#consumer fxn
def consumer():
    consumed = 0
    global out_index, buffer, empty, full, mutex
    while(consumed < 100):
        print(f"Consumer is waiting on something to Consume.")
        full.acquire()  #wait fxn
        print(f"Consumer is trying to get access to the buffer.")
        mutex.acquire() #wait fxn
        value = buffer[out_index]
        buffer[out_index] = -1
        out_index = (out_index + 1) % n
        consumed += 1
        print(f"Consumer has consumed {consumed} from index value {out_index}")
        mutex.release() #signal fxn
        print(f"Consumer is signaling Producer of an available spot.")
        empty.release() #signal fxn
        print(f"Consumer successfully consumed an item.")
        time.sleep(2)
    

p1 = threading.Thread(target = producer, args=())
c1 = threading.Thread(target = consumer, args=())

p1.start()
c1.start()
p1.join()
c1.join()