#!/usr/bin/env python
# echos messages in the form of "echo [msg]\n"

import ttl100, time, sys, datetime
port = ttl100.get_serial_port()

while True:
    line = ""
    while len(line) == 0 or line[-1] != "\n":
        line += port.read(1)
    sys.stdout.write(str(datetime.datetime.now()) + " " + line)
    sys.stdout.flush()
    
    if line.startswith("echo "):
        ohce = "ohce "+line[5:]
        port.write(ohce)
        sys.stdout.write(str(datetime.datetime.now()) + " " + ohce)
        sys.stdout.flush()
        