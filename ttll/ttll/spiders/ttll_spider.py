import scrapy
from ..items import TtllItem


class TtllSpider(scrapy.Spider):
    name = 'ttll'

    def start_requests(self):

        self.index = 'https://www.ttll.cc'
        url = 'https://www.ttll.cc/dy/index.html'
        yield scrapy.Request(url=url, callback=self.get_page)

    def get_page(self,response):

        pages = int(response.xpath('//div[@class="g_page"]/b/text()').extract_first()[1:-1])
        for page in range(1, pages+1):
            if page == 1:
                url = 'https://www.ttll.cc/dy/index.html'
            else:
                url = f'https://www.ttll.cc/dy/index{page}.html'
            yield scrapy.Request(url=url, callback=self.get_infourl)

    def get_infourl(self, response):

        info_urls = response.xpath('//ul[@class="watch"]/li/h4/a/@href').extract()
        for info_url in info_urls:
            film_info_url = self.index + info_url   # 详情页地址
            yield scrapy.Request(url=film_info_url, callback=self.get_info)


    def get_info(self, response):

        sel = response.xpath('//div[@class="pdetail"]')
        item = TtllItem()

        item['film_info_url'] = response.url
        item['film_name'] = sel.xpath('h2/text()').extract_first()
        item['film_star'] = sel.xpath('p[1]/text()').extract_first()
        item['film_first_class'] = sel.xpath('//div[@class="curlocation"]/p/a[2]/text()').extract_first()
        item['film_second_class'] = sel.xpath('p[2]/text()').extract_first()
        item['film_director'] = sel.xpath('p[3]/label[1]/a/text()').extract_first()
        item['film_state'] = sel.xpath('p[3]/label[2]/text()').extract_first()
        item['film_area'] = sel.xpath('p[4]/label[1]/text()').extract_first()
        item['film_language'] = sel.xpath('p[4]/label[2]/text()').extract_first()
        item['film_pubdate'] = sel.xpath('p[5]/label[1]/text()').extract_first()
        item['film_update'] = sel.xpath('p[5]/label[2]/text()').extract_first()
        item['film_pic'] = response.xpath('//div[@class="poster-con"]/img/@src').extract_first()

        url = response.url + 'bf-0-0.html'  # 播放页地址（用于提取play_vid）
        yield scrapy.Request(url=url, meta={'key': item},callback=self.get_vid)

    def get_vid(self,response):
        play_vid = self.index + response.xpath('//div[@class="play-container"]/div[1]/script[@type="text/javascript"]/@src').extract_first()  # js地址

        item = response.meta['key']
        item['play_vid'] = play_vid
        yield scrapy.Request(url=play_vid,meta={'key': item},encoding='utf-8', body='unicode',callback=self.get_js)

    def get_js(self,response):
        item = response.meta['key']
        a = response.text.encode('latin-1').decode('unicode_escape')
        b = a.replace('var VideoListJson=','')

        yield item




