import shutil
import psutil


def check_disk_usage(disk: str):
    du = shutil.disk_usage(disk)
    free: float = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    usage: float = psutil.cpu_percent(1)
    return usage < 75
