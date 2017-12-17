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

## Disable the disco lights (optional)
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

## Adding your first device
A Z-Wave device is called a node. Each node has different pairing commands. Refer to your device manual to find the pairing command for your device. For instance, to add a Fibaro Wall Plug, triple-click the button on the side of the plug.

1. Go to your `Z-Wave` page under `Configuration` in the sidebar.
2. Click `Add Node`
3. Run the pair command on your Z-Wave device
4. Your device should now be added. You can see it if you click the drop-down list called `Nodes`.
5. At this point it will not have a name, and if you do not name it, it will be named according to the manufacturer's name. Click the node in the drop-down list. Enter the new name and click `RENAME NODE`. A tip is to think carefully before you name it. If you want to rename it later on, it will require a bit of extra work.
6. Restart Home Assistant. Your Node will now show.
