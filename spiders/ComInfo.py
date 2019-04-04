import scrapy

from BetExp.items import Article


from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule


class ArticleSpider(scrapy.Spider):

    name = 'article'
    allowed_domains = ['betexplorer.com/soccer']
    competition = ["australia/a-league",
                   "iran/persian-gulf-pro-league", "asia/afc-cup"

                   "albania/albanian-cup",


                   ]

    start_urls = ["https://www.betexplorer.com/soccer/{competition}/stats".format(competition=competition)
                  for competition in competition]

    # name = 'article'
    # def start_requests(self):
    #     urls = [
    #         'https://www.betexplorer.com/soccer/brazil/serie-a/stats/',
    #         'https://www.betexplorer.com/soccer/czech-republic/youth-league/stats/',
    #         'https://www.betexplorer.com/soccer/australia/a-league/stats/'
    #     ]
    #     return [scrapy.Request(url=url, callback=self.parse)
    #             for url in urls]


# get all tds texts
    # def parse(self, response):
    #     trs = response.css('.leaguestats tr')
    #     for tr in trs:
    #         tds = tr.css('td::text')
    #         for td in tds:
    #             print(td.extract())


# get some tds texts

    def parse(self, response):
        article = Article()
        article['url'] = response.url
        article['CompetitionName'] = response.css(
            'span.list-breadcrumb__item__in::text').extract_first().replace(u'\xa0', ' ')

        article['Country'] = response.css(
            'ul.list-breadcrumb li:nth-child(3) a::text').extract_first().replace(u'\xa0', ' ')

        article['Matchsplayed'] = response.css(
            '.leaguestats tr:nth-child(2) td:nth-child(2)::text').extract_first().replace(u'\xa0', ' ')
        article['Matchsremaining'] = response.css(
            '.leaguestats tr:nth-child(3) td:nth-child(2)::text').extract_first().replace(u'\xa0', ' ')
        article['HomeWinRate'] = response.css(
            '.leaguestats tr:nth-child(5) td:nth-child(3)::text').extract_first().replace(u'\xa0', ' ')
        article['DrawRate'] = response.css(
            '.leaguestats tr:nth-child(6) td:nth-child(3)::text').extract_first().replace(u'\xa0', ' ')
        article['AwayWinRate'] = response.css(
            '.leaguestats tr:nth-child(7) td:nth-child(3)::text').extract_first().replace(u'\xa0', ' ')
        return article
