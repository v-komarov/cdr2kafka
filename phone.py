#!/usr/bin/python
#coding:utf-8

import sys
import json
from kafka import KafkaProducer

### kafka
ka_host = ['10.6.0.88:9092']
producer = KafkaProducer(bootstrap_servers=ka_host)
queue = 'avaya'


while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    else:

        producer.send(queue, line)
        producer.flush()


