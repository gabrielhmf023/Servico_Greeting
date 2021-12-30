import arrow

# Mensagens log API
INICIO_LOAD_SERVICO = "Carregando o serviço..."
FIM_LOAD_SERVICO = "Serviço carregado."
INICIO_SERVICO = "Iniciando o serviço..."
FIM_SERVICO = "Fim do serviço."

# Error Business #
ERROR_GENERIC = "Ocorreu um erro generico"
ERROR_NOT_TREATMENT = 'Ocorreu algo que não esperavamos \
                        e para seu conforto estaremos olhando.'
ERROR_OS = 'Nao foi possivel identificar o objeto, \
             verificar o caminho especificado'
ERROR_NONE_TYPE = 'Arquivo invalido. verifique o tipo do documento.'
ERROR_KEY = 'Chave incorreta'

# Sucess Business #
SUCESSO_GET = "Classificador OK."
SUCESSO_PREDICT = "Saudaçao realizada com sucesso. DATA: " + arrow.utcnow().format('DD/MM/YYYY')
SUCESSO_ENDPOINT = "Endpoints funcionando"
