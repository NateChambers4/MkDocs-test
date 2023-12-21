# **How to run `tPMS_blynk.py` on Raspberry Pi running Raspbian**

This guide explains how to run the Python script `tPMS_blynk.py` on a Raspberry Pi running the Raspbian operating system. The script collects data from a DHT11 or DHT22 temperature and humidity sensor and a PMS7003 particle matter sensor and sends the data to Blynk.

## Prerequisites

1. Your Raspberry Pi is running the Raspbian operating system.
2. You have configured the Raspberry Pi's serial port settings:
   - Open the Raspberry Pi configuration settings by running `sudo raspi-config` in the terminal.
   - Navigate to "Interface Options" -> "Serial Port".
   - Ensure that the Serial Port is enabled, and the Serial Console is disabled.
3. Python 3 is installed. You can check the installed Python version by running `python3 --version` in the terminal.
4. Required Python libraries: BlynkLib, pigpio_dht, pandas. You can install these by running `pip3 install BlynkLib pigpio_dht pms7003 pandas`.
5. Install numpy: `sudo apt-get install libatlas-base-dev`
6. Open your terminal and execute the following commands to install the necessary libraries and clone the Blynk Python library: `git clone https://github.com/vshymanskyy/blynk-library-python.git`.
7. Place the `tPMS_blynk.py` script into the `blynk-library-python` folder


## Steps to Run the Script

1. Open the terminal.
3. If not already done, run the Pigpio daemon. The daemon provides access to the GPIO pins of the Raspberry Pi, which is necessary for reading data from the sensors. Run the daemon by entering `sudo pigpiod` in the terminal.
4. Run the script by entering `python3 /home/pi/blynk-library-python/tPMS_blynk.py` in the terminal.
5. The script will now run indefinitely until stopped. While running, it will collect data from the sensors every two seconds and send this data to Blynk.

### Stopping the Script

- To stop the script, press `Ctrl + C` in the terminal. This will terminate the script.

## Troubleshooting

- If you encounter a `DHT sensor failure. Check wiring.` error, check the connection of your DHT sensor to the Raspberry Pi. Ensure that the data pin of the sensor is connected to the correct GPIO pin on the Raspberry Pi.
- If you encounter errors while reading from the PMS sensor or sending data to Blynk, these may be due to temporary issues like a poor internet connection. The script will continue running and try again during the next interval.
- If the script cannot connect to the Pigpio daemon, make sure the daemon is running. You can start it by running `sudo pigpiod` in the terminal. If the error persists, the issue may be due to the daemon's host or port settings. Check these settings and try again.
  
Remember to replace `BLYNK_AUTH_TOKEN` with your actual Blynk authentication token and adjust `DHT_SENSOR` and `DHT_PIN` if necessary.

Note: This guide assumes you've wired your sensors correctly and that your Blynk setup is configured correctly. It focuses on running the Python script and doesn't cover the hardware setup or Blynk configuration.