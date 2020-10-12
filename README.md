## Server Installation on Raspberry
* python3 and pip3
```
apt install python3 python3-pip
```
* Python module: zeroconf flask
```
pip3 install flask zeroconf
```
* Python module PySide2
```
apt install python3-pyside2.qt3dcore python3-pyside2.qt3dinput python3-pyside2.qt3dlogic python3-pyside2.qt3drender python3-pyside2.qtcharts python3-pyside2.qtconcurrent python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qthelp python3-pyside2.qtlocation python3-pyside2.qtmultimedia python3-pyside2.qtmultimediawidgets python3-pyside2.qtnetwork python3-pyside2.qtopengl python3-pyside2.qtpositioning python3-pyside2.qtprintsupport python3-pyside2.qtqml python3-pyside2.qtquick python3-pyside2.qtquickwidgets python3-pyside2.qtscript python3-pyside2.qtscripttools python3-pyside2.qtsensors python3-pyside2.qtsql python3-pyside2.qtsvg python3-pyside2.qttest python3-pyside2.qttexttospeech python3-pyside2.qtuitools python3-pyside2.qtwebchannel python3-pyside2.qtwebsockets python3-pyside2.qtwidgets python3-pyside2.qtx11extras python3-pyside2.qtxml python3-pyside2.qtxmlpatterns python3-pyside2uic
```

## Client Installation

## Sonoff R3 configuration
* Create the Wifi network `sonoffDiy / 20170618sn`
* Open the Sonoff R3 and plug-in jumper
* Start the Sonoff
* Retrieve the Sonoff IP address and the MAC address in the dnsmasq log at /var/log/syslog
* Configure the Wifi SSID and password of the Sonoff from POST request
* Add a rule to assign a Static IP to the Sonoff device in the Wifi server
* Plug in and out the Sonoff device
* Restart the sonoff-imt server

## POST requests description
* [Doc 1.4](SONOFF_DIY_MODE_Protocol_Doc_v1.4.md)
* [Doc 2.0](SONOFF_DIY_MODE_Protocol_Doc_v2.0_Doc.pdf)
