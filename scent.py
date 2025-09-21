import sniffer.api
import subprocess
import os

def process(command):
    return subprocess.run(command, shell=True).returncode == 0

@sniffer.api.file_validator
def rst_files(filename):
    return (filename.endswith(".rst") or filename.endswith('.py')) # and not os.path.basename(filename).startswith(".")

@sniffer.api.runnable
def run_tests(*args):
    # pdf = subprocess.run('make latexpdf', shell=True).returncode == 0
    if process('make clean html'):
        message = input('\nenter a commit message: ')
        process(f'git commit -am {message}')
        return True