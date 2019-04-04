# -*- coding: utf-8 -*-
import mysql.connector
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Amthuc365Pipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="jamesnguyen96", database="time_test", charset = "utf8mb4")
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        try:
            query = "INSERT INTO restaurants (name, location, url, time, price, phone, image, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, (item['name'], item['location'], item['url'], item['time'], item['price'], item['phone'], item['image'], item['description']))
            self.conn.commit()
        except mysql.connector.Error, e:
            print("Error %s" % e.args[1])
        return item
