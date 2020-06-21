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
        base_fnm = f'./RESULTS/RETWEETS/nulsRT-{base_tw}-{self.todays}'
        if ttype == 1:
            return f'{base_fnm}.json'
        else:
            return f'{base_fnm}.txt'  # else return txt

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
    #tweet_list = ["1272636436920111104"]   - contest done
    # mid june tweets we want retweets of
    # tweetid = "1272636436920111104"
    #tweet_list = ["1271790310885076992", "1271030681896919042", "1271115644184989697"]  # early june tweets we want retweets of
    #tweet_list = ["1272636436920111104", "1272644085405421568", "1272985780965838848", "1272985779321688066", "1271030681896919042"]   # mid june tweets we want retweets of

    #tweet_list = ["1272636436920111104", "1272644085405421568", "1272985780965838848", "1272985779321688066", "1271030681896919042"]   # mid june tweets we want retweets of
    # tweet_list = ["1271790310885076992"]  - contest poll - done
    tweet_list = ["1272985780965838848"]

    tweet_obj = RetweetsClass()  # make the class object
    for tweetid in tweet_list:
        tweet_obj.main(tweetid)






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

