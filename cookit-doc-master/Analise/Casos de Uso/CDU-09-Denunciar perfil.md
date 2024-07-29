# [CDU-09] Denunciar perfil

## 1. Descrição
<p> Na tela de perfil, o usuário em denunciar na tela de perfil do usuário, escolhe um tópico e o descreve.
<p/>

## 2. Atores
  1. Usuário - humano, primário, ativo.
  
## 3. Gatilhos

## 4. Pré-condições
  1. O usuário(a) precisa estar cadastrado no sistema.
  2. O usuário(a) precisa estar logado no sistema.

## 5. Pós-condições
  1. O usuário(a) é denunciado.

## 6. Fluxo Principal
Extends [CDU-16](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/fatoracao/Doc/Analise/Casos%20de%20Uso/CDU-16-Visualizar%20Receita.md)
1. O usuário(a) clica no nome de quem postou a receita logo abaixo do nome da mesma;
2. O sistema apresenta o perfil do usuário;
3. O usuário(a) clica no ícone de bandeira no canto superior direito do perfil;
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
        
Alternativamente ao passo 1
1. O usuário(a) clica no ícone de perfil no canto superior direito da tela;
2. O sistema apresenta seu perfil;
3. O usuário(a) clica em "Seguindo" ou "Seguidores" logo abaixo da sua descrição de perfil;
4. O sistema apresenta perfis;
5. O usuário(a) clica no nome de um dos perfis;
6. O sistema apresenta o perfil;

Alternativamente ao passo 5.1
1. O usuário(a) descreve a denúnicia se o tópico escolhido foi "Outros";
2. O usuário(a) segue para o passo 6;

  

## 9. Regras de negócio
  - [[RN02]](Doc/visao.md)