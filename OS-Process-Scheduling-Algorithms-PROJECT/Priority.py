import Table as table

def run(processes):
    """
        Priority Scheduling (Non-preemptive)
        _
    """

    print('running priority...')

    gantt = []

    # initialize
    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0
    total_return_time = 0

    # sort by arrival_time
    proc = sorted(processes, key=lambda proc: proc.priority)
    proc = sorted(proc, key=lambda proc: proc.arrival_time)

    # setting initial values
    proc[0].return_time = proc[0].burst_time
    proc[0].turnaround_time = proc[0].return_time - proc[0].arrival_time
    proc[0].response_time = 0
    proc[0].waiting_time = 0

    gantt.append((proc[0].p_id, (total_return_time, proc[0].burst_time)))

    # update total
    total_response_time += proc[0].response_time
    total_waiting_time += proc[0].waiting_time
    total_turnaround_time += proc[0].turnaround_time
    total_return_time += proc[0].burst_time

    # simulating the process
    for i in range(1, len(proc)):
        tem = proc[i-1].return_time
        low = proc[i].priority
        val = 0
        for j in range(i, len(proc)):
            if tem >= proc[j].arrival_time and low >= proc[j].priority:
                low = proc[j].priority
                val = j

        proc[val].response_time = tem
        proc[val].return_time = tem + proc[val].burst_time
        proc[val].turnaround_time = proc[val].return_time - \
            proc[val].arrival_time
        proc[val].waiting_time = proc[val].turnaround_time - proc[val].burst_time

        gantt.append(
            (proc[val].p_id, (total_return_time, proc[val].burst_time)))

        proc[i], proc[val] = proc[val], proc[i]

        # update total
        total_response_time += proc[i].response_time
        total_waiting_time += proc[i].waiting_time
        total_turnaround_time += proc[i].turnaround_time
        total_return_time += proc[i].burst_time

    proc = sorted(proc, key=lambda proc: proc.arrival_time)

    return {
        'name': 'PR-NP',
        'avg_waiting_time': total_waiting_time/len(proc),
        'avg_response_time': total_response_time/len(proc),
        'avg_turnaround_time': total_turnaround_time/len(proc),
        'processes': proc,
        'gantt': gantt
    }