import twint
import re
import datetime

class TwintSearch(object):

    def __init__(self):
        self.fmt_nodash = '%Y%m%d%H%M%S'
        fmt_dash = '%F%H%M%S'
        self.dl = ' || '
        self.tweet_date_type = '%a %b %d %H:%M:%S +0000 %Y'  # incoming date - don't alter this line!
        dt = datetime.datetime.now()
        self.todays = dt.strftime(self.fmt_nodash)
        self.todays_dash = dt.strftime(fmt_dash)
        self.column_header = "\n - tweetid   ||    created_at        ||   screen_name   ||     tweet   \n"
        self.fname = f'nulsRT-{self.todays}.txt'


    def strip_emoji(self, text):
        re_emoji = re.compile(u'([\U000D000A])|([\U0000000D])|([\U0000000A])|([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
        return re_emoji.sub(r'', text)

    def get_followers(self):
        c = twint.Config()
        c.Store_csv = True
        # c.Store_object = True
        # c.Since = '2020-06-14 00:00:01'
        c.Limit = 29999
        c.Username = "noneprivacy"
        # conf_obj.Custom["tweet"] = ["id"]
        c.Custom["user"] = ["Nuls"]
        c.Custom["user_id"] = [ 912987663052836864 ]

        # conf_obj.Limit = 4
        # conf_obj.Retweets = True

        # conf_obj.Replies = True
        twint.run.Followers(c)
        followers = twint.output.users_list

        k_followers = []

        for user in followers:
            k_followers.append(user)
            print(user)

        with open(f'Followers-{self.fmt_nodash}.csv', 'w+') as output:
            output.write('id, username, followers, following\n')
            for u in k_followers:
                try:
                    output.write('{},{},{},{}\n'.format(u.id, u.username, u.followers, u.following))
                except UnicodeEncodeError:
                    u = self.strip_emoji(u)
                    output.write('{},{},{},{}\n'.format(u.id, u.username, u.followers, u.following))
                    pass


if __name__ == "__main__":
    tw_obj = TwintSearch()
    tw_obj.get_followers()


# https://twitter.com/Nuls/status/1271030681896919042   june11 cryptocheckout
# https://twitter.com/Nuls/status/1271115644184989697   june11 questcapital partner

# nulsid: 912987663052836864

#    twint -s "Nuls" --since 2020-06-14 --hashtag "NULS"




# best for csv: use this = remove linefeeds  \r\n  -- ck 1st for ||  use () instead if necessary
#                     output.write('|| {} || {} || {} || {} || {} || {} ^^'.format(u.id_str, u.datestamp, u.timestamp, u.username, u.name, u.tweet))
#To celebrate the #@Bitcoin # halving event, we're giving away

# to tweet
    # t = tweet()
    # t.id = int(tw["data-item-id"])
    # t.id_str = tw["data-item-id"]
    # t.conversation_id = tw["data-conversation-id"]
    # t.datetime = int(tw.find("span", "_timestamp")["data-time-ms"])
    # # t.datestamp = strftime("%Y-%m-%d", localtime(t.datetime / 1000.0))
    # # t.timestamp = strftime("%H:%M:%S", localtime(t.datetime / 1000.0))
    # t.user_id = int(tw["data-user-id"])
    # c.Custom["tweet"] = "1255605100715937792"

    # twint.run.Search(tw_obj)



# with open('K_followers.csv', 'w') as output:
#     output.write('id,username,followers, following\n')
#
#
#
#     output.write('id,username,followers, following\n')
#     for u in K_followers:
#         output.write('{},{},{},{}\n'.format(u.id, u.username, u.followers, u.following))
#

# GET https://api.twitter.com/1.1/statuses/retweets/1255605100715937792.json
#
# str:
# if `tweet.tweet_type == "retweet"`, returns an empty string













# https://pielco11.ovh/posts/twint-osint/#before-to-start
# https://pielco11.ovh/posts/twint-osint/#before-to-start

# c.Custom["tweet"] = ["id"]
# c.Custom["user"] = ["bio"]
# c.Limit = 3
# c.Store_csv = True
#
# c.Output = "./nulssearch.csv"
# c.Custom["tweet"] = "1255605100715937792"

# c.Since = "2020-4-21 20:30:22"
# c.Until = "2020-5-6"
# # c.Min_retweets = "100"
# c.Search = "nerve_network"
# c.Retweets = 'all'

# -- new:
# c.Custom_csv = ["id", "user_id", "username", "tweet"]

# c.Lang = "en"
# c.Translate = True
# c.TranslateDest = "it"
# u.following = stat(ur, "following")
# t.retweet_id = ''
# t.retweets_count = getStat(tw, "retweet")
# t.likes_count = getStat(tw, "favorite")
# t.link = f"https://twitter.com/{t.username}/status/{t.id}"
# t.user_rt_id, t.user_rt = getRetweet(tw, config)
# t.retweet = True if t.user_rt else False
# t.retweet_id = ''
# t.retweet_date = ''
# logme.debug(__name__ + ':User')
# u = user()
# for img in ur.findAll("img", "Emoji Emoji--forText"):
#     img.replaceWith(img["alt"])
# u.id = inf(ur, "id")
# u.name = inf(ur, "name")
# u.username = inf(ur, "username")
# u.bio = card(ur, "bio")
# u.location = card(ur, "location")
# u.url = card(ur, "url")
# u.join_date = join(ur)[1]
# u.join_time = join(ur)[0]
# u.tweets = stat(ur, "tweets is-active")
# u.following = stat(ur, "following")
# u.followers = stat(ur, "followers")
# u.likes = stat(ur, "favorites")
# u.media_count = media(ur)
# u.is_private = inf(ur, "private")
# u.is_verified = verified(ur)
# u.avatar = ur.find("img", "ProfileAvatar-image")["src"]
# u.background_image = ur.find('div', {'class': 'ProfileCanopy-headerBg'}).find('img').get('src')



#
#
# """Create Tweet object
#    """
# logme.debug(__name__ + ':Tweet')
# t = tweet()
# t.id = int(tw["data-item-id"])
# t.id_str = tw["data-item-id"]
# t.conversation_id = tw["data-conversation-id"]
# t.datetime = int(tw.find("span", "_timestamp")["data-time-ms"])
# t.datestamp = strftime("%Y-%m-%d", localtime(t.datetime / 1000.0))
# t.timestamp = strftime("%H:%M:%S", localtime(t.datetime / 1000.0))
# t.user_id = int(tw["data-user-id"])
# t.user_id_str = tw["data-user-id"]
# t.username = tw["data-screen-name"]
# t.name = tw["data-name"]
# t.place = tw.find("a", "js-geo-pivot-link").text.strip() if tw.find("a", "js-geo-pivot-link") else ""
# t.timezone = strftime("%Z", localtime())
# for img in tw.findAll("img", "Emoji Emoji--forText"):
#     img.replaceWith(img["alt"])
# t.mentions = getMentions(tw)
# t.urls = [link.attrs["data-expanded-url"] for link in tw.find_all('a', {'class': 'twitter-timeline-link'}) if link.has_attr("data-expanded-url")]
# t.photos = [photo_node.attrs['data-image-url'] for photo_node in tw.find_all("div", "AdaptiveMedia-photoContainer")]
# t.video = 1 if tw.find_all("div", "AdaptiveMedia-video") != [] else 0
# t.tweet = getText(tw)
# t.hashtags = [hashtag.text for hashtag in tw.find_all("a", "twitter-hashtag")]
# t.cashtags = [cashtag.text for cashtag in tw.find_all("a", "twitter-cashtag")]
# t.replies_count = getStat(tw, "reply")
# t.retweets_count = getStat(tw, "retweet")
# t.likes_count = getStat(tw, "favorite")
# t.link = f"https://twitter.com/{t.username}/status/{t.id}"
# t.user_rt_id, t.user_rt = getRetweet(tw, config)
# t.retweet = True if t.user_rt else False
# t.retweet_id = ''
# t.retweet_date = ''
# if not config.Profile:
#     t.retweet_id = tw['data-retweet-id'] if t.user_rt else ''
#     t.retweet_date = datetime.fromtimestamp(((int(t.retweet_id) >> 22) + 1288834974657) / 1000.0).strftime("%Y-%m-%d %H:%M:%S") if t.user_rt else ''
# t.quote_url = getQuoteURL(tw)
# t.near = config.Near if config.Near else ""
# t.geo = config.Geo if config.Geo else ""
# t.source = config.Source if config.Source else ""
# t.reply_to = [{'user_id': t['id_str'], 'username': t['screen_name']} for t in json.loads(tw["data-reply-to-users-json"])]
# t.translate = ''
# t.trans_src = ''
# t.trans_dest = ''
#
#
