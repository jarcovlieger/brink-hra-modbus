# Brink HRV Modbus Integration
Home Assistant integration to connect your Brink HRV (Heat Recovery Ventilation) to Home Assistant via Modbus TCP.

<img src="./Images/Sensors_and_controls.png"/>

## Installation
To install the Brink HRV Modbus Integration, follow these steps:

#### HACS installation
1. Open your <b>Home Assistant</b> instance.
2. Navigate to the <b>HACS</b>
3. Click the <b>3 dots menu</b>
4. Click on <b>Custom Repositories</b>
5. Fill in the repository ```https://github.com/jarcovlieger/brink-hrv-modbus```, and category <b>Integration</b>
6. Search for <b> Brink HRV Modbus </b> and click on download

#### Manual installation
1. Copy the ```brink_hrv_modbus``` folder into your ```custom_components``` folder

## Setup
1. Navigate to <b>Settings -> Devices & Services</b>
2. Click on <b>+ Add Integration</b>
3. Search for <b>"Brink HRV Modbus"</b>
4. Add in the <b>IP</b> of your modbus gateway and <b>port</b>

## Documentation
[modbus-uwa2-b-uwa2-e-installation-regulations-614882.pdf](https://www.brinkclimatesystems.nl/documenten/modbus-uwa2-b-uwa2-e-installation-regulations-614882.pdf)

## Tested devices
- Brink Flair 300
