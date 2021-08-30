import asyncio

from motor.motor_asyncio import AsyncIOMotorClient


class MotorBase:
    _db = {}
    _collection = {}

    def __init__(self, connection_string: str, loop=None):
        self.connection_string = connection_string
        self.loop = loop or asyncio.get_event_loop()

        self.db = None

    def client(self, db: str) -> AsyncIOMotorClient:
        self.db = db
        return AsyncIOMotorClient(f"{self.connection_string}", io_loop=self.loop)

    def get_db(self, db: str):
        """
        Get a db instance
        :param db: database name
        :return: the motor db instance
        """
        if db not in self._db:
            self._db[db] = self.client(db)[db]

        return self._db[db]
