import re
from itertools import count

tasks = re.findall(
    '"([A-Z])"', re.match(r'tasks = \[(.*)\]', input()).groups()[0])

n = int(re.match("n = (\d+)", input()).groups()[0])

timetable = {}

task_it = iter(tasks)

task = None

mmr = []

for time in count():
    def get_time(id): return timetable.get(id, time) - time
    def set_time(id): timetable[id] = time+n+1
    try:
        if not task:
            task = next(task_it)
        if (get_time(task) == 0):
            set_time(task)
            mmr.append(task)
            task = None
        else:
            mmr.append("-")
    except:
        # print(mmr)
        print(time-1)
        break
