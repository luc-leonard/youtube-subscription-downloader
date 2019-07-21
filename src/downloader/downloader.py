from cache import cache
import feedparser
import youtube_dl
import string

class Downloader:
    def __init__(self, conf):
        self.conf = conf
        self.cache = cache.Cache(self.conf)

    def update(self):
        number_of_update = 0
        subscriptions_to_update = self.cache.getListOfSubscriptionToUpdate(self.conf.getListOfSubscriptions())
        print("sub to update ", subscriptions_to_update)
        feeds = {feed.title(): feedparser.parse("https://www.youtube.com/feeds/videos.xml?user=" + feed) for feed in subscriptions_to_update}
        for kv in feeds.items():
            feed = kv[1]
            print(kv[1])
            links_to_download = [entry.link for entry in feed.entries if self.cache.isDownloaded(entry.link) is False]
            print(links_to_download)
            with youtube_dl.YoutubeDL({
                'outtmpl': "./{0}/%(title)s.%(ext)s".format(kv[0])
            }) as ydl:
                ydl.download(links_to_download)
                self.cache.update(kv[0])
                number_of_update += 1
        return number_of_update > 0

    def destroy(self):
        self.cache.close()

def makeDownloader(conf):
    return Downloader(conf)
