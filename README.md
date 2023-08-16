# rds
Update the Inovonics 732 Radio Data System Encoder with the currently playing program. 

You'll need to include the appropriate IP address in the file `ipaddress` located in the same directory as this script.

This script currently runs via cron twice an hour at 5 seconds past :00 and :30:
```
0,30 * * * * (perl -le 'sleep 5' && cd /home/dan/rds && ./rds.py) >/dev/null 2>&1
```
