from pprint import PrettyPrinter
from memsource.memsource import Memsource

pp = PrettyPrinter()

m = Memsource(user_name='tj.ruesch', password='#b4cyYCz#hVXhT*')

m.client.create("Test Client")
