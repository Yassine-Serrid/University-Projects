import random
import Table as table
from main import Process 

processes = []

def generateRandomProcess(n, burst, priority):
    processes.append(Process(0+1, 0, random.randint(1, burst), random.randint(1, priority)))

    for i in range(1, n):
        p = Process(i+1, 0, random.randint(1, burst), random.randint(1, priority))
        processes.append(p)

    for i in range(1, n):
        at = processes[i-1].arrival_time + random.randint(1, 5)
        processes[i].arrival_time = at

    x = random.randint(0, n/2)
    y = random.randint(2, 5)

    # Uncomment to see which processes have same arrival time
    # print("x = ", x+1)
    # print("y = ", y)

    for i in range(0, y):
        processes[x+i].arrival_time = processes[x].arrival_time

    table.dumpProcessInfo(processes)

def main(n, burst, priority):
    generateRandomProcess(n, burst, priority)

if __name__ == '__main__':
    priority = 20
    burst = 30
    n = int(input("Number of processes: "))
    main(n, burst, priority)