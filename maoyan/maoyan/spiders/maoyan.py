from scrapy import Spider, Request
from tenxunvideo.items import MovieItem

class MaoyanSpider(Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com/board/4?offset=']
    start_urls = ['http://maoyan.com/board/4?offset=']

    # 每部电影详情页的基本前缀url
    base_url = 'http://maoyan.com'

    # 下一页前缀url
    next_base_url = 'http://maoyan.com/board/4'

    def parse(self, response):
        if response:
            # 获取每页所有电影的节点
            movies = response.css('dl.board-wrapper dd')  # 获取所有电影相关节点，切记！！不能加上extract()
            item = MovieItem()
            for movie in movies:
                item['title'] = movie.css('p.name a::text').extract_first()
                item['actors'] = movie.css('p.star::text').extract_first().strip()
                item['releasetime'] = movie.css('p.releasetime::text').extract_first().strip()
                item['score'] = movie.css('i.integer::text').extract_first() + movie.css(
                    'i.fraction::text').extract_first()
                item['detail_page'] = self.base_url + movie.css('p.name a::attr(href)').extract_first()
                item['cover_img'] = movie.css(
                    'a.image-link img.board-img::attr(data-src)').extract_first()  # 注意：需要根据网页源码写css选择器，和审查元素中的不同，估计是受JS影响
                yield item

            # 处理下一页
            next = response.xpath('.').re_first(r'href="(.*?)">下一页</a>')
            if next:
                next_url = self.next_base_url + next
                yield Request(url=next_url, callback=self.parse, dont_filter=True)