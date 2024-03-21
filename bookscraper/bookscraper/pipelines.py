# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class BookscraperPipeline:

    def __init__(self) -> None:
        self.myclient = pymongo.MongoClient("mongodb://root:root@localhost:27017/?connectTimeoutMS=300000&authSource=admin")
        self.collection = self.myclient["db_books"]["books"]
    
    def process_item(self, item, spider):
        self.collection.insert_one(item)
