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