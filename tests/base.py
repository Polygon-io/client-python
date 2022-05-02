from polygon import RESTClient

import os
import unittest
import httpretty  # type: ignore

# mocks are stored in file tree
mocks = []
dirname = os.path.dirname(__file__)
mockdir = os.path.join(dirname, "mocks")
for dname, _, files in os.walk(mockdir):
    for fname in files:
        if fname.endswith(".json"):
            abspath = os.path.join(dname, fname)
            with open(abspath, "r") as f:
                urllpath = abspath.replace(mockdir, "").replace(".json", "")
                mocks.append((urllpath, f.read()))

unittest.util._MAX_LENGTH = 30000  # type: ignore


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.c = RESTClient("", verbose=True)
        httpretty.enable(verbose=True, allow_net_connect=False)
        for m in mocks:
            url = cls.c.BASE + m[0]
            # print('register', url)
            httpretty.register_uri(httpretty.GET, url, m[1], match_querystring=True)
