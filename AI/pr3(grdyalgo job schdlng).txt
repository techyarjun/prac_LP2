# Job Scheduling Problem

jobs = [
    ('J1', 2, 100),
    ('J2', 1, 50),
    ('J3', 2, 10),
    ('J4', 1, 20),
    ('J5', 3, 30)
]

jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = max(job[1] for job in jobs)

slots = [False] * max_deadline
result = []

profit = 0

for job in jobs:
    name, deadline, p = job

    for j in range(deadline - 1, -1, -1):
        if not slots[j]:
            slots[j] = True
            result.append(name)
            profit += p
            break

print("Selected Jobs:", result)
print("Total Profit:", profit)