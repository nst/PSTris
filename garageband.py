# see README.txt
# tail -f midi.txt | python3 garageband.py

import sys
import mido

OUTPUT_PORT_NAME = "IAC Driver Bus 1"

try:
    print(f"Connecting to '{OUTPUT_PORT_NAME}'...")
    with mido.open_output(OUTPUT_PORT_NAME) as port:
        print("Bridge is active")
        
        for line in sys.stdin:
            m = line.strip().split()
            if not m: continue

            print(m)
            
            msg = mido.Message(m[0], channel=int(m[1]), note=int(m[2]), velocity=int(m[3]))
            
            port.send(msg)

except OSError:
    print(f"Error: Could not find '{OUTPUT_PORT_NAME}'. Check that IAC Driver is enabled in Audio MIDI Setup.")
except KeyboardInterrupt:
    pass