class Configuration:

    def getYoutubeRSSPath(self):
        return "https: // www.youtube.com / feeds / videos.xml?user ="

    def getListOfSubscriptions(self):
        return ['joueurdugrenier']

    def getDbPath(self):
        return "ysd.db"

    def getPollingPeriodInMinutes(self):
        return 10


def parseConfiguration(path_to_json_conf):
    return Configuration()
