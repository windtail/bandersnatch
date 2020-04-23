# coding: utf-8
import re
from configparser import ConfigParser


class Urls:
    def __init__(self, package=None):
        self.package = package


_urls = Urls()


def config_alternative(config: ConfigParser):
    _urls.package = config.get("mirror", "master_package", fallback=None)


def alter(url):
    if re.match(r'^https?://[^/]+/packages/', url):
        if _urls.package is not None:
            return re.sub(r'^https?://[^/]+', _urls.package, url, count=1), True

    return url, False
