#!/usr/bin/env python

import os
import subprocess
import time
import sys


def days_left(cert):
    if os.path.isfile(cert):
        try:
            end_date = subprocess.check_output(
                'openssl x509 -enddate -noout -in ' + cert, shell=True).replace('\n', '').split('=')[1]
            end_date_unix_time = subprocess.check_output(
                'date -d "' + end_date + '" +%s', shell=True).replace('\n', '')
        except subprocess.CalledProcessError:
            print 'ZBX_NOTSUPPORTED'
        days_left = (int(end_date_unix_time) - int(time.time())) / 86400
        if days_left < 0:
            print 0
        else:
            print days_left
    else:
        print 'ZBX_NOTSUPPORTED'


def main():
    cert_path = '/etc/letsencrypt/live/'
    cert = cert_path + sys.argv[-1:][0]+ '/cert.pem'
    days_left(cert)


if __name__ == '__main__':
    main()
