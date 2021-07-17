# 디스크 컨트롤러


def solution(jobs):
    jobs.sort()
    n = len(jobs)
    task = jobs.pop(0)
    t = task[0] + task[1]
    laps = task[1]
    potential = []
    while jobs or potential:
        while jobs and jobs[0][0] <= t:
            potential.append(jobs.pop(0))
        if potential:
            potential.sort(key=lambda x: x[1])
            task = potential.pop(0)
            t += task[1]
            laps += t - task[0]
        else:
            task = jobs.pop(0)
            t = task[0] + task[1]
            laps += task[1]
    return laps // n