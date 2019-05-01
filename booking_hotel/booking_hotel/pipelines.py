# -*- coding: utf-8 -*-
import mysql.connector
import logging
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookingHotelPipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="jamesnguyen96", database="hanoitravel", charset = "utf8mb4")
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        try:
            query = "INSERT INTO hotels (name, location, lat, lng,  source_url, image_url, rating, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, (item['name'], item['location'], item['lat'], item['lng'], item['source_url'], item['image_url'], item['rating'], item['description']))
            self.conn.commit()
            logging.info("1 item has been inserted.")
        except mysql.connector.Error, e:
            print("Error %s" % e.args[1])
        return item
