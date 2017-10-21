# Install Guide for Cleanflight and Control via MSP

## Compiling Firmware

Download [firmware](https://github.com/cleanflight/cleanflight) and compile with

`make TARGET=NAZE OPTIONS=USE_MSP_UART`

There is also a version located [cleanflight_2.1.0_NAZE.hex][here]. 

## Flashing Fimware

1. Open the [cleanflight configurator](https://chrome.google.com/webstore/detail/cleanflight-configurator/enacoimjcgeinfnnnpajinjgmkahmfgb)
and go to the "Firmware Flasher" tab.  This tab is before you connect to the base station. 

2. Click "Load Firmware \[local\]" and load your custom firmware file from 
`cleanflight/obj/cleanflight_x.y.z_NAZE.hex`

(Stefanie loaded the firmwar

## Configuration Options

1. Plug in Skyline and click "Connect"

2. Go to "Ports" tab and disable SerialRX for UART2

3. Go to "Configuration" tab and flip the yaw by 180 degrees

4. Also change the receiver to "MSP_RX"

5. Go to the "Reveiver" tab and change the input map to "AERT1234"

6. Plug the skyline back into the Pi and you should be set to fly!

## Other Options

### Throttle Angle Compensation

Go to "CLI" tab and type

`set thr_corr_value = XX` and `set thr_corr_angle = YY`

This will set it (linearly?) so that it adds `XX` to the throttle when at angle `YY`
