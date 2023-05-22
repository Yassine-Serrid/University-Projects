import SJF as sjfAlgo
import Priority as priorityAlgo
import Table as table

processes = []

class Process:
    """
    Args:
        - p_id (int) : process ID
        - arrival_time (int) : process Arriva time in ready queue
        - burst_time (int) : Burst Time 
        - priority (int) : priority of the process , default: 1
    Defaults:
        - self.waiting_time = 0
        - self.return_time = 0
        - self.turnaround_time = 0
        - self.response_time = 0
        - self.completed = False
    """

    def __init__(self, p_id, arrival_time, burst_time, priority=1):
        self.p_id = p_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

        self.waiting_time = 0
        self.return_time = 0
        self.turnaround_time = 0
        self.response_time = 0
        self.completed = False

def readProcessInfo():
    n = int(input("Number of processes: "))
    fp = open("processes.txt", "r")
    
    # ignore following line as this is process identifier
    ignore = int(fp.readline())
    fp.readline()

    # process subsequent lines
    for i in range(0, n):
        line = fp.readline()
        process = line.split()
        id = int(process[0])
        at = int(process[1])
        bt = int(process[2])
        pr = int(process[3])
        processes.append(Process(id, at, bt, pr))
    
    # Uncomment to print process info
    # for p in processes:
    #     print(p.p_id, p.arrival_time, p.burst_time, p.priority)
    

def main():
    readProcessInfo()

    print("\nStarting SJF scheduling algorithm")
    rs_sjf = sjfAlgo.run(processes)
    print("Average waiting time = ", rs_sjf['avg_waiting_time'])
    print("Average turnaround time = ", rs_sjf['avg_turnaround_time'])

    print("\nStarting Priority scheduling algorithm")
    rs_pri = priorityAlgo.run(processes)
    print("Average waiting time = ", rs_pri['avg_waiting_time'])
    print("Average turnaround time = ", rs_pri['avg_turnaround_time'])

    # Uncomment to see tabular information 
    # table.plot(rs_sjf['processes'])
    # table.plot(rs_pri['processes'])

if __name__ == '__main__':
    main()