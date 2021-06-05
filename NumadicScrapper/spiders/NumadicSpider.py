import scrapy
from NumadicScrapper.items import ArticleItem

class NumadicSpider(scrapy.Spider):
	name = "numadic"
	start_urls = ['https://www.theguardian.com/world/all']

	def parse(self,response):
		ARTICLE_URL_SELECTOR = '//*[contains(@class,"fc-item__link")]//@href'
		for article_url in response.xpath(ARTICLE_URL_SELECTOR).extract():
			yield scrapy.Request(
				url = article_url,
				callback=self.parsearticle
			)

		NEXT_PAGE_SELECTOR = '//*[contains(@class,"pagination__action--static") and contains(@rel,"next")]//@href'
		next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
		if(next_page):
			yield scrapy.Request(
				response.urljoin(next_page),
                callback=self.parse
				)

	def parsearticle(self,response):

		HEADLINE_SELECTOR = '//h1/text()'
		AUTHOR_SELECTOR = '(//a[@rel="author"]/text()|//a[@rel="author"]/*/text())'
		PUBLISHEDAT_SELECTOR = '(//*[contains(@itemprop,"datePublished")]//@datetime|//label[@for="dateToggle"]//@datetime)'

		item = ArticleItem()
		headline = response.xpath(HEADLINE_SELECTOR).extract()
		joinedHeadline = ''

		item['headline']= joinedHeadline.join(headline)
		item['author'] = response.xpath(AUTHOR_SELECTOR).extract()
		item['url']=  response.request.url
		item['published_at'] = response.xpath(PUBLISHEDAT_SELECTOR).extract_first()

		yield item




