#!/usr/bin/env python

from __future__ import print_function
import sys

sys.path.append(r'/home/Nancy/twitter/mks')
sys.path.append(r'/home/Nancy/twitter/nulspy-twitter/python-twitter')
import twitter
from mks import Mks  # nms private key for twitter info - not in project directory


class GetTapi:

    @staticmethod
    def get_tapi():
        mks = Mks().main()
        consumerkey = mks.get("ckey")
        consumersecret = mks.get("csecret")
        accesstoken_key = mks.get("atoken")
        accesstoken_secret = mks.get("asecret")
        tapi = twitter.Api(consumer_key=consumerkey,
                           consumer_secret=consumersecret,
                           access_token_key=accesstoken_key,
                           access_token_secret=accesstoken_secret)
        return tapi


