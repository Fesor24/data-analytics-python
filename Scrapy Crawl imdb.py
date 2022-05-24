import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['www.imdb.com/']
    start_urls = ['https://www.imdb.com/chart/boxoffice/?ref_=hm_cht_sm']

    def parse(self, response):
        
        movie_list= response.xpath("//tbody/tr")
        
        for movie in movie_list:
            title= movie.xpath(".//td[@class='titleColumn']/a/text()").getall()
            gross= movie.xpath(".//td[@class='ratingColumn']/span/text()").getall()
        
            yield {
        
                'titles': title,
                'gross_income': gross,
            
        
            }
        
