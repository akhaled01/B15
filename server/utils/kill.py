import subprocess
import signal
import os


def Kill9090():
    """
    Kills any process running on port listening on port 9090.
    """
    command = "netstat -ano | findstr 9090"
    c = subprocess.Popen(command, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = c.communicate()
    pid = stdout.decode().strip().split(' ')[-1]
    print(pid)
    os.kill(int(pid), signal.SIGKILL)
