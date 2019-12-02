#!/usr/bin/env python
# coding: utf-8

import sys
import os
import logging
import click
import subprocess
import django

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()

log = logging.getLogger(__name__)


@click.group()
def main():
    pass


@main.command()
def mm():
    """make migration and migrate it."""
    click.secho('make migrations...', fg='yellow')
    subprocess.call('python src/manage.py makemigrations', shell=True)
    click.secho('migrate...', fg='yellow')
    subprocess.call('python src/manage.py migrate', shell=True)


if __name__ == '__main__':
    main()
