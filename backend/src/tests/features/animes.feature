Feature: Items API

  Scenario: Obter lista de animes
    Given a ClasseAnime retorna uma lista de objetos anime
    When uma requisição GET for enviada para emalta
    Then o status da resposta deve ser 200
    And o JSON da resposta deve ser uma lista composta por animes 
    