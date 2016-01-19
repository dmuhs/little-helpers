# little-helpers
Some small helper scripts I hacked up in my day to day business.

## Requirements
All Python scripts run on Python 3, because you should let Python 2.x die already and move on with your life. To provide a sweet cli and avoid any pesky argparse code I use [click](http://click.pocoo.org/). Simply install it by running `pip3 install click`.

### geoip.py
Looks up the location data (if available) for any valid IPv4 or IPv6 address using the [nekudo geolocation API](http://geoip.nekudo.com/).

### docker-clean.sh
Removes all docker containers shown in `docker ps -a` that are **currently not running** and newline-separatedly outputs their IDs. Example:
```bash
$ docker ps -a
CONTAINER ID        IMAGE                COMMAND             CREATED             STATUS                     PORTS               NAMES
ecffc300d8a3        hello-world:latest   "/hello"            6 seconds ago       Exited (0) 6 seconds ago                       lonely_stallman     
c7ed3897180f        hello-world:latest   "/hello"            7 seconds ago       Exited (0) 6 seconds ago                       fervent_banach      
7f59c19a3e50        hello-world:latest   "/hello"            7 seconds ago       Exited (0) 6 seconds ago                       prickly_goldstine   
$ ./docker-clean.sh
ecffc300d8a3
c7ed3897180f
7f59c19a3e50
```
