rem from pathlib import Path
rem exec(Path("filename.py").read_text())
rem pip install av
cd C:\ed\DJI
rem netsh wlan show networks
rem pause
netsh wlan show profiles
netsh wlan connect name="TELLO-627F41"
pause
rem python
python test.py
pause