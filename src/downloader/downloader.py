from cache import cache
import feedparser
import youtube_dl
import string

class Downloader:
    def __init__(self, conf):
        self.conf = conf

    def update(self):
        theCache = cache.Cache()
        subscriptions_to_update = theCache.getListOfSubscriptionToUpdate(self.conf.getListOfSubscriptions())
        feeds = {feed.title(): feedparser.parse("https://www.youtube.com/feeds/videos.xml?user=" + feed) for feed in subscriptions_to_update}
        for kv in feeds.items():
            feed = kv[1]
            print(kv[1])
            links_to_download = [entry.link for entry in feed.entries if theCache.isDownloaded(entry.link) is False]
            print(links_to_download)
            with youtube_dl.YoutubeDL({
                'outtmpl': "./{0}/%(title)s.%(ext)s".format(kv[0])
            }) as ydl:
                ret_val = ydl.download(links_to_download[0:1])

def makeDownloader(conf):
    return Downloader(conf)
