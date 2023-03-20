import snscrape.modules.twitter as sntwitter
import time, math

def searchTermsToString(search_terms):
    return '"'+'" OR "'.join(map(str, search_terms))+'"'
def scrape(task, session, prepStatement):
    searchString = f'{searchTermsToString(task["search_terms"])} since:{task["unix_start"]} until:{task["unix_end"]}'
    for amount,tweet in enumerate(sntwitter.TwitterSearchScraper(searchString).get_items()):
        values = [
            int(tweet.id),
            int(task["company"]),
            int(math.floor(time.mktime(tweet.date.timetuple())/86400)),
            int(time.mktime(tweet.date.timetuple())),
            str(tweet.rawContent),
            int(tweet.likeCount),
            int(tweet.replyCount),
            int(tweet.retweetCount)
        ]
        session.execute(prepStatement, values)
    return amount+1