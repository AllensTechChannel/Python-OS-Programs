@echo off
py -m pip install --upgrade pip setuptools wheel
echo ===Playsound will revert to 1.2.2 as there is a common bug in 1.3.0 that prevnts from playsound to work correctly!===
py -m pip uninstall playsound
py -m pip install playsound==1.2.2
pythonplayer.py
