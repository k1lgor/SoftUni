jobs = [int(x) for x in input().split(', ')]
index = int(input())

jobs_before_finish = []

for i in range(len(jobs)):
    if jobs[index] >= jobs[i]:
        jobs_before_finish.append(jobs[i])
print(sum(jobs_before_finish))

