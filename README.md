# zabbix_letsencrypt

Zabbix template for letsencrypt certificates monitoring.

## Version 2019-04-30
- Ignore files in cert folder (0.32 certbot puts a readme file in that folder)


## Version 2019-01-22
- Added support to detect certbot version
- Trigger when certbot version below 0.28

## System requirements

- python
 
## Install

Don't forget change paths:

1. Copy sudo permissions ```cp -r ./zabbix_letsencrypt/conf/zabbix_letsencrypt /etc/sudoers.d/```

2. Copy scripts: ```cp -r ./zabbix_letsencrypt/scripts/letsencrypt /etc/zabbix/scripts/```

3. Copy zabbix conf: ```cp -r ./zabbix_letsencrypt/conf/letsencrypt.conf /etc/zabbix/zabbix_agent.d/```

4. Restart zabbix agent: ```/etc/init.d/zabbix_agent restart```

5. Import template to Zabbix web.
