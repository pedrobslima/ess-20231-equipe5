Feature: Criação e vizualização de posts
  As a usuário
  I want criar e visualizar posts.
  so that eu possa interagir com o fórum.

Scenario: Adicionar e remover tags 
  Given que estou na página de criação de postagens
  When eu adiciono a tag "tag1" 
  And eu adiciono a tag "tag2" 
  Then as tags "tag1" e "tag2" devem ser exibidas 
  When eu removo a tag "tag1" 
  Then a tag "tag1" não deve mais estar visível
