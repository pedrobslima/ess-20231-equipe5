Feature: Publicação de comentários

    Scenario: Comentando uma Postagem
    Given Eu sou o usuário "vinicius13" e estou na página "comments/59b048d5-c8be-4a06-97a1-4703bd4974ca/new_comment"
    When Eu monto o meu comentário com corpo "A sua review é horrível."
    And Faço uma requisição de "POST" do meu comentário, para a rota atual
    Then O status da resposta deve ser "201"