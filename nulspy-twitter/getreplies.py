#!/home/Nancy/anaconda3/bin/python
# Copyright 2016 The Python-Twitter Developers
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
# Change History
# 2010-10-01 Initial commit by @jsteiner207  2014-12-29  PEP8 update by @radzhome 2016-05-07 Update for Python3 by @jeremylow
# May-June 2020 Nancy Schorr - reworked

from __future__ import print_function
import sys
import json
import datetime
from time import strftime, strptime
import re
from get_tapi import GetTapi
import get_tapi

# https://twitter.com/Nuls/status/1271030681896919042   june11 cryptocheckout
# https://twitter.com/Nuls/status/1271115644184989697   june11 questcapital partner


class RepliesObject:

    def __init__(self):
        self.todays = datetime.datetime.now().strftime('%Y-%m%d-%H%M%S')
        self.my_fmt = '%F%H%M%S'
        self.dl = ' || '
        self.lf = '\n'
        self.encode = 'utf-8'
        self.their_date_type = '%a %b %d %H:%M:%S +0000 %Y'  # incoming date - don't alter this line!
        self.headerline = f'To Nuls/Nerve - Replies \n'
        self.column_header = " - tweetid   ||    created_at        ||   userid    || screen_name   ||     tweet"
        self.nulsfnametxt = ''
        self.nervefnametxt = ''
        self.nervefnamejs = ''
        self.nulsfnamejs = ''

    def get_fnames(self):
        fnbase = f'Replies-{self.todays}'
        txdir = f'TXT/{fnbase}.txt'
        jsdir = f'JSON/{fnbase}.json'
        self.nulsfnametxt = f'/home/Nancy/tweetdb/results/NULS/{txdir}'
        self.nulsfnamejs = f'/home/Nancy/tweetdb/results/NULS/{jsdir}'
        self.nervefnametxt = f'/home/Nancy/tweetdb/results/NERVE/{txdir}'
        self.nervefnamejs = f'/home/Nancy/tweetdb/results/NERVE/{jsdir}'

    def strip_emoji(self, tline):
        re_emoji = re.compile(u'([\U000D000A])|([\U0000000D])|([\U0000000A])|([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
        return re_emoji.sub(r' ', tline)

    def tweets_to_csv(self, tweets, whoit=0):
        s = self
        fnametxt = self.nulsfnametxt
        if whoit == 1:
            fnametxt = self.nervefnametxt

        with open(fnametxt, 'w+', encoding=self.encode) as filenm:
            print(s.headerline + s.lf + s.column_header)
            filenm.write(s.headerline + s.lf + s.column_header + s.lf)
            for twt in tweets:
                status = json.loads(twt.AsJsonString())
                stat_id = status.get('id_str') + s.dl  # tweet id
                created = strftime(s.my_fmt, strptime(status['created_at'],  s.their_date_type)) + s.dl
                screen_name = status.get('user').get('screen_name') + s.dl
                user_id = str(status.get('user').get('id')) + s.dl
                thetweet = s.strip_emoji(status.get('full_text')[0:280]) + s.lf
                theline = f'{stat_id}{created}{user_id}{screen_name}{thetweet}{s.lf}'
                filenm.write(theline)
                print(theline)

    def tweets_to_json(self, repliz, whoit=0):
        fnamejson = self.nulsfnamejs
        if whoit == 1:
            fnamejson = self.nervefnamejs
        with open(fnamejson, 'w+', encoding='utf-8') as fjson:
            for tweet in repliz:
                fjson.write(json.dumps(tweet._json))
                fjson.write(self.lf)
        return

    def get_tweets(self, mycreds, whoit):
        # un_t = "2020-06-18"  sincedt = "2020-06-19"  sinceid = "1273404665720258561"  maxid = "1343283607818199040"
        name0 = "Nuls"
        name1 = "nerve_network"

        if whoit == 0:  # 0 = Nuls
            tweets = mycreds.GetSearch(term=name0, lang="en", count=100)
        elif whoit == 1:  # 1 = Nerve
            tweets = mycreds.GetSearch(term=name1, lang="en", count=100)

        print("tweets returned: " + str(len(tweets)))
        return tweets

    def main(self, whoit):
        api_obj = GetTapi.get_tapi()
        tw_results = self.get_tweets(api_obj, whoit)  # twitter api - tapi
        self.get_fnames()
        self.tweets_to_json(tw_results, whoit)
        self.tweets_to_csv(tw_results, whoit)


if __name__ == '__main__':
    tweet_objNuls = RepliesObject()  # make the class object for nuls
    tweet_objNuls.main(0)
    tweet_objNerve = RepliesObject()  # make the class object for nerve
    tweet_objNerve.main(1)


