certbot & cloudflare ssl certificate (docker)
=====================================

forked from [mark86092/certbot-cloudflare-docker](https://github.com/mark86092/certbot-cloudflare-docker)

certbot not only provide web-based challenges, but also provide dns challenges for those
domains without a web hosting

this repo provide sample code for

**"How to abtain a ssl certificate from letsencrypt by dns challenge"** (use cloudflare api)

1. Get your cloudflare api key

2. run docker command

```sh
CF_END_POINT="https://api.cloudflare.com/client/v4/"
CF_AUTH_KEY="YOUR_CLOUDFLARE_AUTH_KEY"
CF_EMAIL="YOUR_CLOUDFLARE_EMAIL"

docker run -ti --rm \
    -e END_POINT="${CF_END_POINT}" \
    -e AUTH_KEY="${CF_AUTH_KEY}" \
    -e EMAIL="${CF_EMAIL}" \
    -v "$PWD/certs:/etc/letsencrypt" \
    a26007565/certbot-cloudflare-docker \
    certonly \
    --manual \
    --preferred-challenges dns \
    -d "{DOMAIN}" \
    -d "*.{DOMAIN}" \
    -m "{EMAIL}" \
    --manual-auth-hook /scripts/auth_hook.py \
    --manual-cleanup-hook /scripts/cleanup_hook.py \
    --manual-public-ip-logging-ok \
    --no-eff-email \
    --agree-tos
```

* all the command is the same as certbot/certbot