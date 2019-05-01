# -*- coding: utf-8 -*-
import mysql.connector
import difflib
import logging
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DiadiemPipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="jamesnguyen96", database="hanoitravel", charset = "utf8mb4")
        self.cursor = self.conn.cursor(buffered=True)

    def process_item(self, item, spider):
        #for crawl restaurants
        if spider.name == "restaurants":
            try:
                #first, check similar with database
                flag = False
                self.cursor.execute("SELECT * FROM restaurants")
                result = self.cursor.fetchone()
                while result is not None:
                    #if crawled
                    if item['source_url'] == result[5]:
                        flag = True
                        break
                    #else, not crawled
                    else:
                        # get similarity, compare name and location of item being crawled with item crawled in database
                        name1 = item['name'].split(" - ")[0].lower().replace("nhà hàng ", "")
                        name2 = result[1].lower().encode("utf-8").replace("nhà hàng ", "")
                        # lc1 = item['location'].lower().split(", phường")[0].split(" district")[0].split(", quận")[0].split(", huyện")[0].replace(", hà nội","").replace(", việt nam","")
                        # lc2 = result[2].lower().encode("utf-8").split(" - quận")[0].split(" - huyện")[0].replace(" - hà nội","")
                        if ((name1 in name2) \
                        or (name2 in name1) \
                        or (difflib.SequenceMatcher(a=name1, b=name2).ratio() > 0.7)) \
                        and (item['lat'] == result[3]) \
                        and (item['lng'] == result[4]):
                            logging.info("Item duplicated.")
                            logging.info(result[0])
                            logging.info(result[1])
                            # logging.info(difflib.SequenceMatcher(a=item['name'].split(" - ")[0].lower(), b=result[1].encode("utf-8").lower()).ratio())
                            flag = True
                            break
                    #next element
                    result = self.cursor.fetchone()
                if flag == False:
                    query = "INSERT INTO restaurants (name, location, lat, lng, source_url, time, price, phone, image_url, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    self.cursor.execute(query, (item['name'], item['location'], item['lat'], item['lng'], item['source_url'], item['time'], item['price'], item['phone'],item['image_url'], item['description']))
                    self.conn.commit()
                    logging.info("1 item has been inserted.")
            except mysql.connector.Error, e:
                print("Error %s" % e.args[1])

        # for crawl hotels
        elif spider.name == "hotels":
            try:
                #first, check similar with database
                flag = False
                self.cursor.execute("SELECT * FROM hotels")
                result = self.cursor.fetchone()
                while result is not None:
                    if item['source_url'] == result[5]:
                        flag = True
                        break
                    else:
                        name1 = item['name'].split(" - ")[0].lower()
                        name2 = result[1].lower().encode("utf-8")
                        # lc1 = item['location'].lower().split(" district")[0].split(", quận")[0].split(", huyện")[0].replace(", hà nội","").replace(", việt nam","")
                        # lc2 = result[2].lower().encode("utf-8").split(", cau giay")[0].split(", quận")[0].split(", huyện")[0].split(" district")[0].replace(", hà nội","").replace(", việt nam","")
                        if ((name1 in name2) \
                        or (name2 in name1) \
                        or (difflib.SequenceMatcher(a=name1, b=name2).ratio() > 0.7)) \
                        and (item['lat'] == result[3]) \
                        and (item['lng'] == result[4]):
                            logging.info("Item duplicated.")
                            logging.info(result[0])
                            logging.info(result[1])
                            # logging.info(difflib.SequenceMatcher(a=lc1, b=lc2).ratio())
                            flag = True
                            break
                    result = self.cursor.fetchone()
                if flag == False:
                    query = "INSERT INTO hotels (name, location, lat, lng, source_url, image_url, rating, description) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"
                    self.cursor.execute(query, (item['name'], item['location'],item['lat'], item['lng'], item['source_url'], item['image_url'], item['rating'] , item['description']))
                    self.conn.commit()
                    logging.info("1 item has been inserted.")
            except mysql.connector.Error, e:
                print("Error %s" % e.args[1])

        #for crawl famous places
        elif spider.name == "history_places" or spider.name == "pagodas" or spider.name == "some_places" or spider.name == "museums":
            try:
                flag = False
                self.cursor.execute("SELECT * FROM famous_places")
                result = self.cursor.fetchone()
                while result is not None:
                    if item['source_url'] == result[6]:
                        flag = True
                        break
                    else:
                        name1 = item['name'].split(" - ")[0].lower()
                        name2 = result[1].lower().encode("utf-8")
                        #check_duplicate
                        if ((name1 in name2) \
                        or (name2 in name1) \
                        or (difflib.SequenceMatcher(a=name1, b=name2).ratio() > 0.7)) \
                        and (item['lat'] == result[3]) \
                        and (item['lng'] == result[4]):
                            logging.info("Item duplicated.")
                            logging.info(result[0])
                            logging.info(result[1])
                            flag = True
                            break
                    result = self.cursor.fetchone()
                if flag == False:
                    query = "INSERT INTO famous_places (name, location, lat, lng, phone, source_url, image_url, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    self.cursor.execute(query, (item['name'], item['location'], item['lat'], item['lng'], item['phone'], item['source_url'], item['image_url'], item['description']))
                    self.conn.commit()
                    logging.info("1 item has been inserted.")
            except mysql.connector.Error, e:
                print("Error %s" % e.args[1])
        return item
        # pass
