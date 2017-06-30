import scrapy
from internetusers.items import InternetusersItem

class internetusers(scrapy.Spider):
	name = 'internetusers'
	allowed_domain =['http://www.internetlivestats.com/'] 
	start_urls =['http://www.internetlivestats.com/internet-users-by-country/']

def parse(self, response):
	for sel in response.xpath('//*[@id="pagecontentwrapper"]/div'):
		
		item = InternetusersItem()
		item['country'] = sel.xpath('//*[@id="example"]/tbody/tr[1]/td[2]/a/text()').extract()	    
		#item['users'] = sel.xpath('//*[@id="example"]/tbody/tr[1]/td[3]/text()').extract() 
    	#item['penetration'] = sel.xpath('//*[@id="example"]/tbody/tr[1]/td[4]/text()').extract()
 		#item['population'] = sel.xpath('//*[@id="example"]/tbody/tr[1]/td[5]/text()').extract()
 		#item['nonusers'] = sel.xpath('//*[@id="example"]/tbody/tr[1]/td[6]/text()').extract()
		
		yield item

