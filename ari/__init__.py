"""ARI client library
"""

import ari.client
import swaggerpy.http_client
from urllib.parse import urlsplit

Client = client.Client


def connect(base_url, username, password):
    """Helper method for easily connecting to ARI.

    :param base_url: Base URL for Asterisk HTTP server (http://localhost:8088/)
    :param username: ARI username
    :param password: ARI password.
    :return:
    """
    split = urlsplit(base_url)
    http_client = swaggerpy.http_client.SynchronousHttpClient()
    http_client.set_basic_auth(split.hostname, username, password)
    return Client(base_url, http_client)
