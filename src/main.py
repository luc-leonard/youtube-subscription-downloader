
from config import config
from downloader import downloader

def main():
    conf = config.parseConfiguration("./config.json")
    the_downloader = downloader.makeDownloader(conf)
    the_downloader.update()


if __name__ == '__main__':
    main()
