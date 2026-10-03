#!/usr/bin/env python3
"""Double-fork sphinx-autobuild so it survives the launching shell."""
from __future__ import annotations

import os
import sys


def main() -> int:
    if len(sys.argv) < 6:
        print(
            "usage: daemonize_autobuild.py PIDFILE LOGFILE REPO PORT BUILD_DIR",
            file=sys.stderr,
        )
        return 2
    pidfile, logfile, repo, port, build_dir = sys.argv[1:6]

    # First fork: parent returns immediately.
    pid = os.fork()
    if pid > 0:
        # Wait until the grandchild writes the pidfile (short).
        os._exit(0)

    os.setsid()

    pid = os.fork()
    if pid > 0:
        os._exit(0)

    os.chdir(repo)
    os.umask(0o022)

    log_fd = os.open(logfile, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    os.dup2(log_fd, 1)
    os.dup2(log_fd, 2)
    devnull = os.open("/dev/null", os.O_RDONLY)
    os.dup2(devnull, 0)
    os.close(log_fd)
    os.close(devnull)

    with open(pidfile, "w", encoding="utf-8") as fh:
        fh.write(str(os.getpid()))

    # exec uv; the python listener is often a child of `uv run`.
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.execvp(
        "uv",
        [
            "uv",
            "run",
            "sphinx-autobuild",
            "--host",
            "127.0.0.1",
            "--port",
            port,
            "source",
            build_dir,
            "-j",
            "auto",
        ],
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
