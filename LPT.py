import bisect


def assign(n, m, Jobs, Schedule, LPT=False):
    if LPT:
        Jobs.sort(reverse=True)

    result = 0
    MachineLoad = list((0, i) for i in range(m))
    for jobCapacity, jobID in Jobs:
        machineLoad, machineID = next(iter(MachineLoad))
        MachineLoad.remove((machineLoad, machineID))
        newMachineLoad = machineLoad + jobCapacity
        Schedule[machineID].append([jobID, newMachineLoad])
        bisect.insort_left(MachineLoad, (newMachineLoad, machineID))
        result = max(result, newMachineLoad)

    return Schedule, result


if __name__ == '__main__':
    assign(LPT=True)
