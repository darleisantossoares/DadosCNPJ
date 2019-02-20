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
            with requests.Session() as session:
                r = session.post(self.URL_POST_RECEITA, data={'cnpj': cnpj}, verify=False)

                if r.status_code == requests.codes.ok:
                    return r.text
                    break

                if tries > 2:
                    break
                    raise ValueError('Site da receita provavelmente fora do ar, tente novamente mais tarde')
           
            tries += 1 

if __name__ == '__main__':
    print(Receita().consulta("13449612000108"))