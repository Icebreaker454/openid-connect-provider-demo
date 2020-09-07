# Introduction
This is an example OpenID connect 1.0 provider for Flask.

# Features
* OpenID configuration via `/.well-known/openid-configuration` endpoint

# How to run
## Identity provider
To run the example identity provider (OP), execute the following commands:

```bash
pip install -r requirements.txt # install the dependencies
gunicorn wsgi:app -b :9090
```

Note that you will have to change the default `9090` port in the `application.cfg` as well
in case you want to change the ports
