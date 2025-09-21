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
    # clear_directory = subprocess.run('rm -rf build/html build/doctree', shell=True).returncode == 0
    clear_directory = True
    # build = subprocess.run('make clean html', shell=True).returncode == 0
    # pdf = subprocess.run('make latexpdf', shell=True).returncode == 0
    # if clear_directory and build:
    if clear_directory and process('make clean html'):
        message = input('\nenter a commit message: ')
        # subprocess.run(f'git commit -am {message}', shell=True).returncode == 0
        process(f'git commit -am {message}')
        return True