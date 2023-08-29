Feature: Mais Vistos
	Lista de animes ordenados de acordo com sua quantidade de visualizacoes

Scenario: Mudar periodo de tempo
Given estou na página Mais Vistos
Then eu vejo uma lista de animes sem periodo de tempo definido
And o primeiro anime da lista desde sempre é "Kimetsu no Yaiba" com "646" visualizacoes
And o segundo anime da lista desde sempre é "Naruto" com "269" visualizacoes
And o terceiro anime da lista desde sempre é "One Piece" com "212" visualizacoes
When eu seleciono que o periodo da lista seja do último "mes"
Then o primeiro anime da lista do ultimo mes é "Kimetsu no Yaiba" com "71" visualizacoes
And o segundo anime da lista do ultimo mes é "One Piece" com "58" visualizacoes
And o terceiro anime da lista do ultimo mes é "Naruto" com "46" visualizacoes

Scenario: Mudar quantidade máxima de itens na lista
Given estou na página Mais Vistos
Then eu vejo uma lista de animes
And o primeiro anime da lista é "Cowboy Bebop" com "337" visualizacoes
And o segundo anime da lista é "Shingeki no Kyojin" com "225" visualizacoes
And o terceiro anime da lista é "One Piece" com "49" visualizacoes
When eu mudo o limite de itens na lista para "2"
Then o primeiro anime da lista é "Cowboy Bebop" com "337" visualizacoes
And o segundo anime da lista é "Shingeki no Kyojin" com "225" visualizacoes
And o terceiro anime da lista não é retornado