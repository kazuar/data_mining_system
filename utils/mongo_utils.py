
import pymongo
import traceback

MONGODB_ADDRESS = 'localhost'
MONGODB_PORT = 27017

class MongodbConnection(object):
    def __init__(self):
        self._connection = None

    @property
    def connection(self):
        if not self._connection:
            try:
                self._connection = pymongo.MongoClient(MONGODB_ADDRESS, MONGODB_PORT)
            except Exception:
                traceback.print_exc()
        return self._connection
