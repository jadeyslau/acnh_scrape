# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import telebot, json, csv, slack
from datetime import datetime
from . import topsecret

class ScrapyacnhPipeline(object):

    def send_message_slack(self, message, channel):
        token    =  topsecret.slack_token

        client   = slack.WebClient(token=token)
        response = client.chat_postMessage(channel=channel,text=message)
        assert response["ok"]
        # assert response["message"]["text"] == message

    def send_message_telegram(self, item, spider):
        product  = item.get('Product')
        link     = item.get('Link')
        status   = item.get('Status')
        in_stock = item.get('In Stock')

        token   = topsecret.telegram_token
        chat_id = topsecret.telegram_chat_id

        if in_stock:
            bot = telebot.TeleBot(token)
            bot.send_message(chat_id, product+' is in stock: '+link)

    def check_last_scrape(self, spider):
        csv_file  = 'tmp/'+spider.name+'.csv'
        with open(csv_file, "r", encoding="utf-8", errors="ignore") as scraped:
            reader = csv.reader(scraped, delimiter=',')
            n_rows = sum(1 for row in reader)-1
            scraped.seek(0)
            reader = csv.reader(scraped, delimiter=',')
            in_stock = False

            for i, row in enumerate(reader):
                if i == n_rows:
                    if row[1] == 'True': in_stock = True
        return in_stock

    def process_item(self, item, spider):
        now = datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")

        if not self.check_last_scrape(spider): #if last scrape returned false then send message
            self.send_message_telegram(item, spider)

        self.send_message_slack(now+' '+spider.name+' is running on '+topsecret.device, '#test')
        return item
