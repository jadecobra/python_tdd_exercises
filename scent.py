import sniffer.api
import subprocess
import os

# Global variable to hold the sphinx-autobuild process
autobuild_process = None

def process(command):
    return subprocess.run(command, shell=True).returncode == 0

@sniffer.api.file_validator
def rst_files(filename):
    # Skip hidden files/directories and common non-source directories
    parts = filename.split(os.sep)
    if any(part.startswith('.') for part in parts):
        return False
    
    ignored_dirs = {'build', 'venv', '.venv', 'node_modules', '__pycache__', 'notes'}
    if any(part in ignored_dirs for part in parts):
        return False

    return filename.endswith(".rst") or filename.endswith('.py')

@sniffer.api.runnable
def run_tests(*args):
    global autobuild_process
    
    # If the process is already running, we don't need to do anything
    # because sphinx-autobuild has its own internal watcher.
    if autobuild_process is not None and autobuild_process.poll() is None:
        return True

    # Start sphinx-autobuild in the background if it's not running.
    # We use -j auto for parallel builds and --open-browser to make it easy to view.
    # Note: --open-browser might be annoying in some CLI environments, 
    # but it's a common preference for 'autobuild'.
    command = 'uv run sphinx-autobuild source build/html -j auto --open-browser'
    
    print(f"Starting sphinx-autobuild: {command}")
    autobuild_process = subprocess.Popen(command, shell=True)
    
    return True
