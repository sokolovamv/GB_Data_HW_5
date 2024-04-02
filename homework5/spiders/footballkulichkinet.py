import scrapy
from scrapy.http import HtmlResponse

class FootballkulichkinetSpider(scrapy.Spider):
    name = "footballkulichkinet"
    allowed_domains = ["football.kulichki.net"]
    start_urls = ["https://football.kulichki.net/ruschamp/"]

    def parse(self, response: HtmlResponse):
        teams = response.xpath("//tr/td/b/font/a")
        
        for team in teams:
            name = team.xpath(".//text()").get().strip()
            link = team.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.parse_team, meta={'team_name' : name})


            #yield {
             #   'name' : name,
              #  'link' : link}
    
    def parse_team(self, response):
        rows = response.xpath("//tr/td/font/b/a")
        for row in rows:
            coach = row.xpath(".//text()").get().strip() 
            name = response.request.meta['team_name']
            yield {
                'team_name' : name, 
                'coach' : coach
                }


        """_summary_

        Yields:
            _type_: _description_
        

        balls = response.xpath("//tr/td/font/b")

        for ball in balls:
            numbers = ball.xpath(".//text()").get().strip()
            yield {
            'team_name' : name, 
            'balls' : numbers
            }

        

        """
        #yield response.follow(url=link, callback=self.parse_teams, meta={'team_name' : name})

   # def

"""
    def parse_teams(self, response):
        rows = response.xpath("//tr[contains(@class, 'col2 inl vtop')]")
        for row in rows:
            balls = row.xpath(".//td/font/b").get().strip()
            name = response.request.meta['team_name']
        
        yield {
            'team_name' : name, 
            'balls' : balls
            """ 
