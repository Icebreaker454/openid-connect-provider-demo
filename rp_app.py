from uuid import uuid4
from urllib.parse import urlencode
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/test_auth")
def authenticate_via_provider():

    global state
    state = uuid4().hex
    identity_domain = "http://localhost:9090"
    scope = "openid email profile"
    response_type = "code"
    redirect_uri = "http://localhost:5000/test_auth_callback"

    params = {
        "scope": scope,
        "response_type": response_type,
        "client_id": "sample",
        "client_secret": "sample",
        "state": state,
        "redirect_uri": redirect_uri,
    }

    context = {"auth_url": f"{identity_domain}/authorize?{urlencode(params)}"}

    return render_template("login.jinja2", **context)


@app.route("/test_auth_callback")
def callback_openid():
    return render_template("callback.jinja2", code=request.args.get("code"))
