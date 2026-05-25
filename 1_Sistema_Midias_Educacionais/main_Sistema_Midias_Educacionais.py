from questao1_lista2 import Midia, Video, Podcast, TextoNarrado, Plataforma

minha_plataforma = Plataforma("SoundCloud")

v1 = Video("aula de samba", "20", "1080p")
p1 = Podcast("Circuitos", "40", "Carlinhos")
t1 = TextoNarrado("A Historia dos Povos originarios", "15", "portugues")

minha_plataforma.adicionar_midia(v1)
minha_plataforma.adicionar_midia(p1)
minha_plataforma.adicionar_midia(t1)

minha_plataforma.listar_midias()
minha_plataforma.reproduzir_todas()

"""
Qual é a classe abstrata do sistema?
R = A classe "Midia" é a classe abstrata do sistema

Onde aparece a hierarquia?
R = Nas classes "Video", "Podcast" e "TextoNarrado", podemos afirmar isso pois a hierarquia aparece na definição das classes, que herdam da super classe
"Midia"

Onde aparece o polimorfismo?
R = O polimorfismo aparece no método reproduzir() e na forma como a classe "Plataforma" o executa, dentro do método reproduzir_todas da "Plataforma", existe
a linha print(j.reproduzir()), o polimorfismo acontece exatamente aí: a plataforma chama o mesmo método (reproduzir()) para todos os itens da lista, mas cada 
objeto responde de uma forma diferente (o vídeo mostra a resolução, o podcast mostra o apresentador e o texto narrado mostra o idioma)

Por que Midia não deveria ser instanciada diretamente?
R = "Midia" é uma classe abstrata, não faz sentido existir uma mídia genérica que não seja nem vídeo, nem podcast e nem texto narrado. Ela serve apenas 
como um molde para as outras classes.
"""
