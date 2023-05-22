Steps to run the simulation -
1. Generate process first
    python3 ProcessGenerator.py
    Number of processes: 100
    Max limit for CPU burst: 30
    Maximum limit for priority: 20

2. Run the simulator
    python3 main.py

    Starting SJF scheduling algorithm
    running sjf...
    Average waiting time =  514.82
    Average turnaround time =  532.65

    Starting Priority scheduling algorithm
    running priority...
    Average waiting time =  695.25
    Average turnaround time =  713.08