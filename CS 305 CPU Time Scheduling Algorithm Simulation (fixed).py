import time

class ProcessClass:
    def __init__(self, process_num):
        self.process_num = process_num

    def running_phrase(self):
        print(f'I am process {self.process_num}.')
        print ('I am currently running!')
        print() 

process1 = ProcessClass(1)

process2 = ProcessClass(2)

process3 = ProcessClass(3)

process4 = ProcessClass(4)


process_queue = []
process_queue.append(process1)
process_queue.append(process2)
process_queue.append(process3)
process_queue.append(process4)

#add mechanism to count how much times a process has left before being added to the queue etc.
# check replit

x = 0
while(x < 10):
    process = process_queue.pop(0)
    process.running_phrase()
    time.sleep(5)
    process_queue.append(process)
    x += 1

