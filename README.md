# rds
Update the Inovonics 732 Radio Data System Encoder with the currently playing program. 

You'll need to include the appropriate IP address in the file `ipaddress` located in the same directory as this script.

This script currently runs via cron twice an hour at :01 and :31:
```
1,31 * * * * cd /home/dan/rds && ./rds.py
```
