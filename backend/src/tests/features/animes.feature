Feature: Items API

  Scenario: Obter lista de animes
    Given o ItemService retorna uma lista de objetos anime
    When uma requisição GET for enviada para "/EmAlta"
    Then o status da resposta deve ser "200"
    And o JSON da resposta deve ser uma lista composta por animes 
    And o anime com nome "Naruto", avaliacao "7.0" e assistidos "120" está na lista
    And o anime com nome "Kimetsu No Yaiba", avaliacao "7.2" e assistidos "90"  está na lista
    And o anime com nome "One Piece", avaliacao "7.4" e assistidos "130"  está na lista