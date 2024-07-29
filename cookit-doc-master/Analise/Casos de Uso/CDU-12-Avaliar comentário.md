# [CDU-12] Avaliar Comentário

## 1. Descrição
- O usuário avalia um comentário de uma receita.

## 2. Atores
1. Usuário(a) - Humano, primário, ativo.

## 3. Gatilhos

## 4. Pré-Condições
1. O usuário(a) precisa estar logado(a) no sistema.
2. A receita precisa estar cadastrada no sistema;

## 5. Pós-Condições
1. A avaliação é contabilizada de acordo com a escolha do usuário;
2. O dono do comentário pode receber uma notificação (de acordo com a configuração de notificação do mesmo).

## 6. Fluxo Principal
1. O sistema exibe, ao final da página, uma sessão de avaliações feitas com relação à receita, com seus respectivos comentários, caso feitos. Cada uma possui as opções "Gostei" e "Não Gostei". [Tela](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20receita%20completa.png);
2. O usuário clica em uma das opções para uma avaliação.
3. O sistema atualiza o valor da opção selecionada e notifica o dono da avaliação de acordo com a configuração do mesmo.

## 7. Fluxo Alternativo

## 8. Situações de Erro
- O comentário é apagado antes da ação ser feita:
    - Consequência: o sistema retorna um aviso de que a operação não pôde ser concluída.

## 9. Regras de Negócio
 - [[RN0X - A Definir]](Doc/visao.md)
