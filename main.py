import LPT
import OPT
from random import randint
from copy import deepcopy
from matplotlib import pyplot as plt
import time


def getInput():
    n, m = map(int, input().split(' '))
    Jobs = []
    Schedule = [[] for _ in range(m)]
    for i in range(n):
        capacity = int(input())
        Jobs.append((capacity, i))
    return [n, m, Jobs, Schedule]


def generateInput():
    n = randint(1, 12)
    m = randint(1, 3)
    Jobs = []
    Schedule = [[] for _ in range(m)]
    for i in range(n):
        capacity = randint(1, 10 ** 6)
        Jobs.append((capacity, i))
    return [n, m, Jobs, Schedule]


def plotApproximation(LPTCoeffList, LSCoeffList, ax):
    ax.title.set_text('Approximation of various algorithms')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Approximation')
    ax.plot(LPTCoeffList, label='LPT')
    ax.plot(LSCoeffList, label='List scheduling')
    ax.legend()


def plotExecutionTime(OPTTime, LPTTime, LSTime, ax):
    ax.title.set_text('Execution time of various algorithms')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Execution time')

    ax.plot(OPTTime, label='Enumeration')
    ax.plot(LPTTime, label='LPT')
    ax.plot(LSTime, label='List scheduling')
    ax.legend()


if __name__ == '__main__':
    LPTCoeffList, LSCoeffList = [], []
    OPTTime, LPTTime, LSTime = [], [], []
    for it in range(100):
        if it % 10 == 0:
            print("Iteration: ", it)
        n, m, Jobs, Schedule = generateInput()

        startTime = time.time()
        OPTSchedule, OPTResult = OPT.assign(n, m, deepcopy(Jobs), deepcopy(Schedule))
        OPTTime.append(time.time() - startTime)

        startTime = time.time()
        LPTSchedule, LPTResult = LPT.assign(n, m, deepcopy(Jobs), deepcopy(Schedule), LPT=True)
        LPTTime.append(time.time() - startTime)
        LPTCoeff = LPTResult / OPTResult
        assert (LPTCoeff <= 4 / 3 and LPTCoeff >= 1)
        LPTCoeffList.append(LPTCoeff)

        startTime = time.time()
        LSSchedule, LSResult = LPT.assign(n, m, deepcopy(Jobs), deepcopy(Schedule), LPT=False)
        LSTime.append(time.time() - startTime)
        LSCoeff = LSResult / OPTResult
        assert (LSCoeff <= 2 and LSCoeff >= 1)
        LSCoeffList.append(LSCoeff)

    print("Average LPT coeff: ", sum(LPTCoeffList) / len(LPTCoeffList))
    print("Average LS coeff: ", sum(LSCoeffList) / len(LSCoeffList))
    print()
    print("Average Enumeration execution time: ", sum(OPTTime) / len(OPTTime))
    print("Average LPT execution time: ", sum(LPTTime) / len(LPTTime))
    print("Average LS execution time: ", sum(LSTime) / len(LSTime))

    fig, axs = plt.subplots(2, 1)

    plotApproximation(LPTCoeffList, LSCoeffList, axs[0])
    plotExecutionTime(OPTTime, LPTTime, LSTime, axs[1])

    fig.tight_layout()
    plt.show()
