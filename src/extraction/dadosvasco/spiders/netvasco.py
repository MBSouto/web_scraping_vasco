import scrapy


class NetvascoSpider(scrapy.Spider):
    name = "netvasco"
    allowed_domains = ["www.netvasco.com.br"]
    start_urls = ["https://www.netvasco.com.br/futebol/index2023.shtml"]

    def parse(self, response):
        # Extrai os links para as temporadas
        temporadas = response.css(
            'div.col-md-3 div.relacionados ul.list-inline li a::attr(href)'
        ).getall()

        for link in temporadas:
            url_completa = response.urljoin(link)
            yield scrapy.Request(url=url_completa, callback=self.parse_temporada)

    def parse_temporada(self, response):
        # Extrai as informações das partidas nesta página de temporada
        partidas = response.css('div.col-md-9')

        for partida in partidas:
            yield {
                'data_mandante_visitante_gols': partida.css('tbody td::text').getall(),
                'competição_resultado': partida.css('tbody td b::text').getall(),
                'temporada': partida.css('div.row::text').get()
            }
