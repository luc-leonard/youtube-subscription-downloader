import sqlite3
from datetime import datetime


class Cache:
    def __init__(self, conf):
        self.db = sqlite3.connect(conf.getDbPath())
        self.duration_between_refresh = conf.getPollingPeriodInMinutes() * 60
        cursor = self.db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS subscription_status (id varchar(255) primary key, last_updated timestamp)")
        cursor.execute("SELECT * FROM subscription_status")
        result = cursor.fetchall()
        cursor.close()
        print(result)

    def getListOfSubscriptionToUpdate(self, subscription_list):
        return [sub for sub in subscription_list if self.shouldUpdate(sub)]

    def shouldUpdate(self, subscribtion_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT last_updated FROM subscription_status WHERE id LIKE ?", [subscribtion_id])
        result = cursor.fetchone()
        if result is None:
            return True
        delay = datetime.now() - datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S.%f')
        return delay.seconds > self.duration_between_refresh

    def update(self, subscription_id):
        cursor = self.db.cursor()
        cursor.execute("REPLACE INTO subscription_status (id, last_updated) VALUES(?, ?)", [subscription_id, datetime.now()])
        cursor.close()
        self.db.commit()

    def isDownloaded(self, video_id):
        return False

    def close(self):
        self.db.close()


def makeCache(configuration):
    return Cache(configuration)
