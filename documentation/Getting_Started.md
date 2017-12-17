# 1. Getting Started
## Hardware needed
* 1 x Raspberry Pi 3
* 1 x Adafruit Pi Case
* 1 x 2.5A Power Supply (Raspberry Foundation)
* 1 x SDHC Card
* 1 x CAT-6 Cable

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

If you're using a Mac computer, open finder. Hit `cmd+K` and connect to `smb://hassio.local`. You will be asked which folder you want to open. Choose `config`.

You now have access to your configuration. In order to edit the `.yaml` files I recommend using a dedicated editor. I use [Atom](www.atom.io)
