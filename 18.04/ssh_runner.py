import subprocess
import time

sshd_run_args = ["/usr/sbin/sshd", "-D", "-p", "33"]
sshd_process = subprocess.Popen(sshd_run_args)

sshd_process.wait()
