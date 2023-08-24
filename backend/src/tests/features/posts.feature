Feature: Publicacao de Posts

    Scenario: Criação de post simples
    Given Eu sou o usuário "pedro12" e estou na página de criação de post "/post/new_post"
    When Eu monto o meu post com título "Review episódio 1 de Jujutsu Kaisen", tag "Review", corpo "Episódio legal."
    And Faço uma requisição de "POST" da minha publicação, para a rota atual
    Then O status da resposta deve ser "201"

    Scenario: Criação de post com imagem
    Given Eu sou o usuário "pedro12" e estou na página de criação de post "/post/new_post"
    When Eu monto o meu post com título "Review episódio 2 de Jujutsu Kaisen", tag "Review", corpo "Essa segunda temporada de Jujutsu Kaisen está muito boa! Episódio fantástico!"
    And Anexo o arquivo "screenshot.png"
    And Faço uma requisição de "POST" da minha publicação, para a rota atual
    Then O status da resposta deve ser "201"