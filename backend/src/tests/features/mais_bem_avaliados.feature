Feature: Mais Bem Avaliados
    Lista de animes ordenados de acordo com sua avaliacao

    Scenario: Acessar lista de animes mais bem avaliados na ordem decrescente
        Given order_best_rated retorna uma lista de animes
        When uma requisicao GET for enviada para "/mais-bem-avaliados/?order_by=decrescente"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve conter uma lista de animes ordenada de forma decerescente
    
    Scenario: Acessar lista de animes mais bem avaliados na ordem crescente
        Given order_best_rated retorna uma lista de animes
        When uma requisicao GET for enviada para "/mais-bem-avaliados/?order_by=crescente"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve conter uma lista de animes ordenada de forma crescente
    
    Scenario: Definir tamanho da lista de animes
        Given order_best_rated retorna uma lista contendo o nome a nota dos animes armazenados
        When uma requisicao GET for enviada para "/mais-bem-avaliados/?max=2"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve conter uma lista com no maximo "2" elementos