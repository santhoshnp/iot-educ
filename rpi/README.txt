-----------------------------------------------------------------------------------
Programs and scripts for Raspberry Pi running Raspbian operating system.
-----------------------------------------------------------------------------------

NOTE: To run the files that begin with "grove-" you have to first set up your
      GrovePi or GrovePi+ environment as described farther below.

README.txt - the file you're reading now; read through this entire file at
   least once before you try to do anything so you can get an overview of
   everything that's involved

install-python-packages.sh - install pre-requisite Python packages needed to run these programs
   To run, type in:  ./install-python-packages.sh

cpu-temp-piland.py - continuously read Pi's internal CPU temperature and write to Pi Land
   To run, type in:  python cpu-temp-piland.py

gpio-button-piland.py - continuously read a button connected to GPIO 17 and write to Pi Land
   To run, type in:  sudo python gpio-button-piland.py

grove-button-piland.py - continuously read a Grove button connected to port D3 and write to Pi Land
   To run, type in:  sudo python grove-button-piland.py

grove-button.py - continously read a Grove button connected to port D3 and print on/off state
   To run, type in:  sudo python grove-button.py

grove-buzzer-piland.py - continously read Pi Land and turn buzzer on or off
based on the data value that's read
   To run, type in:  sudo python grove-buzzer-piland.py

grove-buzzer.py - beep a Grove Buzzer connected to port D2
   To run, type in:  sudo python grove-buzzer.py

grove-dht11-dht22-piland.py - continuously read DHT11 and DHT22 Temp & Humidity sensors
and write to Pi Land
   To run, type in:  sudo python grove-dht11-dht22-piland.py

grove-dht11-piland.py - continuously read DHT11 Temp & Humidity and write to Pi Land
   To run, type in:  sudo python grove-dht11-piland.py

grove-dht22-piland.py - continuously read DHT22 Temp & Humidity and write to Pi Land
   To run, type in:  sudo python grove-dht22-piland.py

grove-lcd-piland.py - continuously read a Pi Land data slot and print on LCD display
   To run, type in:  sudo python grove-lcd-piland.py

grove-lcd.py - print example messages on a Grove LCD display
   To run, type in:  sudo python grove-lcd.py
 
grove-led-piland.py - continously read Pi Land and turn LED on or off
based on the data value that's read
   To run, type in:  sudo python grove-led-piland.py

grove-led.py - flash a LED connected to port D6
   To run, type in:  sudo python grove-led.py

grove-light-piland.py - continously read Grove Light Sensor connected to port A1 and write to Pi Land
   To run, type in:  sudo python grove-light-piland.py

grove-relay-piland.py - continously read Pi Land and turn relay on or off
based on the data value that's read
   To run, type in:  sudo python grove-relay-piland.py

grove-sound-piland.py - continously read Grove Sound Sensor connected to port A0 and write to Pi Land
   To run, type in:  sudo python grove-sound-piland.py

grove-ultrasonic-piland.py - continuously read Ultrasonic Ranger and write to Pi Land
   To run, type in:  sudo python grove-ultrasonic-piland.py

grove_rgb_lcd.py - Grove LCD display driver routine (from GrovePi library); this file
   is part of the GrovePi software located under GrovePi/Software/Python/grove_rgb_lcd;
   this file needs to be in your same program directory in order to run programs that
   write to the Grove LCD display

read-cpu-temp.py - read Pi's internal CPU temperature and print in degrees C and F
   To run, type in:  python read-cpu-temp.py

read-mac-addr.py - read Pi's network MAC address and print it
   To run, type in:  python read-mac-addr.py

-----------------------------------------------------------------------------------
Setting up your Raspberry Pi for use with the GrovePi and GrovePi+
-----------------------------------------------------------------------------------

These instructions are based on the GrovePi information found on this web page:

http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/

Steps:

-----------------------------------------------------------------------------------
*** INSTRUCTION REFERENCE #1 ***
-----------------------------------------------------------------------------------

NOTE: The Raspberry Pi will automatically reboot during this step, so make sure you've
      saved any other work you've been doing before you perform these steps.
 
Make sure your Raspberry Pi is connected to the Internet either through an Ethernet
cable or through a Wi-Fi link.

Log into your Raspberry Pi, either through the Ethernet network, the Wi-Fi network,
or using an HDMI monitor and USB keyboard directly connected to the Pi.

Type in these commands in the bash shell:

   cd ~
   git clone https://github.com/DexterInd/GrovePi
   cd GrovePi/Script
   sudo chmod +x install.sh
   sudo ./install.sh

Press ENTER key when instructed to press ENTER to begin

Press "y" and ENTER when prompted "Do you want to continue [Y/n]?

The Raspberry Pi will automatically restart when the installation is complete.

After the Raspberry Pi has rebooted log back in.

-----------------------------------------------------------------------------------
*** INSTRUCTION REFERENCE #2 ***
-----------------------------------------------------------------------------------

If you are running a recent Raspberry Pi (3.18 kernel or higher) you may also need to
update the /boot/config.txt file. Edit it with 'sudo nano /boot/config.txt' and add these
lines at the end:

 dtparam=i2c1=on
 dtparam=i2c_arm=on

Note that the "1" in "i2c1" is a one not an L!

These lines may have already been automatically added for you depending on what
version you're using.

If you added these lines, reboot the Pi and then log back in.

-----------------------------------------------------------------------------------
*** INSTRUCTION REFERENCE #3 ***
-----------------------------------------------------------------------------------

Type in this command in the bash shell:

   sudo adduser pi i2c

Now log out of the Pi and then log back in. This is needed for the adduser
change to take effect.

-----------------------------------------------------------------------------------
*** INSTRUCTION REFERENCE #4 ***
-----------------------------------------------------------------------------------

Type in this command in the bash shell:

   sudo i2cdetect -y 1

You should see an output that looks like this:

     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- 04 -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --

-----------------------------------------------------------------------------------
*** INSTRUCTION REFERENCE #5 ***
-----------------------------------------------------------------------------------

Now we'll check if the GrovePi is working.

Connect a Grove LED to port D4 using the cable.

Type in these commands in a bash shell:

   cd ~
   cd GrovePi/Software/Python
   python grove_led_blink.py

If everything is working, the LED should start blinking.

-----------------------------------------------------------------------------------
*** INSTRUCTION REFERENCE #6 ***
-----------------------------------------------------------------------------------

Now we'll install the GrovePi Python package so you can use it from
anywhere on your Raspberry Pi.

Type in these commands in a bash shell:

   cd ~
   cd GrovePi/Software/Python
   sudo python setup.py install

-----------------------------------------------------------------------------------
*** INSTRUCTION REFERENCE #7 ***
-----------------------------------------------------------------------------------

At this point you should have a functioning GrovePi environment
and you can start running the IoT Education template programs
for Raspberry Pi found at:  https://github.com/IoTDevLabs/iot-educ

They are under the 'rpi' folder.

