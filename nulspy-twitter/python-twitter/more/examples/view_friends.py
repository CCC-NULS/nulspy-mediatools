#!/usr/bin/env python

# Copyright 2016 The Python-Twitter Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ------------------------------------------------------------------------
# Change History
# 2010-10-01
#   Initial commit by @jsteiner207
#
# 2014-12-29
#   PEP8 update by @radzhome
#
# 2016-05-07
#   Update for Python3 by @jeremylow
#
#[Status(ID=1257940251500150785, ScreenName=nmschorr,
# Created=Wed May 06 07:48:22 +0000 2020,
# Text="RT @nerve_network: To celebrate the @Bitcoin halving event,
# we're giving away $NULS &amp;
# $NVT\n\nComplete the rules to participate\n\nRules:\n🔗 Fol…"),

from __future__ import print_function
import twitter



# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

# users = api.GetFriends()

myts = api.GetUserTimeline() #get tweets


# [Status(ID=1257940251500150785, ScreenName=nmschorr, Created=Wed May 06 07:48:22 +0000 2020, Text="RT @nerve_network: To celebrate the @Bitcoin halving event, we're giving away $NULS &amp; $NVT\n\nComplete the rules to participate\n\nRules:\n🔗 Fol…"),

# print([u.screen_name for u in users])
print([m for m in myts])
