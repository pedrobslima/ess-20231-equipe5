Feature: Criação e vizualização de posts
  As a usuário
  I want criar e visualizar posts.
  so that eu possa interagir com o fórum.

Scenario: Criação de post
    Given que estou na página de criação de postagens
    When Seleciono o título de post "Review episódio 2 de Jujutsu Kaisen"
    And Escolho a tag "Review"
    And Escrevo no corpo "Essa segunda temporada de Jujutsu Kaisen está muito boa! Episódio fantástico!"
    Then Minha review é publicada
    And Eu vejo o post do usuário "pedro12" com título "Review episódio 2 de Jujutsu Kaisen" e conteúdo "Essa segunda temporada de Jujutsu Kaisen está muito boa! Episódio fantástico!" e tags "Review"