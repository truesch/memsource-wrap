from pprint import PrettyPrinter
from memsource.memsource import Memsource

pp = PrettyPrinter()

m = Memsource(user_name='tj.ruesch', password='#b4cyYCz#hVXhT*')

# test client
customer = m.client.create("Test Client 7")
customer_list = m.client.list()
m.client.get(customer_list[0])

project = m.project.list()[0]
pp.pprint(project)