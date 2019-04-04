import scrapy
from urllib.parse import urljoin
from BetExp.items import Article


class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['https://www.betexplorer.com/soccer/']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('#countries-select li div a::attr(href)'):
            yield response.follow(href, self.parse_author)

        # # follow pagination links
        # for href in response.css('li.next a::attr(href)'):
        #     yield response.follow(href, self.parse)

    def parse_author(self, response):

        for href in response.css('.table-main tbody:nth-child(1) tr td a::attr(href)'):
            # print('href', href)
            yield response.follow("https://www.betexplorer.com" + href.extract()+"stats", self.parse_stats)

    def parse_stats(self, response):
        # def extract_with_css(query):
        #     return response.css(query).get(default='').strip()

        # yield {
        #     # 'name': extract_with_css('span.tablet-desktop-only::text'),
        #     'HomeWinRate': extract_with_css('.table-main tr:nth-child(5) > td:nth-child(3)::text').replace(u'\xa0', ' '),
        #     'AwayWinRate': extract_with_css('.table-main tr:nth-child(7) > td:nth-child(3)::text').replace(u'\xa0', ' ')
        # }
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
