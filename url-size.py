#!/usr/bin/env python3

import click
import sys
from urllib.error import HTTPError
import urllib.request


def human_readable(n):
    for u in ['','KB','MB','GB','TB','PB']:
        if abs(n) < 1000.0:
            return str(round(n, 2)) + u
        n /= 1024.0
    return None


def url_size(url):
    try:
        u = urllib.request.urlopen(url)
        return int(u.getheader('Content-Length'))
    except (ValueError, HTTPError):
        click.echo('Invalid URL or 404. :(')
        sys.exit(1)

@click.command()
@click.argument('url')
def main(url):
    size = human_readable(url_size(url))
    if size:
        click.echo(size)
    else:
        click.echo('The file is bigger than one PB. What are you doing!?')


if __name__ == '__main__':
    main()
