# [CDU-03] Favoritar Receita

## 1. Descrição
<p>O usuário adiciona uma receita que ele gostou na sua lista de favoritos.<p/>

## 2. Atores
  1. Usuário(a) - humano, primário, ativo.
  
## 3. Gatilhos

## 4. Pré-condições
  1. O usuário(a) precisa estar logado(a) no sistema.

## 5. Pós-condições
  1. A receita é adiciona da lista de favoritos.

## 6. Fluxo Principal
Extends [CDU-01](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/fatoracao/Doc/Analise/Casos%20de%20Uso/CDU-01-Busca%20por%20filtro.md) 
1. O usuario clica no ícone de adicionar receita aos favoritos na miniatura;
2. O sistema exibe uma mensagem indicando que a receita foi adicionada a lista de favoritos.

## 7. Situações de erro
  
## 8. Fluxos alternativos
Alternativamente ao passo 1
  1. O sistema apresenta a [receita completa](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20receita%20completa.png);
  2. O usuario clica no ícone de adicionar receita;
Alternativamente ao passo 1
  1. O usuário pode selecionar sua própria receita e clicar no ícone de adicionar aos favoritos.
  
## 9. Regras de negócio
  - [[RN02]](Doc/visao.md)
