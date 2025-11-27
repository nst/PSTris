# PSTris
A Tetris implementation in PostScript

<img src="pstris.gif" width="320" align="center"></src>

#### Motivation

- implement a realtime game in PostScript
- play it in Ghostscript on macOS

See also:

- [PSChess](https://github.com/nst/PSChess)
- [PSSokoban](https://github.com/nst/PSSokoban)
- [Programming in PostScript](https://seriot.ch/projects/programming_in_postscript.html)

### Features

- 600 lines, 10 KB of PostScript
- 69 unique operators
- realtime input
- direct drop
- levels with increasing speed
- 7-tetriminos random bags
- high scores
- Nintendo scoring scheme
- sound through external MIDI synthetizer

### Play Tetris in Ghostscript

Terminal window 1:

    $ gs -sNOSAFER tetris.ps

Terminal window 2:
    
    $ stty raw -echo; cat >> t.txt

Play with arrows and space bar in window 2.

### Sound (Optional)

The program write MIDI commands in `midi.bin`.

You can read `midi.bin` from a helper script to send the commands to a synthetizer.

On macOS, you can use GarageBand and the brigde `midi.py`:

    1. in "Audio MIDI Setup" application, open "IAC Driver" and check "Device in online"
    2. in "GarageBand" application, create a new empty project with a MIDI track. "8-Bit Grit" instrument works fine.
    3. run `tail -f midi.bin | python3 midi.py`

### Notes and Limitations

Some implementation details inspired from [MeatFighter](https://meatfighter.com/nintendotetrisai/).
