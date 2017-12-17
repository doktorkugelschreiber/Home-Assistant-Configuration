# 2. Installing Z-Wave
## Hardware needed
* 1 x Aetoec Z-Stick (gen. 5)
* 1 x Z-Wave Device of your choice

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
