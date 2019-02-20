import json
import requests

class Receita:
    
    URL_POST_RECEITA = 'https://www.receita.fazenda.gov.br/pessoajuridica/cnpj/cnpjreva/Cnpjreva_Comprovante.asp'

    def __ini__(self):
        pass 

    def consulta(self, cnpj):
        return self.request(cnpj)

    def request(self, cnpj):
        tries = 0
        while True:
            r = requests.post(self.URL_POST_RECEITA, data={'cnpj': cnpj})

            if r.status_code == requests.codes.ok:
                return r.content
                break

            if tries > 2:
                break
                raise ValueError('Site da receita provavelmente fora do ar, tente novamente mais tarde')
    