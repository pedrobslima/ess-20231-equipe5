Feature: Criação e vizualização de posts
    As a usuário
    I want criar e visualizar posts.
    so that eu possa interagir com o fórum.

Scenario: Integração entre página inicial, criação de post e comentar
    Given que estou na página de criação de postagens
    When Seleciono o título de post "Review episódio 1 de Jujutsu Kaisen"
    And Escolho a tag "Review"
    And Escrevo "Episódio legal." no corpo do post
    Then Minha review é publicada
    And Eu vejo o post do usuário "pedro12" com título "Review episódio 1 de Jujutsu Kaisen", com conteúdo "Episódio legal." e tags "Review"
    When Seleciono a opção de comentar no post
    And Escrevo "A sua review é horrível." no corpo do comentário
    And Seleciono a opção de publicar o comentário
    Then meu comentário foi publicado com o corpo sendo "A sua review é horrível.", na página do post original