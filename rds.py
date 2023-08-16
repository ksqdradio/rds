#!/usr/bin/env python

import pandas as pd
import sqlalchemy
import telnetlib

now = pd.Timestamp.now(tz="US/Pacific")  # .tz_convert('utc')
print(now)

DEFAULT_DPSTR = "KSQD 90.7 FM, 89.7 FM, 89.5 FM, and ksqd.org"

try:
    df = pd.read_sql_query(
        f"select * from shows where start < datetime('{now}') and end > datetime('{now}') order by start",
        "sqlite:///../twoweekarchive/shows.db",
    )
    if len(df) > 0:
        dpsstr = f"{df['title'][0]} on {DEFAULT_DPSTR}"
    else:
        print("sql query did not receive valid results; falling back to default")
        dpsstr = DEFAULT_DPSTR
except sqlalchemy.exc.OperationalError:
    print("invalid sql query; falling back to default")
    dpsstr = DEFAULT_DPSTR

print(dpsstr)

with open("ipaddress") as f:
    ip = f.read().strip()

tn = telnetlib.Telnet(ip, port=10001, timeout=10)
tn.write(f"DPS={dpsstr}\r\n".encode("latin_1"))
try:
    response = tn.read_until(b"OK", timeout=10)
except EOFError as e:
    print(f"Connection closed: {e}")

print(response)
tn.close()
