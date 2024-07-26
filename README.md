# Web API for TheThingsStack LoRaWAN application with MQTT integration template: Python DjangoREST Framework

This is Web API template for any LoRaWAN application than uses TheThingsNetwork infrastructure (TheThingsStack), created in Python with Django and DjangoREST framework.

![architecture scheme]()

## Functionality

- `manage LoRaWAN end device`: register/add new end-devices to your TTN application using API; with API you can integrate mobile or web front-end apps to manage your end-devices in application.
- `MQTT integration`: subscribe to your TTN application with MQTT client, track end-devices uplinks (messages) and send configurations and data with downlinks using API.
- `store end-devices informations`: using API and local database you can store your devices configurations and basic informations (like: devID, devEUI).
- `manage user access`: with build-in access management you can divide individal sections so only specified users can have access to specific end-devices.
- `cloud timeseries data integration`: integration with InfluxDB Cloud 2.0 for timeseries data storage - if your end devices colect measurements

## TODO

- [x] create venv and install vital components
- [] create pip requirements file (requirements.txt)
- [x] set up new basic project
- []
