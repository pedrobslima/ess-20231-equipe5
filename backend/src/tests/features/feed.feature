Feature: Items API

Scenario: Obter 10 ultimos posts decrescente
    Given o ItemService retorna uma lista de id
    When uma requisição GET for enviada para "/feed"
    Then o status da resposta deve ser "200"
    And o JSON da resposta deve ser uma lista composta por id
    And o post com id "7" está na lista
    And o post com id "6" está na lista
    And o post com id "5" está na lista
    And o post com id "4" está na lista
    And o post com id "3" está na lista
    And o post com id "2" está na lista
    And o post com id "1" está na lista
    And o post com id "0" está na lista