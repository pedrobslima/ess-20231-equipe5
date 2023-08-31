Feature: Mais Bem Avaliados
    Lista de animes ordenados de acordo com sua avaliacao

Scenario: Mudar a forma de ordenação da lista de decrescente para crescente
Given estou na página Mais Bem Avaliados
Then eu vejo uma lista de animes ordenada de maneira decrescente
And o primeiro anime da lista decrescente é "One Piece" com nota "8.9"
And o segundo anime da lista decrescente é "Kimetsu no Yaiba" com nota "8.7"
And o terceiro anime da lista decrescente é "Naruto" com nota "8.4"
When eu mudo a forma de ordenação para crescente
Then o primeiro anime da lista crescente é "Naruto" com nota "8.4"
And o segundo anime da lista crescente é "Kimetsu no Yaiba" com nota "8.7"
And o terceiro anime da lista crescente é "One Piece" com nota "8.9"

Scenario: Mudar quantidade máxima de itens na lista
Given estou na página Mais Bem Avaliados
Then eu vejo uma lista de animes contendo "3" itens
And o primeiro anime da lista de "3" itens é "One Piece" com nota "8.9"
And o segundo anime da lista de "3" itens é "Kimetsu no Yaiba" com nota "8.7"
And o terceiro anime da lista de "3" itens é "Naruto" com nota "8.4"
When eu mudo o limite de itens na lista para "2"
Then o primeiro anime da lista limitada é "One Piece" com nota "8.9"
And o segundo anime da lista limitada é "Kimetsu no Yaiba" com nota "8.7"
And o terceiro anime da lista não é retornado
    