from apps.core.integrations.rick_and_morty.integrations_core import integrationRickAndMorty
from rest_framework.response import Response
from rest_framework import status

class conection_rick_and_morty():
    def __init__(self) -> None:
        self.integrationRickAndMorty=integrationRickAndMorty()
    
    def MeloElCompraIjon(self, adicion):
        Melo=self.integrationRickAndMorty.conections(adicion)    
        if Melo.status_code==200:
            response=Melo.json()
            return response
        return Response("Paila amigo no hay ijon",status=status.HTTP_400_BAD_REQUEST)        
    
    def RickIsLive(self):
        breakpoint()
        JsonComplet=self.MeloElCompraIjon("character")
        response=JsonComplet["results"][0]['status']

        return Response(response,status=status.HTTP_200_OK)