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

    dns_record = cloudflare.dns_record_selector(cloudflare.list_dns_records(zone_id, "TXT", "_acme-challenge.{}".format(domain)))
    dns_record_id = dns_record["id"]

    print(cloudflare.delete_dns_record(zone_id, dns_record_id))
    time.sleep(5)
