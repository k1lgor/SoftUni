jobs = [int(x) for x in input().split(', ')]
index = int(input())

jobs_before_finish = [job for job in jobs if jobs[index] >= job]

print(sum(jobs_before_finish))
