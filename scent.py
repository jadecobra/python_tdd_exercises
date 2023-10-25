import sniffer.api
import subprocess
import os


@sniffer.api.file_validator
def rst_files(filename):
    return filename.endswith(".rst") and not os.path.basename(filename).startswith(".")


@sniffer.api.runnable
def run_tests(*args):
    if subprocess.run("make html", shell=True).returncode == 0:
        return True
