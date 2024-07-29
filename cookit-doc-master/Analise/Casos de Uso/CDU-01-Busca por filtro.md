# [CDU-01] Busca por Filtro

## 1. Descrição
<p> O usuário insere os ingredientes de sua preferência, visualiza um conjunto 
de receitas associadas e seleciona uma delas. <p/>

## 2. Atores
1. Usuário(a)- Humano, primário, ativo
2. Visitante - Humano, primário, ativo
    
## 3. Gatilhos

## 4. Pré-condições
1. As receitas precisam estar cadastradas no sistema;
2. Os ingredientes precisam estar cadastrados no sistema.
    
## 5. Pós-condições
1. A visualização de um conjunto de receitas associadas a busca.
    
## 6. Fluxo Principal
1. O usuário acessa o sistema;
2. O Sistema exibe a tela inicial tal qual o [prototipo](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20inicial.png), com destaque para três seções: "Quero que tenha" (que pode ser modificada para "Quero que tenha somente"), "Quero que não tenha" e a area de busca pelo nome; 
3. O usuário digita no campo "Quero que tenha somente" todos os ingredientes de sua preferencia da seguinte forma: 
  - 3.1. O usuário digita no campo antes citado o nome do ingrediente e o sistema 
    exibe uma lista de ingredientes similares ao texto digitado; 
  - 3.2. O usuário clica em uma das opções;
  - 3.3. O sistema transforma a opção em uma tag listada;
4. O usuário clica em buscar;
5. O sistema irá atualizar a tela inicial exibindo uma lista de receitas que utilizam estritamente os ingredientes selecionados;
6. O usuário clica na receita de sua preferência;
7. O sistema retorna o detalhamento da receita;
8. O usuário visualiza o detalhamento da receita como no [prototipo](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20receita%20completa.png) .

## 7. Situações de erro
  - Situação do erro 1: O usuário insere dados inválidos no campo de filtro;
  - Consequência: O sistema exibe uma mensagem de erro avisando ao usuário que
    ele inseriu uma informação inválida e solicita e o mesmo insira um ingrediente
    válido.
  - Situação de erro 2: Usuário inclui um ingrediente no campo "quero apenas" 
    ou no campo "quero esses e me mostre mais" e em seguida inclui esse mesmo 
    ingrediente no campo "não quero que tenha" ou o inverso; 
  - Consequência: A tag será criada no último campo solicitado e apagada do anterior.

## 8. Fluxos alternativos
### Utilizando o campo "não quero que tenha"
    
Alternativamente ao passo 3 até o 3.3
    
1. O usuário digita no campo "Não quero que tenha" todos os ingredientes dos quais não quer da seguinte forma: 
  -1.1. O usuário digita no campo antes citado o nome do ingrediente e o sistema exibe uma lista de ingredientes similares ao texto digitado; 
    -1.2. O usuário clica em uma das opções;
    -1.3. O sistema transforma a opção em uma tag listada;
2. Ao final o sistema irar exibir uma lista de receitas onde nenhuma apresenta os ingredientes que o usuario solicitou que não tivesse.  
    
### Utilizando o campo "não quero que tenha" e “Quero que tenha somente” simultaneamente
    
1. O usuário digita no campo "Não quero que tenha" todos os ingredientes dos quais não quer da seguinte forma: 
  -1.1. O usuário digita no campo antes citado o nome do ingrediente e o sistema exibe uma lista de ingredientes similares ao texto digitado; 
  -1.2. O usuário clica em uma das opções;
  -1.3. O sistema transforma a opção em uma tag listada;
2. Em seguida o usuário digita no campo "Quero que tenha somente" todos os ingredientes de sua preferencia da seguinte forma: 
  -2.1. O usuário digita no campo antes citado o nome do ingrediente e o sistema exibe uma lista de ingredientes similares ao texto digitado; 
  -2.2. O usuário clica em uma das opções;
  -2.3. O sistema transforma a opção em uma tag listada;    
3. Ao final o sistema irar exibir uma lista de receitas onde nenhuma apresenta os ingredientes que o usuario solicitou que não tivesse e ao mesmo tempo essas receitas possuem apenas os ingredientes que o usuario solicitou que houvessem.

### Utilizando o campo "não quero que tenha" e “Quero que tenha” simuntaneamente
    
  1. O usuário digita no campo "Não quero que tenha" todos os ingredientes dos
     quais não quer da seguinte forma: 
    -1.1. O usuário digita no campo antes citado o nome do ingrediente e o 
           sistema exibe uma lista de ingredientes similares ao texto digitado; 
    -1.2. O usuário clica em uma das opções;
    -1.3. O sistema transforma a opção em uma tag listada;
  2. Em seguida o usuário digita no campo "Quero que tenha" todos os 
     ingredientes de sua preferencia da seguinte forma: 
    -2.1. O usuário digita no campo antes citado o nome do ingrediente e o 
          sistema exibe uma lista de ingredientes similares ao texto digitado; 
    -2.2. O usuário clica em uma das opções;
    -2.3. O sistema transforma a opção em uma tag listada;    
  3. Ao final o sistema irar exibir uma lista de receitas onde nenhuma 
     apresenta os ingredientes que o usuario solicitou que não tivesse e 
     ao mesmo tempo essas receitas possuem os ingredientes que o usuario
     solicitou que houvessem.

## 9. Regras de negócio
  - [[RN1]](Doc/visao.md)