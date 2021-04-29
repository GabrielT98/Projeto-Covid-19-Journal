from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia

class EstadoDAO:
    def __init__(self):
        noticia1 = Noticia(1,"São Paulo tem semana mais mortal da pandemia, com 5.657 óbitos.",
        'video/noticia1.mp4','img/noticia1.png','O estado de São Paulo teve a semana com mais mortes da pandemia entre 4 e 10 de abril, com 5.657 óbitos. É praticamente o triplo do número de vítimas da semana com mais mortes na primeira onda, em meados de julho, quando 1.945 pessoas perderam a vida devido à covid-19. Os dados são da Secretaria Estadual de Saúde, compilados pelo consórcio de imprensa de que o UOL faz parte. Hoje (11) foram registradas 510 mortes por covid-19 --o número é extremamente alto para um domingo, quando a quantidade de dados incluída no sistema costuma cair. O número de mortes por covid-19 na última semana é 13% maior do que na anterior. Já faz seis semanas que a quantidade de vítimas da pandemia sobe sem para em São Paulo. O número de casos na semana de 4 a 10 de abril também foi o maior já registrado pelo estado. Mas a alta em relação à semana anterior é menor do que a verificada entre as mortes, 5%. Isso é um indicativo de que a pandemia está, muito lentamente, tirando o pé do acelerador --embora ainda esteja acelerando. Os reflexos são sentidos primeiro no número de casos e, só depois, no de mortes --já que, em geral, a covid-19 não provoca morte imediata. Na contramão do número de mortes e casos, a ocupação dos leitos exclusivos para pacientes com covid-19 vem caindo em São Paulo. Depois de passar de 90%, chegou a 86% neste domingo (11).',
        "11/04/2021")

        noticia2 = Noticia(2,"Sem aval da Anvisa para testes, Butantan começa hoje a produzir ButanVac.",'video/noticia2.mp4','img/noticia2.png','  O Instituto Butantan começa hoje a produzir as primeiras doses da ButanVac, a vacina contra a covid-19 que deve ter produção 100% nacional, sem a necessidade da importação de matéria-prima. O instituto, porém, ainda precisa de um aval da Anvisa (Agência Nacional de Vigilância Sanitária) para iniciar os testes clínicos do imunizante em humanos. Ontem, a agência negou a autorização e pediu o complemento de documentação por parte do Butantan, que se comprometeu em atender às exigências. Antes disso, o UOL havia adiantado que o instituto pretendia começar a produção da ButanVac ainda nesta semana. Segundo o diretor do Butantan, Dimas Covas, a instituição começará a produzir inicialmente um primeiro lote com um milhão de doses, mas tem a expectativa de produzir 18 milhões de doses até junho. O anúncio do início da produção vem num momento em que o país enfrenta uma escassez de oferta de doses da CoronaVac, a vacina contra a covid-19 envasada pelo Butantan com insumos importados da China. Há problemas em diversas cidades brasileiras, principalmente, com a aplicação da dose de reforço.Linha de produção da vacina contra a gripe O Butantan alega que a distribuição das doses é de responsabilidade do Ministério da Saúde, que chegou a orientar os municípios a não guardarem a segunda dose e usarem todo o estoque. Durante a coletiva realizada hoje no Instituto Butantan, com a equipe do governador João Doria (PSDB), a coordenadora do programa estadual de imunização, Regiane de Paula, repetiu que não há falta de doses no estado de São Paulo. De acordo com o Butantan, a fabricação da ButanVac vai ocorrer em uma linha de produção que vinha sendo utilizada para a vacina contra a gripe. A CoronaVac é produzida e envasada em outro maquinário. Assim como a vacina da gripe, o Butantan utilizará para a ButanVac a técnica de obtenção do IFA (Insumo Farmacêutico Ativo) a partir do cultivo de cepas do vírus em ovos de galinha. A instituição tem hoje um primeiro lote com 520 mil ovos que receberão o vírus, rendendo depois duas doses da vacina cada um. No anúncio da ButanVac, há cerca de um mês, o governo paulista e o Butantan chegaram a classificar a vacina como "100% brasileira". Logo depois, porém, a instituição admitiu que usou uma tecnologia criada no Hospital Mount Sinai, de Nova York, nos Estados Unidos. A ButanVac é desenvolvida por um consórcio internacional, mas poderá ser produzida integralmente no Butantan, com custo mais baixo.',
        "28/04/2021")

        