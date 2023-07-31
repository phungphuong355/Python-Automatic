#!/usr/bin/env python3
# shebang
# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from modules import areas
from modules import health_computer as hc


def print_hi(name):
    # Calculate area
    print(areas.triangle(3, 5))
    print(areas.circle(4))

    # Check
    if not hc.check_disk_usage("/") == hc.check_cpu_usage():
        print("ERROR!")
    else:
        print("Everything is ok!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
