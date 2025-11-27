# mkfifo midi.bin; python3 midi.py < midi.bin

import sys
import mido

port_name = 'IAC Driver Bus 1'

try:
    with mido.open_output(port_name) as port:
        print(f"Bridge active. Sending to '{port_name}'...", file=sys.stderr)
        while True:
            # Wait for exactly 3 bytes (Status, Note, Velocity)
            data = sys.stdin.buffer.read(3)
            if len(data) < 3: break
            
            try: port.send(mido.Message.from_bytes(data))
            except ValueError as e: print(e)
except (OSError, KeyboardInterrupt) as e:
    print(e)
