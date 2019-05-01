# -*- coding: utf-8 -*-
import mysql.connector
import logging
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HanoialleventPipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="jamesnguyen96", database="hanoitravel", charset = "utf8mb4")
        self.cursor = self.conn.cursor(buffered=True)
    def process_item(self, item, spider):
        try:
            #first, check crawled
            query1 = "SELECT * FROM events WHERE source_url = %s"
            self.cursor.execute(query1,(item['source_url'],))
            result = self.cursor.fetchone()
            #crawled -> UPDATE data
            if result:
                query2 = "UPDATE events SET name = %s, location = %s, lat = %s, lng = %s, start_time = %s, end_time = %s, image_url = %s, description = %s, organizer_name = %s WHERE source_url = %s"
                self.cursor.execute(query2, (item['name'], item['location'], item['lat'], item['lng'], item['start_time'], item['end_time'], item['image_url'], item['description'], item['organizer_name'], item['source_url'],))
                self.conn.commit()
                logging.info("Item updated!")
            #not crawled -> INSERT data
            else:
                query2 = "INSERT INTO events (name, location, lat, lng, start_time, end_time, source_url, image_url, description, organizer_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                self.cursor.execute(query2, (item['name'], item['location'], item['lat'], item['lng'],item['start_time'], item['end_time'], item['source_url'], item['image_url'], item['description'], item['organizer_name']))
                self.conn.commit()
                logging.info("Item inserted!")
        except mysql.connector.Error, e:
            print("Error %s" % e.args[1])
        return item
