# DDC Auto Brightness

Adjust your monitor brightness base on Sun altutide.

# Configuration

You have to set 3 brightness level:

    BRIGHTNESS_1 = 0
    BRIGHTNESS_2 = 10
    BRIGHTNESS_3 = 20

Your GPS location:

    LAT = 43.5321
    LNG = 3.8618

Then DDCAB will compute the brightness according to this table:

| Time                     | Brightness level        |
|:------------------------:|:-----------------------:|
| Before dawn              | level 1                 |
| Between dawn and sunsire | from level 1 to level 2 |
| Between sunrise and noon | from level 2 to level 3 |
| Between noon and sunset  | from level 3 to level 2 |
| Between sunset and dusk  | from level 2 to level 1 |
| After dusk               | level 1                 |

# System requirements

You need to install the python requirements:

    pip install -r requirements.txt

Then you also need ddcctl which can be found here:

    git clone https://github.com/kfix/ddcctl.git
    cd ddcctl
    make install

Make sure ddcctl works with your setup:

    # This sets the brightness to 100 for monitor #1
    ddcctl -d 1 -b 100
    # This sets the brightness to 0 for monitor #1
    ddcctl -d 1 -b 100

# Usage

First try it to check everything works, then set up a crontab that runs every minute:

    * * * * * /Users/yann/Documents/DDCAB/ddcab.py > /dev/null

# License

Creative Common BY NC SA 4.0
https://creativecommons.org/licenses/by-nc-sa/4.0/
