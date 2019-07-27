import json

class Configuration:

    def __init__(self, json_file):
        self.__dict__ = json.load(json_file)

    def getYoutubeRSSPath(self):
        return self.youtubeRSSPath

    def getListOfSubscriptions(self):
        return self.listOfSubscriptions

    def getDbPath(self):
        return self.dbPath

    def getPollingPeriodInMinutes(self):
        return self.pollingPeriodInMinutes

    def getOutputDir(self):
        return self.outputDir

    def getPlexUsername(self):
        return self.plexUsername

    def getPlexPassword(self):
        return self.plexPassword

    def getPlexServer(self):
        return self.plexServer

    def getPlexLibrary(self):
        return self.plexLibrary


def parseConfiguration(path_to_json_conf):
    with open(path_to_json_conf, 'r') as f:
        return Configuration(f)
