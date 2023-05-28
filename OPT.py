from copy import deepcopy

INF = 10 ** 10
_resultTime = INF
_resultSchedule = []


def enumerate(n, m, Jobs, Schedule, currentTime=0):
    global _resultTime, _resultSchedule
    if len(Jobs) == 0:
        if currentTime < _resultTime:
            _resultTime = currentTime
            _resultSchedule = deepcopy(Schedule)
        return

    jobCapacity, jobID = Jobs[-1]
    Jobs.pop()

    for machineID in range(m):
        newSchedule = deepcopy(Schedule)
        if len(newSchedule[machineID]):
            newSchedule[machineID].append([jobID, newSchedule[machineID][-1][1] + jobCapacity])
        else:
            newSchedule[machineID].append([jobID, jobCapacity])
        enumerate(n, m, deepcopy(Jobs), deepcopy(newSchedule), max(currentTime,
            newSchedule[machineID][-1][1]))


def assign(n, m, Jobs, Schedule):
    global _resultTime, _resultSchedule
    _resultTime = INF
    _resultSchedule = []
    if n > m:
        enumerate(n, m, deepcopy(Jobs), deepcopy(Schedule))
    else:
        _resultSchedule = deepcopy(Schedule)
        _resultTime = Jobs[0][0]
        for machineID in range(n):
            _resultSchedule[machineID].append([Jobs[machineID][1], Jobs[machineID][0]])
            _resultTime = max(_resultTime, Jobs[machineID][0])
    return _resultSchedule, _resultTime
