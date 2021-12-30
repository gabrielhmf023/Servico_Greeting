import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import arrow 


class BoasVindasService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):
        """"
        Carrega o serviço
        """

        logger.debug(mensagens.FIM_LOAD_SERVICO)

    def executar_rest(self, texts):

        logger.debug(mensagens.INICIO_SERVICO)
        start_time = time.time()

        response_predicts = [text.upper() for text in texts['Nome']]
        response_saudacao = [text.upper() for text in ['Olá']]
        response_dia = [text.upper() for text in ['Tenha um bom dia!']]

        logger.debug(mensagens.FIM_SERVICO)
        logger.debug(f"Fim de todas as tarefas em {time.time()-start_time}")

        df_response = pd.DataFrame(texts, columns=['Nome'])
        df_response['Nome'] = response_predicts

        df_response = df_response.drop(columns=['Nome'])

        return response_saudacao, response_predicts ,response_dia
