import sqlite3

class Cache:

    def getListOfSubscriptionToUpdate(self, subscription_list):
        return [sub for sub in subscription_list if self.shouldUpdate(sub)]

    def shouldUpdate(self, subscribtion_id):
        return True

    def isDownloaded(self, video_id):
        return False


def makeCache(configuration):
    return Cache()
