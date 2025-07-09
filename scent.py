import sniffer.api
import subprocess
import os


@sniffer.api.file_validator
def rst_files(filename):
    return (filename.endswith(".rst") or filename.endswith('.py')) # and not os.path.basename(filename).startswith(".")

@sniffer.api.runnable
def run_tests(*args):
    # clear_directory = subprocess.run('rm -rf build/html build/doctree', shell=True).returncode == 0
    clear_directory = True
    build = subprocess.run('make html', shell=True).returncode == 0
    # pdf = subprocess.run('make latexpdf', shell=True).returncode == 0
    if clear_directory and build:
        return True