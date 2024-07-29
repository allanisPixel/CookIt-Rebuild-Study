# [CDU-15] Validar Ingrediente

## 1. Descrição
- O moderador recebe a notificação da adição de um novo ingrediente ao
sistema e o aceita ou rejeita.
## 2. Atores
1. Moderador - Humano, secundário, ativo
## 3. Gatilhos
1. Um usuário cria um novo ingrediente durante o [registro de uma receita](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/master/Doc/Analise/Casos%20de%20Uso/CDU-02-Cadastro%20de%20receitas.md) e imediatamente é enviado a um moderador que irá avaliar se o ingrediente existe e é válido.
## 4. Pré-condições
1. O moderador precisa ser pré-cadastrado no sistema.
 	 
## 5. Pós-condições
1. Ingrediente Aceito
	1.1. A inclusão do ingrediente no sistema.
	1.2. A notificação do usuario que o ingrediente foi aceito e a receita está publica.

2. Ingrediente Rejeitado
	2.1. A inclusão do ingrediente no banco de invalidos.
	2.2. A notificação do usuario que o ingrediente não foi aceito, a razão e que receita está privada podendo ser corrigida para se tornar pública.
    
## 6. Fluxo Principal
1. O moderador entra no site;
2. O sistema lhe mostra a mesma tela inicial que mostraria para um usuário;
3. O moderador faz o login no sistema com sua conta de moderador;
4. O Sistema exibe uma tela com três seções: Validar Ingredientes, Bugs, Denuncias;
5. O moderador entra na seção Validar Ingredientes;
6. O sistema exibe uma lista de novos ingredientes e o nome da receita de origem. A lista é exibida das mais antigas para as mais novas, usando um sistema de cores destacando o tempo de espera da solicitação e destacando o status da avaliação (realizada ou pendenete) ;
7. O moderador seleciona uma das opções;
8. O sistema lhe mostra toda a receita e o ingrediente possivelmente novo destacado e as opções de validar;
9. O moderador clicar em validar;
10. O sistema exibe um aviso dizendo que a receita foi adicionada ao sistema;

## 7. Situações de erro

## 8. Fluxos alternativos
Rejetando Ingrediente:

Alternativo aos passos 9 e 10:
1. O moderador clica em "Rejeitar Ingrediente";
2. O sistema lhe pergunta o porque ele desaprova o ingrediente;
3. O moderador seleciona os motivos (radio butons com motivos genéricos a decidir) e clica em concluir; 
4. O sistema exibe uma mensagem informando que o usuario será notificado da desaprovação e dos motivos;

Reavaliando Ingrediente:
    
1. O moderador executa o caso de uso da mesma forma, porém a opção de validar já estará selecionada.

## 9. Regras de negócio
    