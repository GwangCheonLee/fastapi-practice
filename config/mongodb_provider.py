from motor.motor_asyncio import AsyncIOMotorClient

from config.database import setting

mongodb_client = AsyncIOMotorClient(setting.mongodb_url)
example_database = mongodb_client.get_database("example")
example_collection = example_database.get_collection("items")
