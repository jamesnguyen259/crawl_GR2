# -*- coding: utf-8 -*-
import mysql.connector
import difflib
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DiadiemPipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="jamesnguyen96", database="hanoitravel", charset = "utf8mb4")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if spider.name == "restaurants":
            try:
                query2 = "INSERT INTO restaurants (name, location, source_url, time, price, phone, image_url, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                self.cursor.execute(query2, (item['name'], item['location'], item['url'], item['time'], item['price'], item['phone'], item['image'], item['description']))
                self.conn.commit()
            except mysql.connector.Error, e:
                print("Error %s" % e.args[1])

        elif spider.name == "hotels":
            try:
                flag = False
                self.cursor.execute("SELECT * FROM hotels")
                result = self.cursor.fetchone()
                while result is not None:
                    if difflib.SequenceMatcher(a=item['name'], b=result[1]) > 0.6 and difflib.SequenceMatcher(a=item['location'], b=result[2]) > 0.6:
                        print("Item already in db!")
                        flag = True
                        result = self.cursor.fetchone()
                if flag == False:
                    query = "INSERT INTO hotels (name, location, source_url, image_url, rating, description) VALUES (%s, %s, %s, %s, %s, %s)"
                    self.cursor.execute(query, (item['name'], item['location'], item['source_url'], item['image_url'], item['rating'] , item['description']))
                    self.conn.commit()
            except mysql.connector.Error, e:
                print("Error %s" % e.args[1])

        elif spider.name == "history_places" or spider.name == "pagodas" or spider.name == "some_places":
            query = "INSERT INTO famous_places (name, location, phone, source_url, image_url, description) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, (item['name'], item['location'], item['phone'], item['source_url'], item['image_url'], item['description']))
            self.conn.commit()

        return item
        # pass
