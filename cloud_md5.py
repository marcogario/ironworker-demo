import sys
import time

if len(sys.argv) != 2:
    print("Usage: %s <file>" % sys.argv[0])
    exit(-1)

file_content = open(sys.argv[1], 'rb').read()

from iron_worker import IronWorker, Task

worker = IronWorker()
task = Task(code_name="new_demo")
task.payload = file_content
response = worker.queue(task)
remote_task = worker.task(response)

while True:
    remote_task = worker.task(response)
    status = remote_task.status
    if status == "complete" or status=="error":
        break
    time.sleep(1)

raw_log = worker.log(response)
clean_log = []
do_copy = False
for line in raw_log.splitlines():
    if do_copy:
        clean_log.append(line)
    if line == "**OUTPUT**":
        do_copy = True
clean_log = "\n".join(clean_log)
print(clean_log)
