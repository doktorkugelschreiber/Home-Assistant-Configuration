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

If you're using a Mac computer, open finder. Hit `cmd+K` and connect to `smb://hassio.local`. You will be asked which folder you want to open. Choose `config`.

You now have access to your configuration. In order to edit the `.yaml` files I recommend using a dedicated editor. I use [Atom](www.atom.io).

## Installing Z-Wave
1. Insert Z-Stick in Raspberry Pi USB Port.
2. Open your `configuration.yaml`
3. Add the following lines to your configuration.
```
zwave:
  usb_path: /dev/ttyACM0
```
4. Save your configuration, then go to your Home Assistant instance in your browser.
5. Click on `Configuration` in the sidebar. Then click `General`. Scroll down to `Server Management` and click `Restart`.

When Home Assistant has restarted, you should have a settings panel called `Z-Wave` when you click `Configuration` in the side bar.

## Disable the disco lights
Your Z-Stick's LED is probably blinking in different colors. If you find that annoying, there is a way to disable it.
1. Open your `configuration.yaml`.
2. Somewhere along the lines, add the following code:
```
shell_command:
  disco_off: echo -e -n "\x01\x08\x00\xF2\x51\x01\x00\x05\x01\x51" > /dev/ttyACM0
```
3. Save your configuration and restart Home Assistant as described above.
4. After the restart, open the sidebar. In the bottom left there is an icon that looks like a remote control. Click it.
5. You should now see a page called `Services`.
6. In the `Service` entry, enter `shell_command.disco_off`.
7. Click `CALL SERVICE`.
8. Disco lights should now be off.

## Components
**Automations**
**Scripts**
**Scene picker**
**Timers**

**Custom UI**
* [State cards](https://github.com/andrey-git/home-assistant-custom-ui) used to add sliders for dimmable lights.

**Custom Themes**
* [Midnight theme](https://community.home-assistant.io/t/midnight-theme/28598)
* [Grey Night theme](https://community.home-assistant.io/t/grey-night-theme/30848)
