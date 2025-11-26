# PSTris
A Tetris implementation in PostScript

<img src="pstris.gif" width="320" align="center"></src>

#### Motivation

- implement a realtime game in PostScript
- play it in GhostView on macOS

See also:

- [PSChess](https://github.com/nst/PSChess)
- [PSSokoban](https://github.com/nst/PSSokoban)
- [Programming in PostScript](https://seriot.ch/projects/programming_in_postscript.html)

### Features

- 600 lines or 10 KB of PostScript
- 69 different operators
- realtime input
- direct drop
- levels with increasing speed
- 7-tetriminos random bags
- high scores
- Nintendo scoring scheme
- sound through external MIDI synthetizer

### Play Tetris in GhostView

Terminal window 1:

    $ gs -sNOSAFER tetris.ps

Terminal window 2:
    
    $ stty raw -echo; cat >> t.txt

Play with arrows and space bar in window 2.

### Sound (Optional)

The program write midi commands in `midi.txt`.

You can read this file from a helper script to turn them into a MIDI commands for a synthetizer.

On macOS, you can use GarageBand and the brigde script `garageband.py`:

    1. in "Audio MIDI Setup" application, open "IAC Driver" and check "Device in online"
    2. in "GarageBand" application, create a new empty project with a MIDI track. "8-Bit Grit" instrument works fine.
    3. run `tail -f midi.txt | python3 garageband.py`

### Notes and Limitations

Some implementation details inspired from [MeatFighter](https://meatfighter.com/nintendotetrisai/).

Tested with [GhostView on macOS](https://github.com/johnhcc/homebrew-gs-x11).
