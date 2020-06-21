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
# Change History   2010-10-01    Initial commit by @jsteiner207  2014-12-29    PEP8 update by @radzhome 2016-05-07    Update for Python3 by @jeremylow
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

class GetUserTwsClass:
    def __init__(self):
        self.fmt_nodash = '%Y%m%d%H%M%S'
        fmt_dash = '%F%H%M%S'
        self.dl = ' || '
        self.tweet_date_type = '%a %b %d %H:%M:%S +0000 %Y'  # incoming date - don't alter this line!
        dt = datetime.datetime.now()
        self.todays = dt.strftime(self.fmt_nodash)
        self.todays_dash = dt.strftime(fmt_dash)
        self.column_header = "\n - tweetid   ||    created_at        ||   screen_name   ||     tweet   \n"

    def get_fname(self, user_id):
        base_fnm = f'./RESULTS/USER/userTW-{user_id}-{self.todays}'
        # if ttype == 1:
        #     return f'{base_fnm}.json'
        # else:
        return f'{base_fnm}.txt'  # else return txt

    def get_title_line(self):
        title_base = "Nuls Tweets from @Nuls "
        return f'{title_base} - Today is {self.todays_dash}\n'

    def strip_emoji(self, text):
        re_emoji = re.compile(u'([\U000D000A])|([\U0000000D])|([\U0000000A])|([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
        return re_emoji.sub(r'', text)

    def tweets_to_csv(self, tweet_bundl, user_id):
        dl = self.dl
        title_line = self.get_title_line()
        print(title_line + self.column_header)
        fname_txt = self.get_fname(user_id)
        with open(fname_txt, 'w+', encoding='utf-8') as txt_file:
            txt_file.write(title_line)
            txt_file.write(self.column_header)
            for tweet_ob in tweet_bundl:
                jdict = tweet_ob.AsJsonString()
                status = json.loads(jdict)
                idstr = status.get('id_str')
                tw_created_at = strftime(self.fmt_nodash, strptime(status['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
                tweeter_name = status.get('user').get('screen_name')
                thetweet = self.strip_emoji(status.get('full_text')[0:280])
                the_line = f'{idstr}{dl}{tw_created_at}{dl}{tweeter_name}{dl}{thetweet}\n'
                txt_file.write(the_line)
                print(the_line, end='')


    def get_tweets(self, userid):
        api_obj = GetTapi.get_tapi()
        ttweets = api_obj.GetUserTimeline(userid, since_id=1272636436920111104)
        return ttweets

    def main(self, user):
        tweets_bundle = self.get_tweets(user)
        self.tweets_to_csv(tweets_bundle, user)


if __name__ == '__main__':
    myusers = [971524324141170688,
               1164168330904838146, 1107459040886571009, 1015486123450122240, 79102298, 1133787845192065024, 1133787841182425088, 396585013, 306739055, 290089377, 407788597, 352693203, 241336363,
               167153894, 276727820, 293257459, 263261764, 128636517, 107775453, 154033642, 425304459, 135274898, 157421261, 43344760, 30636454, 1159985647861424129, 1207489570071142400,
               1130426454234157056, 1105121244427386881, 1105122883288719361, 1130426485364277249, 1203883680571068417, 554172044, 1037947142629818369, 1037944449936945152, 1037941342012301312,
               1037931584890974208, 1037928961206964224, 1037925346987765761, 1037919088708730880, 1037913876514275329, 1037910560904425473, 1037905663463022592, 1037902081728819201,
               1037897738971566080, 1037894722516267013, 1037738265862758400, 1037734883525677057, 1037731967607820288, 1037727650469408768, 1037721453406244864, 1037617354845216770,
               1037610961438294016, 1102819391576563712, 1197174930804215808, 1273150633076494336, 16351738,
               1207488306373513216, 1157006171863052288, 1037607015713894402, 1037602820206161920, 1037570440842031106, 1241362535355494400, 4858661680, 1037565341893685248, 1037561581486333952,
               1037557963777486848, 1037554167919730693, 1037547460145500160, 1037545672189206529, 1134769316165849088, 1037543986104135681, 1037541548680830976, 1089561314844827648,
               1010415229451132929, 1010018707433590784, 1010403929161543680, 1010399222003142656, 1010391221599023104, 1010381475672256512, 1010376861132644354, 1010348209531547648,
               1010219201053655040, 1089552773551517697, 1010203348803321857, 1010196507943768064, 1010052388399415296, 1089547892820307968, 1010039181416910848, 1009838281905745920,
               995725024957939712, 976136880294002688, 985537756322410496, 985536239561408522, 997481488688992257, 985420002554597376, 985413001791528960, 985400676032368644, 985377925754073088,
               985365687341203457]

    tweet_obj = GetUserTwsClass()  # make the class object
    for i in myusers:
        tweet_obj.main(i)   # runnit
























# Nuls || uid: 912987663052836864
# Nuls || uid: 912987663052836864
# Nuls || uid: 912987663052836864




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

