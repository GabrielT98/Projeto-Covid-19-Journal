from typing import List
from application.model.entity.noticia import Noticia

class Estado:
    def __init__(self,nome : str ,sigla : str ,imagem: str ,noticias :List[Noticia]):
        self.__nome = nome
        self.__sigla = sigla
        self.__imagem = imagem
        self.__noticias = noticias
    
    def getNome(self) -> str :
        return self.__nome
    
    def getSigla(self) ->str :
        return self.__sigla
    
    def getImagem(self) -> str:
        return self.__imagem

    def getNoticias(self) -> List[Noticia]:
        return self.__noticias