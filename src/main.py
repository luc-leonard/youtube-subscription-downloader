from config import config
from downloader import downloader
import time
from plexapi.myplex import MyPlexAccount


def main():
    conf = config.parseConfiguration("./config.json")
    the_downloader = downloader.makeDownloader(conf)
    account = MyPlexAccount(conf.getPlexUsername(), conf.getPlexPassword())
    plex = account.resource(conf.getPlexServer()).connect()
    movies = plex.library.section(conf.getPlexLibrary())

    while True:
        number_of_upload = the_downloader.update()
        if number_of_upload > 0:
            movies.update()
        time.sleep(conf.getPollingPeriodInMinutes() * 60)

    the_downloader.destroy()


if __name__ == '__main__':
    main()
