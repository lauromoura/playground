import scrapy
from scrapy.contrib.loader import ItemLoader
from scrapy.selector import Selector

MAX_STAGES = 19

class Rider(scrapy.Item):
    name = scrapy.Field()
    secondsBehind = scrapy.Field()
    stageNumber = scrapy.Field()

class RiderPipeline(object):

    def process_item(self, item, spider):
        return item

class ProCyclingStatsGCScraper(scrapy.Spider):
    name = 'pcs-vuelta-scraper'

    def __init__(self, stage=None):
        if stage is None:
            stage = '1'

        start_urls = 'http://www.procyclingstats.com/race/Vuelta_a_Espana_2014_Stage_%s_General_Classification'

        self.start_urls = [start_urls % x for x in range(1,2)]

    def parse(self, response):
        stageNumber = response.xpath('//font[@class="blue"]/text()').extract()[0]
        self.log("STAGE NUMBER: " + stageNumber)

        leaderTime = 0

        for sel in response.css("#ResultList > div[style*='padding: 5px 0;']"):
            names = sel.xpath(".//a[starts-with(@href, 'rider/')]/@href").extract()[0].split('/')[-1]
            name = ' '.join([x.capitalize() for x in names.split('_')])
            time = sel.xpath('.//span[last()]/text()').extract()[0]

            if time == ',,':
                secondsBehind = self.lastSeconds
            else:
                time = map(int, time.split(':'))
                secondsBehind = time[-1] + time[-2] * 60
                if (len(time) == 3):
                    secondsBehind += time[-3] * 3600

                if leaderTime and leaderTime != secondsBehind:
                    secondsBehind += leaderTime
                else:
                    leaderTime = secondsBehind

                self.lastSeconds = secondsBehind


            rider = Rider()
            rider['name'] = name
            rider['secondsBehind'] = secondsBehind
            rider['stageNumber'] = stageNumber

            yield rider
