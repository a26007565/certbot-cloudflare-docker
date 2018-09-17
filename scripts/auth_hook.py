#!/usr/bin/env python

import requests
import json
import time
import cloudflare


if __name__ == '__main__':
    import sys
    import os

    domain = os.environ["CERTBOT_DOMAIN"]
    validation = os.environ["CERTBOT_VALIDATION"]

    zone_name = ".".join(domain.split(".")[-2:])
    zone = cloudflare.zone_selector(cloudflare.list_zones(zone_name))
    zone_id = zone["id"]

    print(cloudflare.create_dns_record(zone_id, "TXT", "_acme-challenge.{}".format(domain), validation))
    time.sleep(5)
