# Projeto Reversi

Este projeto foi criado como um trabalho da disciplina de Inteligência Artificial (GCC128) da Universidade Federal de Lavras e tem como intuito aplicar os fundamentos da disciplina em um jogo de tabuleiros chamado Reversi (ou Othello).

## Linguaguens utilizadas

* Foi utilizada a linguagem Python e a biblioteca Pygame

## Organização dos arquivos

* Na pasta principal se encontram os arquivos .py responsáveis pela implementação do jogo, juntamente com o README
* Na pasta Sprites estão armazenadas as imagens em .png e .jpg utilizadas na interface
* Na pasta fonts está armazenada a fonte utilizada na escrita: BD_Cartoon_Shout

## Explicando os arquivos .py

### Reversi.py

Este arquivo é responsável por implementar a interface do jogo e integrá-la com o back-end do jogo. É nele em que as imagens e a fonte são carregadas e exibidas na tela, além de tratar os eventos de interação com o jogador. Cada função é responsável por uma tela/parte da interface:

#### 1- tela_inicial(): 

É a primeira tela a aparecer no jogo, contém o logo e um botão de jogar.
No trecho abaixo é possível verificar o tratamento de eventos no jogo, como QUIT, que refere-se ao botão de sair padrão e também o MOUSEBUTTONDOWN que captura o clique do usuário e verifica os valores _x_ e _y_ posição clicada. Há uma condição que verifica se o jogador está clicando dentro da área do botão jogar.

```
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
    elif event.type == MOUSEBUTTONDOWN:
        X, Y = pygame.mouse.get_pos()
        if (X >= 350 and X <= 650 and Y >= 400 and Y <= 550):    
```

#### 2- reversiInterface(game, dificuldade)

Responsável pela interação do jogador com o game. Implementa na interface as jogadas a partir dos valores _x]- e _y_ da posição clicada.

```
if Y <= 650 and Y >=75 and X <= 820 and X >= 200:
    # Aqui será verificada qual linha e coluna o jogador escolheu.
    i = floor((X-200)/75)
    j = floor((Y-75)/75)
```

Neste trecho, é verificado em qual posição _ij_ o jogador clicou, para que assim, seja realizada a jogada na matriz do tabuleiro

```
if(game.jogar(i, j)):
    display(game)
    # Esta será a jogada da IA, e é passada a dificuldade (número de recursões).
    jogadaAdv = MiniMax.escolheJogada(game, dificuldade)
    game.jogar(jogadaAdv[0], jogadaAdv[1])
```
Já no trecho acima, é verificado se a jogada é válida para que seja de fato realizada. Após o jogador realizar sua jogada, será a vez da IA que escolherá sua jogada através da chamada método MiniMax que será explicado posteriormente. 


#### 3- game_over(game)

Nesta função é implementada a tela de fim de jogo, contendo o placar e as opções de saída e jogar novamente.

```
 new_game = ReversiGame.ReversiGame()
    selecionar_nivel(new_game)
```
No trecho acima, é criado um novo objeto do jogo que reiniciará o game.

#### 4- selecionar_nivel(game)

Esta função é responsável por criar a tela de seleção de nível. São o total de três níveis, e cada um deles possui um valor de dificuldade diferente, este, será utilizado no método do MiniMax como a altura da árvore de jogo a ser analisada. 
* Fácil: 2
* Médio: 4
* Difícil: 5

#### 5- display(game, todasPoss = [])

Responsável por exibir o tabuleiro, as peças e as possibilidades da jogada a cada iteração do algoritmo. Nota-se que para a IA, as possibilidades não são mostradas, nem mesmo a mensagem para passar a vez

#### 6- background_display(game)

É responsável por carregar a imagem de BG, e também exibir o placar das peças a cada jogada realizada.

<br>

### ReversiGame.py

#### 1- main()

Este método é utilizado apenas para testes das funcionalidades e regras do jogo no terminal.

#### 2- jogar(self, x, y)

Este método é responsável pelo gerenciamento das jogadas, avaliando tanto a posição, quanto realizando a troca de jogadores. Também é responsável pelo cálculo de possibilidades e retorna um valor booleano que indica se a jogada é válida ou não. 
As peças capturadas pelo jogador serão transformadas:
```
  for i in range(-1, 2):
      for j in range(-1, 2):
          if((x+i >= 0 and y+j >= 0) and (x+i <= 7 and y+j <= 7)):
              if(self.tabuleiro[x+i][y+j] == "BLANK"):
                  self.alteradas.add((x+i, y+j))
              self.transformarLinha(x+i, y+j, i, j)
```

#### 3- transformarLinha(self, x, y, desX, desY)

Este método será responsável por realizar a transformação das peças do adversário nas peças do jogador. O algoritmo caminha nas peças do adversário até encontrar uma peça que seja sua. A partir deste ponto, volta para o início transformando as peças adversárias.

#### 4- possJogar(self, x, y)

Este método é responsável por checar se o espaço em branco pode ser jogado, testando as oito linhas que podem definir uma possibilidade.

#### 5- possLinha(self, x, y, desX, desY)

Este método checa se a linha de algum dos oito vizinhos da peça define uma possibilidade.Uma peça do jogador após N do adversário, sem nenhum epaço em branco entre elas.

#### 6- setTodasPoss(self)

Este método é responsável por descobrir todas as possibilidades de jogada que o jogador atual possui na rodada. Caso não haja nenhuma possibilidade, muda-se o estado do jogo.

```
if(len(self.todasPoss) == 0):
    if(self.estado == "NORMAL" and self.placar["BLANK"] > 0):
        self.estado = "PASS"
    else:
        self.estado = "FIN"
```
O atributo estado pode receber o valor "PASS" que passa a vez para o próximo jogador, ou poderá receber o valor "FIN" que finalizará o jogo.

#### 7- getTodasPoss(self)

Este método tem como objetivo, retornar uma lista de tuplas em que cada uma contém os valores x e y das coordenadas das possibilidades.

#### 8- transformaPeca(self, x, y)

Este método é responsável por mudar a cor de uma peça ou colocá-la em um espaço em branco.
```
self.placar[self.tipoJog] += 1
    if(self.tabuleiro[x][y] == "BLANK"):
        self.placar["BLANK"] -= 1         
```
Ao colocar uma nova peça no tabuleiro, o placar do jogador é incrementado e caso a posição seja vazia, a quantidade de posiçes vazias é decrementada.

```
else:
    self.placar[ReversiGame.negTipo(self.tipoJog)] -= 1 
```

Caso não seja vazia, a cor é mudada e o placar do adversário é decrementado.

```
self.tabuleiro[x][y] = self.tipoJog
 ```
Por fim, a posição espacificada do tabuleiro recebe o valor do tipo da peça do jogador.

#### 9- negTipo(tipo)

Este é um método auxiliar que retorna a cor oposta da peça. Utilizado para facilitar a leitura do código.

#### 10- __init__(self)

Este método é o construtor da classe ReversiGame. Responsável por realizar a inicialização dos atributos, como por exemplo o estado, o tipo do jogador, o placar inicial (que começa com duas peças de cada tipo) e a criação da lista de possibilidades. Também é criado o tabuleiro do jogo:

```
 for i in range(8):
    if(i < 3 or i > 4):
        self.tabuleiro.append(["BLANK"]*8)
     elif(i == 3):
        self.tabuleiro.append(["BLANK"]*3 + ["WHITE", "BLACK"] + ["BLANK"]*3)
     else:
        self.tabuleiro.append(["BLANK"]*3 + ["BLACK", "WHITE"] + ["BLANK"]*3)
```
São definidos os espaços das potenciais jogadas e descobre as possibilidades do primeiro a jogar.

<br><br>

### MiniMax.py

Neste arquivo é implementado o algoritmo do MiniMax, que é utilizado pela IA para escolher as suas melhores jogadas, de acordo com previsões de situações futuras em que o jogador possa vencer ou levar vantagens. Isso é calculdado de forma que a cada passo, assume-se que o jogador maximizador está tentando maximizar as suas chances de ganhar, enquanto na próxima rodada o jogador minimizador está tentando minimizar as chances de isso acontecer (maximizando as chances de que ele próprio ganhe). O maximizador precisa escolher uma jogada que tem a maior dentre as menores pontuações que o minimizador pode fazer aquele ter. <br><br>
Foi utilizada a poda alfa e beta com o objetivo de otimizar o algoritmo, uma vez que quanto mais recursões (altura da árvore de possibilidades), mais lento ele fica. <br><br>
Para conhecer mais sobre o MiniMax:
 * https://en.wikipedia.org/wiki/Minimax
 * https://www.youtube.com/watch?v=KU9Ch59-4vw
 * https://www.youtube.com/watch?v=l-hh51ncgDI
 * https://towardsdatascience.com/how-a-chess-playing-computer-thinks-about-its-next-move-8f028bd0e7b1

#### 1- miniMax(tipo, rec, poss, game, alpha, beta, maxRec)

Este método é responsável pela implementação do MiniMax para escolher a melhor jogada. Nele, é passado um valor que definirá quantas recursões serão realizadas, e esse valor irá definir a dificuldade do jogo (o quanto a IA será inteligente).

```
if(rec >= maxRec):
    return Mediador.avaliaJogo(game)
```
Neste trecho, é avaliado o estado do jogo caso seja a última recursão. 

```
possibilidades = Mediador.getPoss(game)
if(len(possibilidades) == 0):
    if(tipo == "MAX"):
        return miniMax("MINI", rec+1, poss, Mediador.cloneGame(game), alpha, beta, maxRec)
    else:
        return miniMax("MAX", rec+1, poss, Mediador.cloneGame(game), alpha, beta, maxRec)
```
São verificadas as possibilidades de jogada da IA, e caso não haja nenhuma, passa a vez e a função é chamada novamente, passando de nível diretamente.

```
 if(tipo == "MAX"):
    possMax = -infit
    for poss in possibilidades:
        auxMax = miniMax("MINI", rec+1, poss, Mediador.cloneGame(game), alpha, beta, maxRec)
        possMax = max(possMax, auxMax)
            
        alpha = max(alpha, auxMax)
        if(beta <= alpha):
           break
                
   return possMax
 
elif(tipo == "MINI"):
   possMini = infit
   for poss in possibilidades:
       auxMini = miniMax("MAX", rec+1, poss, Mediador.cloneGame(game), alpha, beta, maxRec)
       possMini = min(possMini, auxMini)
            
       beta = min(beta, auxMini)
       if(beta <= alpha):
           break
    
    return possMini
```
Neste trecho é realizada a recursão de maximização ou minimização. Caso a arvore está em "MAX" é feita a recursão de maximização, caso o contrário, é realizada a de minimização. Observa-se a utilização da poda alfa e beta, na qual alfa recebe o maior valor da maximização, e beta o menor valor da minimização.


#### 2- escolheJogada(game, maxRec)

Este método é responsável por escolher a jogada de acordo com o resultado do MiniMax.


