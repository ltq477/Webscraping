import scrapy
from internetusers.items import InternetusersItem

class internetusers(scrapy.Spider):
	name = 'internetusers'
	allowed_domain =['http://www.internetlivestats.com/'] 
	start_urls =['http://www.internetlivestats.com/internet-users-by-country/']

	def parse(self, response):
		for sel in response.xpath('//*[@id="pagecontentwrapper"]//tbody/tr'):

			item = InternetusersItem()
			item['country'] = sel.xpath('.//td[2]/a/text()').extract()
			item['users'] = sel.xpath('.//td[3]/text()').extract()
			item['penetration'] = sel.xpath('.//td[4]/text()').extract()
			item['population'] = sel.xpath('.//td[5]/text()').extract()
			item['nonusers'] = sel.xpath('.//td[6]/text()').extract()

			yield item

