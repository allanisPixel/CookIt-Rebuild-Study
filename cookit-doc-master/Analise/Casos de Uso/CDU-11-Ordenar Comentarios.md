# [CDU-11] Filtrar Comentários

## 1. Descrição
<p> 
Diante da página de descrição de uma receita, o usuário filtra os comentarios 
feitos sobre a receita.
<p/>

## 2. Atores
  1. Usuário(a) - humano, primário, ativo.
  
## 3. Gatilhos

## 4. Pré-condições

## 5. Pós-condições

## 6. Fluxo Principal
Extends [CDU-16](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/fatoracao/Doc/Analise/Casos%20de%20Uso/CDU-16-Visualizar%20Receita.md)
1. O sistema [apresenta o detalhamento da receita](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20receita%20completa.png);
2. O usuario se dirige ao final da página onde encontra-se os comentarios e
seleciona um botão que possue um menu "drop down" onde está escrito "Mais 
populares" e o botão lhe mostra as opções "Mais populares", "Mais recentes" 
e "Mais antigas";
3. O usuario seleciona uma das opções;
4. O sistema ordena os comentarios com a opção selecionada.

## 7. Situações de erro
        
## 8. Fluxos alternativos

## 9. Regras de negócio

## 10. Informações adicionais

<p>Os comentarios mais populares são aqueles que tem o maior numero de "gostei" 
e "não gostei" somados.<p/>