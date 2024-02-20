import requests

class integrationRickAndMorty ():
    def conections(self,extension):
        url= "https://rickandmortyapi.com/api/"
        url+=extension
        response=requests.get(url)
        return response

        