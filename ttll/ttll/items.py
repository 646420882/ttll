# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TtllItem(scrapy.Item):
    film_name = scrapy.Field()  # 电影名
    film_info_url = scrapy.Field()  # 电影详情页链接
    film_star = scrapy.Field()   # 主演
    film_first_class = scrapy.Field()    # 一级分类
    film_second_class = scrapy.Field()   # 二级分类
    film_director = scrapy.Field()   # 导演
    film_area = scrapy.Field()   # 地区
    film_state = scrapy.Field()   # 状态（完结、BD、HD、TS）
    film_language = scrapy.Field()  # 语言
    film_pubdate = scrapy.Field()   # 上映日期
    film_update = scrapy.Field()   # 更新日期
    film_pic = scrapy.Field()   # 封面图片
    craw_time = scrapy.Field()  # 爬取时间
    play_vid = scrapy.Field()  # 访问js链接时的标识
