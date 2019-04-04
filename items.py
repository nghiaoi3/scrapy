# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    url = scrapy.Field()
    CompetitionName = scrapy.Field()
    Country = scrapy.Field()
    Matchsplayed = scrapy.Field()
    Matchsremaining = scrapy.Field()
    HomeWinRate = scrapy.Field()
    DrawRate = scrapy.Field()
    AwayWinRate = scrapy.Field()
    # lastUpdated = scrapy.Field()
