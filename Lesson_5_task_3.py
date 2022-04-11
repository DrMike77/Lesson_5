with open("salary.txt") as f:
    w_list = [w_line.split() for w_line in f.readlines()]
workers_with_info = [{"name": worker[0], "salary": float(worker[1])}
    for worker in w_list
    if len(worker) > 1]
for worker in workers_with_info:
    if worker['salary'] < 20_000:
        print(worker['name'])
