"""
@author grtsinry43
@date 2024/12/24 17:19
@description 热爱可抵岁月漫长
"""
import json
import io
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["py-exper"]
collection = db["movies"]

class Movie:
    name: str
    en_name: str
    imgSrc: str
    info: str
    intro: str
    short_comment: str
    comment: str
    item_link: str
    directors: list
    actors: list
    types: list

def load_data(filename='result.json'):
    with io.open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_to_db(data):
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

def main():
    data = load_data('result.json')
    # 每次运行前清空数据库
    collection.delete_many({})
    save_to_db(data)
    print("Data has been saved to the database.")

if __name__ == '__main__':
    main()