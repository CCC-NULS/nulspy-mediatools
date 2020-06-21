#!/usr/bin/env python

# 6/20/2020: nms: original license - I'm too chicken to remove it so here it is:

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
# Change History  2010-10-01  Initial commit by @jsteiner207 2014-12-29   PEP8 update by @radzhome  2016-05-07  Update for Python3 by @jeremylow
# https://twitter.com/Nuls/status/

from __future__ import print_function
import json
import datetime
from time import strftime, strptime
import re
from get_tapi import GetTapi

# https://twitter.com/Nuls/status/1271030681896919042   june11 cryptocheckout
# https://twitter.com/Nuls/status/1271115644184989697   june11 questcapital partner
# 1271790310885076992   june13 which country
# 1271379579404455936   june13 pl


class RetweetsClass:
    def __init__(self):
        self.fmt_nodash = '%Y%m%d%H%M%S'
        fmt_dash = '%F%H%M%S'
        self.dl = ' || '
        self.tweet_date_type = '%a %b %d %H:%M:%S +0000 %Y'  # incoming date - don't alter this line!
        dt = datetime.datetime.now()
        self.todays = dt.strftime(self.fmt_nodash)
        self.todays_dash = dt.strftime(fmt_dash)
        self.column_header = "\n - tweetid   ||    created_at        ||   screen_name   ||     tweet   \n"

    def get_fname(self, base_tw, ttype=0):
        base_fnm = f'/home/Nancy/tweetdb/results/RETWEETS/RT-{base_tw}-{self.todays}'
        fpath = f'{base_fnm}.txt'  # else return txt
        if ttype == 1:
            fpath = f'{base_fnm}.json'
        return fpath

    def get_title_line(self, base_tweet):
        title_base = "Tweets to Nuls: Retweets of tweet # "
        return f'{title_base} {base_tweet} today is {self.todays_dash}\n'

    def strip_emoji(self, text):
        re_emoji = re.compile(u'([\U000D000A])|([\U0000000D])|([\U0000000A])|([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
        return re_emoji.sub(r'', text)

    def tweets_to_csv(self, tweet_bundl, base_tweet):
        dl = self.dl
        title_line = self.get_title_line(base_tweet)
        print(title_line + self.column_header)
        fname_txt = self.get_fname(base_tweet)
        with open(fname_txt, 'w+', encoding='utf-8') as txt_file:
            txt_file.write(title_line)
            txt_file.write(self.column_header)
            for tweet_ob in tweet_bundl:
                jdict = tweet_ob.AsJsonString()
                status = json.loads(jdict)
                idstr = status.get('id_str')
                tw_created_at = strftime(self.fmt_nodash, strptime(status['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
                tweeter_name = status.get('user').get('screen_name')
                thetweet = self.strip_emoji(status.get('full_text')[0:140])
                the_line = f'{idstr}{dl}{tw_created_at}{dl}{tweeter_name}{dl}{thetweet}\n'
                txt_file.write(the_line)
                print(the_line, end='')
            print()

    def tweets_to_json(self, tweet_bundle, base_tweet):
        fname = self.get_fname(base_tweet, 1)
        with open(fname, 'w+', encoding='utf-8') as fjson:
            for tweet in tweet_bundle:
                fjson.write(json.dumps(tweet._json))
                fjson.write('\n')

    def get_retweets(self, statusid):
        api_obj = GetTapi.get_tapi()
        retweets = api_obj.GetRetweets(statusid, count=200)
        return retweets

    # def GetRetweeters(self,  status_id,  cursor=None,  count=100,  stringify_ids=False):

    def main(self, base_tweet):
        retweets_bundle = self.get_retweets(base_tweet)
        self.tweets_to_json(retweets_bundle, base_tweet)
        self.tweets_to_csv(retweets_bundle, base_tweet)


if __name__ == '__main__':
    # june16 contest:  1272985780965838848

    #tweet_list = ["1272636436920111104"]   - contest done
    # mid june tweets we want retweets of
    # tweetid = "1272636436920111104"
    #tweet_list = ["1271790310885076992", "1271030681896919042", "1271115644184989697"]  # early june tweets we want retweets of
    #tweet_list = ["1272636436920111104", "1272644085405421568", "1272985780965838848", "1272985779321688066", "1271030681896919042"]   # mid june tweets we want retweets of

    #tweet_list = ["1272636436920111104", "1272644085405421568", "1272985780965838848", "1272985779321688066", "1271030681896919042"]   # mid june tweets we want retweets of
    # tweet_list = ["1271790310885076992"]  - contest poll - done
    tweet_list = ["1272985780965838848", "1272985779321688066"]

    tweet_obj = RetweetsClass()  # make the class object
    for tweetid in tweet_list:
        tweet_obj.main(tweetid)

