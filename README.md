# Iovation Device Fingerprint Generator

This is a script to generate iovation device fingerprints. https://developer.bazaarvoice.com/conversations-api/tutorials/submission/device-fingerprinting/iovation-web

## Required Modules

```
requests, PyExecJS
```

## Usage

The generateiobb function can be used as follows:-

```
generateiobb("https://www.nike.com/launch/t/air-jordan-3-white-white/","http://user:pass@1.2.3.4:8080")
```

The first variable is the URL of the page where snare.js is being loaded, the second variable is the proxy.

## Update

I have added iOS device fingerprint generator. Its for Iovation iOS SDK version 4.3.0, the same one used in Nike's SNKRS iOS app. Currently the script has some pre-populated fields about the device that was used to generate a sample device id. Those fields are at the beginning of the script and should be changed according to the country and the device its supposed to imitate.

There is also detailed description of the information the fingerprint contains.