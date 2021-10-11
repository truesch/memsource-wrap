from typing import List
from memsource import api_rest

from memsource.schemas.client import Client as ClientModel


class Client(api_rest.BaseApi):
    # Document: https://cloud.memsource.com/web/docs/api#tag/Client

    def create(self, name: str) -> ClientModel:
        return ClientModel(**self._post("v1/clients", {"name": name}))

    def get(self, clientID: int) -> ClientModel:
        return ClientModel(**self._get(f"v1/clients/{clientID}"))

    def list(self, page: int=0) -> List[ClientModel]:
        clients = self._get("v1/clients", {"page": page})
        return [ClientModel(**client) for client in clients.get("content", [])]
