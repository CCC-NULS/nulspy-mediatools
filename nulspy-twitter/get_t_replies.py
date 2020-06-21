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
# 2010-10-01 Initial commit by @jsteiner207  2014-12-29  PEP8 update by @radzhome 2016-05-07 Update for Python3 by @jeremylow
#  May-June 2020 Nancy Schorr - reworked

from __future__ import print_function
import json
import datetime
from time import strftime, strptime
import re
from get_tapi import GetTapi

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
        self.nulsfnametxt = f'./RESULTS/REPLIES/NULS/{txdir}'
        self.nulsfnamejs = f'./RESULTS/REPLIES/NULS/{jsdir}'
        self.nervefnametxt = f'./RESULTS/REPLIES/NERVE/{txdir}'
        self.nervefnamejs = f'./RESULTS/REPLIES/NERVE/{jsdir}'

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
                theline = f'{stat_id}{created}{user_id}{screen_name}{thetweet}'
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






    # tweets = mycreds.GetSearch(term=name0, lang="en", max_id="1273293607818199042", count=100)
    # tweets = mycreds.GetSearch(term=name1, lang="en",  until=un_t, since=sincedt, count=100)
    #  include_rts:
    # tweet_timeline = api_data.GetSearch(raw_query="q=(plies&count=100")

    # GetUserTimeline(self, id=None, user_id=None, screen_name=None, since_id=None,
    # ct = 200
    # username = 'NULS'
    # screenm = 'Nuls'
    # userid = '912987663052836864'
    # sinceid = '1266350210168520705'  #first june 11 tweet

    # "q=from%3Acityofmentor%20since%3A2017-04-01%20until%3A2017-04-20"
    # "q=from%3Acityofmentor%20since%3A2017-04-01%20until%3A2017-04-20"
    #   strftime('%Y%m%d%H%M%S')

#   strftime('%F%H%M%S')

#  include_rts:

#     ttoday = datetime.datetime.now().strftime('%Y%m%d%H%M%S')


#when you fetch the tweet store the tweetId ie., id_str
# using twitter search api do the following query [q="to:$tweeterusername", sinceId = $tweetId]
# Loop all the results , the results matching the in_reply_to_status_id_str to $tweetid is the replies for the post.


# uname    screen_name  ||   uid
# NULS || Nuls || uid: 912987663052836864
# NULS || Nuls || uid: 912987663052836864

    # for tweetid in tweet_list:
    #     tweet_obj.main(tweetid, since, ct, today)

    # since=sinc, until=untl, count=ct, term=trm

    # def GetSearch(self,
    #   term=None,
    #   raw_query=None,
    #   geocode=None,
    #   since_id=None,
    #   max_id=None,
    #   until=None,
    #   since=None,
#   count=15,
#   lang=None,
#   locale=None,
#   result_type="mixed",
#   include_entities=None,
#   return_json=False):


# tweet_timeline = api_data.GetSearch(raw_query=qstr)
#     qstr = "to=Nuls&until=2020-06-13&since=2020-05-19&filter=replies&count=100"
#
#     qstr2 = "to=Nuls&until=2020-06-13&since=2020-05-19&filter=replies"
# api_data.GetSearch(raw_query='(to%3ANuls)%20min_replies%3A5%20min_faves%3A5%20until%3A2020-06-13%20since%3A2020-05-19%20filter%3Areplies&count=100')

# (to%3ANuls)%20min_replies%3A5%20min_faves%3A5%20until%3A2020-06-13%20since%3A2020-05-19%20filter%3Areplies&
# tweet_timeline = api_data.GetSearch(raw_query="q=(to=Nuls)&until=2020-06-13&since=2020-05-19&filter=replies&count=100")

# raw_query="q=twitter%20&result_type=recent&since=2020-05-19&count=200")
# q=(to=Nuls)&min_replies=5&min_faves=5&until=2020-06-13&since=2020-05-19&filter=replies&count=100"
# "q=(to=Nuls)&until=2020-06-13&since=2020-05-19&filter=replies&count=100"

# tweet_timeline = api_data.GetUserTimeline(screen_name=screen_name, count=200)

# since_id=None,
#                    count=None,
#                    max_id=None,
#                    trim_user=False)



# {"possibly_sensitive_appealable": false, "entities": {"user_mentions": [],
# "hashtags": [{"indices": [22, 29], "text": "amiibo"},
#            {"indices": [33, 41], "text": "Picross"}],
# "symbols": [], "urls": [{"display_url": "nintendo.com/games/detail/p\u2026",
# "url": "https://t.co/MjciohRcuW", "expanded_url": "http://www.nintendo.com/games/detail/picross-3d-round-2-3ds",
#                        "indices": [90, 113]}],
# "media": [{"type": "photo", "id": 778025997606105089,
#          "url": "https://t.co/ibou4buFxe",
#                                                                  "media_url": "http://pbs.twimg.com/media/CswaoY4UAAA8-Zj.jpg",
#            "indices": [114, 137], "id_str": "778025997606105089", "display_url": "pic.twitter.com/ibou4buFxe", "expanded_url":
#                "https://twitter.com/NintendoAmerica/status/778307811012780032/video/1",
#            "sizes": {"large": {"resize": "fit", "w": 1280, "h": 720}, "small": {"resize": "fit", "w": 680, "h": 383}, "thumb": {"resize": "crop", "w": 150, "h": 150}, "medium": {"resize": "fit", "w": 1200, "h": 675}}, "media_url_https": "https://pbs.twimg.com/media/CswaoY4UAAA8-Zj.jpg"}]}, "extended_entities": {"media": [{"id": 778025997606105089, "url": "https://t.co/ibou4buFxe", "media_url": "http://pbs.twimg.com/media/CswaoY4UAAA8-Zj.jpg", "video_info": {"duration_millis": 62996, "aspect_ratio": [16, 9], "variants": [{"bitrate": 320000, "url": "https://video.twimg.com/amplify_video/778025997606105089/vid/320x180/5Qr0z_HeycC2DvRj.mp4", "content_type": "video/mp4"}, {"bitrate": 2176000, "url": "https://video.twimg.com/amplify_video/778025997606105089/vid/1280x720/mUiy98wFwECTRNxT.mp4", "content_type": "video/mp4"}, {"bitrate": 832000, "url": "https://video.twimg.com/amplify_video/778025997606105089/vid/640x360/SX_HepRw0MeH796L.mp4", "content_type": "video/mp4"}, {"url": "https://video.twimg.com/amplify_video/778025997606105089/pl/PX7Gx8TRhJyUZ2-L.m3u8", "content_type": "application/x-mpegURL"}, {"url": "https://video.twimg.com/amplify_video/778025997606105089/pl/PX7Gx8TRhJyUZ2-L.mpd", "content_type": "application/dash+xml"}]}, "ext_alt_text": null, "sizes": {"large": {"resize": "fit", "w": 1280, "h": 720}, "small": {"resize": "fit", "w": 680, "h": 383}, "thumb": {"resize": "crop", "w": 150, "h": 150}, "medium": {"resize": "fit", "w": 1200, "h": 675}}, "indices": [114, 137], "type": "video", "additional_media_info": {"title": "Picross 3D Round 2 - amiibo \"Hands-On\u201d Gameplay ", "description": "Unlock more puzzles in Picross 3D Round 2 with amiibo!", "call_to_actions": {"visit_site": {"url": "http://www.nintendo.com/games/detail/picross-3d-round-2-3ds"}}, "monetizable": false, "embeddable": true}, "id_str": "778025997606105089", "display_url": "pic.twitter.com/ibou4buFxe", "expanded_url": "https://twitter.com/NintendoAmerica/status/778307811012780032/video/1", "media_url_https": "https://pbs.twimg.com/media/CswaoY4UAAA8-Zj.jpg"}]}, "favorited": false, "text": "Puzzled on how to use #amiibo in #Picross 3D Round 2? Just follow these six simple steps!\nhttps://t.co/MjciohRcuW https://t.co/ibou4buFxe", "retweeted": false, "retweet_count": 119, "user": {"is_translator": false, "profile_image_url_https": "https://pbs.twimg.com/profile_images/745752686780387333/wsjpSx2K_normal.jpg", "url": "https://t.co/cMLmFbyXaL", "entities": {"description": {"urls": [{"display_url": "esrb.org", "url": "https://t.co/OgSR65P8OY", "expanded_url": "http://esrb.org", "indices": [103, 126]}]}, "url": {"urls": [{"display_url": "nintendo.com", "url": "https://t.co/cMLmFbyXaL", "expanded_url": "http://www.nintendo.com/", "indices": [0, 23]}]}}, "listed_count": 10347, "friends_count": 1350, "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/623621309210083328/e9ZICp8d.jpg", "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/623621309210083328/e9ZICp8d.jpg", "profile_use_background_image": true, "profile_link_color": "038543", "description": "Welcome to the official Nintendo profile for gaming news! We\u2019re listening, too. For ESRB ratings go to https://t.co/OgSR65P8OY", "favourites_count": 260, "protected": false, "profile_background_tile": false, "id_str": "5162861", "has_extended_profile": false, "profile_text_color": "333333", "verified": true, "follow_request_sent": false, "contributors_enabled": false, "lang": "en", "id": 5162861, "statuses_count": 11909, "notifications": false, "location": "", "created_at": "Wed Apr 18 22:43:15 +0000 2007", "name": "Nintendo of America", "is_translation_enabled": false, "default_profile_image": false, "profile_background_color": "ACDED6", "utc_offset": -25200, "geo_enabled": false, "profile_banner_url": "https://pbs.twimg.com/profile_banners/5162861/1476972565", "profile_sidebar_border_color": "FFFFFF", "screen_name": "NintendoAmerica", "profile_sidebar_fill_color": "F6F6F6", "profile_image_url": "http://pbs.twimg.com/profile_images/745752686780387333/wsjpSx2K_normal.jpg", "default_profile": false, "time_zone": "Pacific Time (US & Canada)", "followers_count": 5246308, "translator_type": "none", "following": false}, "id_str": "778307811012780032", "is_quote_status": false, "in_reply_to_status_id": null, "in_reply_to_status_id_str": null, "contributors": null, "id": 778307811012780032, "favorite_count": 609, "in_reply_to_screen_name": null, "geo": null, "created_at": "Tue Sep 20 19:00:17 +0000 2016", "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>", "truncated": false, "lang": "en", "in_reply_to_user_id_str": null,
#  "place": null, "coordinates": null, "in_reply_to_user_id": null, "possibly_sensitive": false}

# Nancy Schorr, [07.06.20 04:37]
# here the retweets from the company count guess:
# https://twitter.com/Nuls/status/1266350210168520705/retweets/without_comments
    # uname = userr.get('name')
    # userr = status.get('user')

# a = api.GetUserRetweets(1)
# user.name, screen_name, id_str, created_at, Text
#
# print(m.id_str + ' || ' + m.created_at + ' || ' + m.user.name + ' || ' + m.screen_name + ' || ' + m.Text + '\n')


# myts = api.GetUserTimeline()
# 1266350210168520705
# retweets = api.GetRetweets(statusid='1257940251500150785')
# https://twitter.com/search?q=%40nerve_network%20To%20celebrate%20the%20%40Bitcoin%20halving%20event&src=typed_query


# [Status(ID=1257940251500150785, ScreenName=nmschorr, Created=Wed May 06 07:48:22 +0000 2020,
# Text="RT @nerve_network: To celebrate the @Bitcoin halving event, we're giving away $NULS &amp; $NVT\n\nComplete the rules to participate\n\nRules:\n🔗 Fol…"),


# retweets = api.GetRetweets(statusid='1266350210168520705',
# print([u.screen_name for u in users])
# for m in retweets:
#     print(m, '\n')

# june 11 tweet https://twitter.com/Nuls/status/1271115644184989697

