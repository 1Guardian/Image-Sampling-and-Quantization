import signal
import os
import sys
import subprocess
import time

def signal_handler(sig, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
while(1 == 1):
    print("HHello")
