class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    n = len(jobs)
    slot = [False] * n
    result = ['-'] * n

    for job in jobs:
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job.id
                break

    print("Scheduled Jobs:", end=" ")
    for job_id in result:
        if job_id != '-':
            print(job_id, end=" ")
    print()

jobs = [
    Job('a', 2, 100),
    Job('b', 1, 19),
    Job('c', 2, 27),
    Job('d', 1, 25),
    Job('e', 3, 15)
]

job_scheduling(jobs)

