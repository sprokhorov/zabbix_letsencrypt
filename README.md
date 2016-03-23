# zabbix_letsencrypt

Zabbix template for letsencrypt certificates monitoring.

## System requirements

- python
 
## Install

Don't forget change paths:

1. Edit `/etc/sudoers` and add this line: ```zabbix  ALL=(ALL:ALL) NOPASSWD:ALL```

2. Copy scripts: ```cp -r ./zabbix_letsencrypt/scripts/letsencrypt /etc/zabbix/scripts/```

3. Copy zabbix conf: ```cp -r ./zabbix_letsencrypt/conf/letsencrypt.conf /etc/zabbix/zabbix_agent.d/```

4. Restart zabbix agent: ```/etc/init.d/zabbix_agent restart```

5. Import template to Zabbix web.
