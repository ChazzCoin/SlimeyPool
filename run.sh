#!/bin/sh

# sudo hdiutil create -fs HFS+ -volname "SlimeyPool1" -srcfolder "/Users/chazzromeo/ChazzCoin/SlimeyPool" SlimeyPool1.dmg
cd /Volumes/SlimeyPool
source /Volumes/SlimeyPool/venv/bin/activate
python /Volumes/SlimeyPool/run.py

