#!/usr/bin/env python

import os


def main():
    cert_path = '/etc/letsencrypt/live/'
    domains_list = os.listdir(cert_path)
    data = ''
    count = 1
    for domain in domains_list:
        cert = cert_path + domain + '/cert.pem'
        if os.path.isfile(cert):
            if count == 1:
                data += '{"data": ['
            if not count == len(domains_list):
                data += '{"{#DOMAIN}": "' + domain + '"}, '
            else:
                data += '{"{#DOMAIN}": "' + domain + '"}]}'
            count += 1
    print data


if __name__ == '__main__':
    main()
