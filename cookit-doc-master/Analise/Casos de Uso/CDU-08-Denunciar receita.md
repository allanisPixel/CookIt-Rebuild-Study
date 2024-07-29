# [CDU-08] Denunciar receita

## 1. Descrição
<p> Na tela da receita completa, o usuário denuncia a receita escolhendo um tópico e informando a descrição do mesmo.
<p/>

## 2. Atores
  1. Usuário - humano, primário, ativo.
  
## 3. Gatilhos

## 4. Pré-condições
  1. O usuário(a) precisa estar cadastrado no sistema.
  2. O usuário(a) precisa estar logado no sistema.

## 5. Pós-condições
  1. A receita é denunciada.

## 6. Fluxo Principal
Extends [CDU-16](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/fatoracao/Doc/Analise/Casos%20de%20Uso/CDU-16-Visualizar%20Receita.md)

2. O sistema apresenta a [receita completavv](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/%2351-correcoes-prototipo/Doc/Analise/Prototipo/Redesing%20%234/Tela%20receita%20completa.png);
3. O usuário(a) clica no ícone de bandeira no canto superior direito da receita;
4. O sistema apresenta tópicos como opções de denúncia;
5. O usuário(a) clica em um dos tópicos;
    5.1. O usuário(a) clica em "Denunciar";
6. O sistema apresenta mensagem de denuncia efetuada;

## 7. Situações de erro
1. O usuário(a) tenta concluir a denúncia sem escolher um tópico.
    - Consequência: O sistema notifica a necessidade de escolha de um tópico.
2. O usuário(a) tenta concluir a denúncia sem a descrever.
    - Consequência: O sistema notifica a necessidade de descrição da denúncia.
        
## 8. Fluxos alternativos

Alternativamente ao passo 4
1. O usuário(a) descreve a denúnicia se o tópico escolhido foi "Outros";
2. O usuário(a) segue para o passo 5;


## 9. Regras de negócio
  - [[RN02]](Doc/visao.md)