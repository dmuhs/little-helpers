#!/usr/bin/env python3

import click
import urllib.request
import json
import sys


def get_data(ip):
    url = "http://geoip.nekudo.com/api/{}".format(ip)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read()
                              .decode()
                              .replace('false', '"unknown"')
                              .replace('null', '"unknown"'))
    if data.get('type') == 'error':
        click.echo('ERROR: ' + data['msg'])
        sys.exit(1)
    else:
        if 'unknown' in (data['city'], data['country']['name'], data['location']['time_zone']):
            data['location']['latitude'] = 'unknown'
            data['location']['longitude'] = 'unknown'
    return data


@click.command()
@click.argument('ip', default='')
def lookup(ip):
    data = get_data(ip)
    output = ("=== Lookup for {ip} ===\n"
              "Geolocation: {city}, {country} ({code})\n"
              "Position: {lat}, {long}\n"
              "Timezone: {tz}\n")

    click.echo(output.format(
        ip=data['ip'],
        city=data['city'],
        country=data['country']['name'],
        code=data['country']['code'],
        lat=data['location']['latitude'],
        long=data['location']['longitude'],
        tz=data['location']['time_zone']))

if __name__ == '__main__':
    lookup()
