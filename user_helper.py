import base64
import json

from flask import current_app, request


class UserHelper:
    @staticmethod
    def get_user():
        auth_enabled = current_app.config["auth_enabled"]

        if not auth_enabled:
            return current_app.config["test_user"]

        user_token = request.headers.get("X-Amzn-Oidc-Data")

        if user_token:
            payload = user_token.split(".")[1]
            decoded_payload = base64.b64decode(payload)
            decoded_json = json.loads(decoded_payload)

            return decoded_json["username"]

        return user_token
