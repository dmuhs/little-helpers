# little-helpers
Some small helper scripts I hacked up in my day to day business.

## Requirements
All Python scripts run on Python 3, because you should let Python 2.x die already and move on with your life. To provide a sweet cli and avoid any pesky argparse code I use `click`. Simply install it by running `pip3 install click`.

### geoip.py
Looks up the location data (if available) for any valid IPv4 or IPv6 address using the [nekudo geolocation API](http://geoip.nekudo.com/).
