# IoT & Education: A Global City Teams Challenge Project

This is where we store source code and documents that project participants can use.

The GitHub site is broken down into two components:

* [Code Repository](https://github.com/IoTDevLabs/iot-educ) - where source code is kept, such as Python programs and bash scripts
* [Wiki Pages](https://github.com/IoTDevLabs/iot-educ/wiki) - where descriptive information is kept, such as a list of reference books

---

## Code Repository

The code repository is organized as a set of folders:

* **[rpi](https://github.com/IoTDevLabs/iot-educ/tree/master/rpi)** - contains programs and scripts for Raspberry Pi
* **[bbb](https://github.com/IoTDevLabs/iot-educ/tree/master/bbb)** - contains programs and scripts for BeagleBone Black 
* _folders for other devices and IoT Dev Kits will be added here_

### Downloading a copy of the Code Repository

The entire code repository can be downloaded by clicking on this link:

* https://github.com/IoTDevLabs/iot-educ/archive/master.zip

If you are logged onto a device running Linux, such as a Raspberry Pi or BeagleBone Black, you can use the following command line program to download the respository to your device:

`wget https://github.com/IoTDevLabs/iot-educ/archive/master.zip`

If you're using Git on the Pi or on your laptop, you can clone this repository using this command:

`git clone https://github.com/IoTDevLabs/iot-educ.git`

### Quickstart on a Raspberry Pi

*These instructions assume you're running the latest version of the Raspbian operating system on your Raspberry Pi and that you have your Pi connected to the Internet.*

1. Log into the Pi.
1. Verify you have Internet connectivity:
  1. ping www.google.com
  2. *If you have Internet connectivity you should see a response that shows a time= value on the right side of each line. If you get a message saying something like 'Destination Host Unreachable' or 'Timeout' or 'No Response' then you don't have a working Internet connection for the Pi. Work on getting your Pi connected to the Internet either through a LAN cable or by using WiFi.*
1. Download and apply latest operating system updates:
  1. `sudo apt-get update`
  2. `sudo apt-get upgrade`
    1. *If upgrades are available, they will be displayed and you will be asked whether to continue. Press Enter to select the default option of Y for yes.*
1. Clone the git repository containing the template code:
  1. `git clone https://github.com/IoTDevLabs/iot-educ.git`
1. Install Python packages used by the template code:
  1. `cd iot-educ/rpi`
  2. `./install-python-packages.sh`
1. Run the template program to read and print the Pi's CPU temperature:
  1. `python read-cpu-temp.py`
  2. *Each time you run this program you should see the Pi's CPU temperature printed out in both Celsius and Fahrenheit*
1. Run the template program to continously read and print the CPU temperature and write it to Pi Land room 404:
  1. `python cpu-temp-piland.py`
  2. *When this program runs you should see a URL printed out every 2 seconds and the temperature data value should be appearing in [Pi Land room 404](http://piland.socialdevices.io/404/display) in the first data slot at the top right. If you heat or cool the Pi board you should see the temperature change.*

### Next Steps

From here you can modify the cpu-temp-piland.py program to use your own Pi Land room number, and if you wish, you can modify the device name string and/or data slot number being used.

Once you get this first program working and learn how to modify it for your own room, you can move on to some of the other programs.
