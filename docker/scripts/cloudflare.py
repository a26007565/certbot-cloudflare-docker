import requests
import json
import os

END_POINT = os.environ["END_POINT"]
AUTH_KEY = os.environ["AUTH_KEY"]
EMAIL = os.environ["EMAIL"]


def list_zones(hint_domain):
    headers = {
        "X-Auth-Key": AUTH_KEY,
        "X-Auth-Email": EMAIL,
    }
    params = {
        "name": hint_domain,
    }

    r = requests.get("{}zones".format(END_POINT), headers=headers, params=params)
    return r.json()


def create_dns_record(zone_id, dns_type, name, content):
    headers = {
        "X-Auth-Key": AUTH_KEY,
        "X-Auth-Email": EMAIL,
    }
    data = {
        "type": dns_type,
        "name": name,
        "content": content,
    }

    r = requests.post("{}zones/{}/dns_records".format(END_POINT, zone_id), headers=headers, data=json.dumps(data))
    return r.json()


def list_dns_records(zone_id, dns_type, name):
    headers = {
        "X-Auth-Key": AUTH_KEY,
        "X-Auth-Email": EMAIL,
    }
    params = {
        "type": dns_type,
        "name": name,
    }

    r = requests.get("{}zones/{}/dns_records".format(END_POINT, zone_id), headers=headers, params=params)
    return r.json()


def delete_dns_record(zone_id, dns_record_id):
    headers = {
        "X-Auth-Key": AUTH_KEY,
        "X-Auth-Email": EMAIL,
    }

    r = requests.delete("{}zones/{}/dns_records/{}".format(END_POINT, zone_id, dns_record_id), headers=headers)
    return r.json()


def zone_selector(response):
    return response["result"][0]


def dns_record_selector(response):
    return response["result"][0]
