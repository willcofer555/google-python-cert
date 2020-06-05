import psutil
import shutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free < 10

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80


print(check_disk_usage("/"))
print(check_cpu_usage())

if not check_disk_usage("/") or not check_cpu_usage():
    print("Error")
else:
    print("all is well")
