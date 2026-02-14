#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


import socket

def get_free_port(start_port=8000, max_tries=20):
    port = start_port
    for _ in range(max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError("No free port found.")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # If running the server, check for port in use and auto-increment
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        # Default port is at the end of the command, e.g. runserver 0.0.0.0:8000
        if len(sys.argv) > 2 and ':' in sys.argv[2]:
            host, port = sys.argv[2].rsplit(':', 1)
            try:
                port = int(port)
            except ValueError:
                port = 8000
            free_port = get_free_port(port)
            if free_port != port:
                print(f"Port {port} in use, switching to {free_port}.")
                sys.argv[2] = f"{host}:{free_port}"
        else:
            free_port = get_free_port(8000)
            if free_port != 8000:
                print(f"Port 8000 in use, switching to {free_port}.")
                sys.argv.append(f"0.0.0.0:{free_port}")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
