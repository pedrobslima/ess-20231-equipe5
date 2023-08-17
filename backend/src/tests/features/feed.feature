Feature: Items API

Scenario: Obter 10 ultimos posts decrescente
    Given o ItemService retorna uma lista de id
    When uma requisição GET for enviada para "/feed"
    Then o status da resposta deve ser "200"
    And o JSON da resposta deve ser uma lista composta por id
    And o post com id "7" tem posição "0" na lista
    And o post com id "6" tem posição "1" na lista
    And o post com id "5" tem posição "2" na lista
    And o post com id "4" tem posição "3" na lista
    And o post com id "3" tem posição "4" na lista
    And o post com id "2" tem posição "5" na lista
    And o post com id "1" tem posição "6" na lista
    And o post com id "0" tem posição "7" na lista