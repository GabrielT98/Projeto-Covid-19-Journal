class Noticia:
    def __init__(self,id : int ,titulo : str ,urlVideo : str ,urlImagem : str ,texto : str ,dataPub : str ):
        self.__id = id
        self.__titulo = titulo
        self.__urlVideo = urlVideo
        self.__urlImagem = urlImagem
        self.__texto = texto
        self.__dataPub = dataPub
        self.__curtidas = 0
        self.__visualizacoes = 0

    def getId(self) -> int :
        return self.__id

    def getTitulo(self) -> str :
        return self.__titulo

    def getUrlVideo(self) -> str :
        return self.__urlVideo

    def getUrlImagem(self) -> str :
        return self.__urlImagem

    def getTexto(self) -> str :
        return self.__texto
    
    def getDataPub(self) -> str :
        return self.__dataPub
    
    def getCurtidas(self) -> int :
        return self.__curtidas
    
    def getVisualizacoes(self) -> int:
        return self.__visualizacoes