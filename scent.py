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
    make_html = 'make clean html'
    prep_pdf = 'sphinx-build -b latex source build/latex'
    make_pdf = 'make latexpdf'
    if process(prep_pdf) and process(make_pdf) and process(make_html):
        # message = input('\nenter a commit message: ')
        # process(f'git commit -am {message}')
        return True