Given eu sou o usuário “pedro12” na página inicial da aplicação
And eu quero criar uma review sobre um episódio que acabei de assistir, 
         com uma imagem e a tag “Review”
And a tag “Review” já existe
When seleciono a opção de criar um novo post
And escrevo no título do post “TITULO ALTERADO DE NOVO!”
And escolho a tag “Review”
And escrevo no corpo “Essa segunda temporada de Jujutsu Kaisen está muito boa! Episódio fantástico!”
And seleciono a opção de anexar um arquivo local de mídia
Then uma janela do explorador de arquivos do computador é aberta
And escolho o arquivo “screenshot.png”
Then a janela é fechada e estou de volta na janela de criação do post
And é indicado que “screenshot.png” está anexada ao post
And seleciono a opção de publicar o meu post 
Then minha review é publicada, com o campo de usuário sendo “pedro12”

Cenário de falha 1
Then aparece um pop-up de erro na janela

Cenário de falha 2

MEU QUINTO CENÁRIO

CENÁRIO 4
