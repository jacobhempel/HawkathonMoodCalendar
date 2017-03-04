import pymongo
import numpy as np
def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.mood_calendar
    users = db.users
    for each_user in users.find():
        moods = each_user['mood']
        avg_mood = np.mean(moods)
        if avg_mood <= 1:
            print 'You seem very sad lately'
        elif avg_mood > 1 and avg_mood < 4:
            print 'You are content lately'
        elif avg_mood >= 4:
            print 'You are very happy lately!'


if __name__ == '__main__':
    main()
