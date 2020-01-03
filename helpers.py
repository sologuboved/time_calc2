import os
import sys
import re


def get_base_dir():
    return os.path.dirname(os.path.abspath(__file__))


def write_pid():
    prefix = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    previous_pid = find_previous_pid(prefix)
    if previous_pid:
        print("\nRemoving {}...".format(previous_pid))
        os.remove(previous_pid)
    pid_fname = '{}_{}.pid'.format(prefix, str(os.getpid()))
    print("Writing {}\n".format(pid_fname))
    with open(pid_fname, 'w') as handler:
        handler.write(str())
    return pid_fname


def find_previous_pid(prefix):
    for fname in os.listdir(get_base_dir()):
        if re.fullmatch(r'{}_\d+\.pid'.format(prefix), fname):
            return fname
