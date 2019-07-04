import youtube_dl
import feedparser
import sys


def main():
    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for arg in sys.argv:
            feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?user=" + arg)
            ydl.download([entry.link for entry in feed.entries])


if __name__ == '__main__':
    main()
