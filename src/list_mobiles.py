#!/usr/bin/env python3

from gemuo.simple import simple_run

def run(client):
    for x in client.world.mobiles():
        print(x)

simple_run(run)
