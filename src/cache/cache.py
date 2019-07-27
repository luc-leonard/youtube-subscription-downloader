import sqlite3
from datetime import datetime


class Cache:
    def __init__(self, conf):
        self.db = sqlite3.connect(conf.getDbPath())
        self.duration_between_refresh = conf.getPollingPeriodInMinutes() * 60
        cursor = self.db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS subscription_status (id varchar(255) primary key, last_updated timestamp)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS downloaded_videos (id varchar(255) primary key, last_updated timestamp)")
        cursor.execute("SELECT * FROM subscription_status")
        result = cursor.fetchall()
        cursor.close()
        print("result", result)

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

    def setDownloaded(self, video_id):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO downloaded_videos (id, last_updated) VALUES(?, ?)", [video_id, datetime.now()])
        cursor.close()
        self.db.commit()

    def isDownloaded(self, video_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT id FROM downloaded_videos WHERE id LIKE ?", [video_id])
        result = cursor.fetchone()
        cursor.close()
        return result is not None

    def close(self):
        self.db.close()


def makeCache(configuration):
    return Cache(configuration)
