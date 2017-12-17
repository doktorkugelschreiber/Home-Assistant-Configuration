# Read Me
This is a copy of my Home Assistant Configuration. The configuration is a work in progress. I will be implementing new hardware and software as time progresses.

# This configuration runs on
**Hub Hardware**
* 1 x Raspberry Pi 3
* 1 x Adafruit Pi Case
* 1 x 2.5A Power Supply (Raspberry Foundation)
* 1 x 16 GB SanDisk SDHC Card
* 1 x Aetoec Z-Stick (gen. 5)
* 1 x CAT-6 Cable

**Z-Wave Devices**
* 5 x Fibaro Wall Plug
* 3 x NEXA AD-147 Dimmable Wall Plug

**Other smart devices**
* 1 x SONOS Playbar
* 1 x Apple TV (gen. 3)

# Set Up
## Installing Hass.io
1. [Download Hass.io for Raspberry Pi 3](https://github.com/home-assistant/hassio-build/releases/download/1.1/resinos-hassio-1.1-raspberrypi3.img.bz2)
2. [Download Etcher.io](https://etcher.io)
3. Using Etcher, flash Hass.io on to your SDHC Card

## Installing your Raspberry Pi
1. Mount Pi in Pi Case.
2. Insert the flashed SD card.
3. Using the CAT-6 Cable, connect the Pi to your router.
4. Connect the power supply.

Hass.io will now start to set up. It can take up to 20 minutes. In your web browser, go to "hassio.local". When set up, you will see your instance of Home Assistant. At this point, you probably won't see anything but some weather indicators. 

## Access your configuration
In order to access the configuration files, you will need to set up Samba share, which lets you connect to the configuration directory from your computer.

In the sidebar click "Hass.io" and on the top bar press the shopping bag. Click on Samba Share and install it. Open Samba Share and change the username and password. Then hit the Start button to start the addon.

If you're using a Mac computer, open finder. Hit cmd+K and connect to smb://hassio.local.

## Components
**Automations**
**Scripts**
**Scene picker**
**Timers**

**Custom UI**
* State cards: https://github.com/andrey-git/home-assistant-custom-ui used to add sliders for dimmable lights

**Custom Themes**
* Midnight theme: https://community.home-assistant.io/t/midnight-theme/28598
* Grey Night theme: https://community.home-assistant.io/t/grey-night-theme/30848
