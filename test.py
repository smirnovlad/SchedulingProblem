import pytest
import OPT
import LPT

def test_JobsLessThanMachines():
    n, m = 6, 7
    Jobs = [(capacity, index) for (index, capacity) in enumerate([4, 19, 21, 23, 13, 1])]
    Schedule = [[] for _ in range(m)]
    assert(OPT.assign(n, m, Jobs, Schedule)[1] == 23)

def test_OneMachine():
    n, m = 9, 1
    Jobs = [(capacity, index) for (index, capacity) in enumerate([i for i in range(1, n + 1)])]
    Schedule = [[] for _ in range(m)]
    assert(OPT.assign(n, m, Jobs, Schedule)[1] == sum([i for i in range(1, n + 1)]))

def test_SortedJobs():
    n, m = 7, 3
    Jobs = [(capacity, index) for (index, capacity) in enumerate([i for i in range(n, 0)])]
    Schedule = [[] for _ in range(m)]
    assert(LPT.assign(n, m, Jobs, Schedule, LPT=True)[1] == LPT.assign(n, m, Jobs, Schedule, LPT=False)[1])
