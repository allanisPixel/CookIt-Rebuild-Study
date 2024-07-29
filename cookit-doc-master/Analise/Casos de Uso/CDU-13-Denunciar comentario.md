# [CDU-13] Denunciar comentário 

## 1. Descrição
 -  O usuário lê a aba de comentários e encontra algo irregular. O mesmo denúncia o comentário em questão e aguarda que seja analisado e julgado de acordo as diretrizes do sistema.  
## 2. Atores
  1. Usuário(a) - Humano, primário, ativo
## 3. Gatilhos
  1. Usuário visualiza algo de errado na aba comentários.
## 4. Pré-condições
  1. O usuário(a) precisa estar logado(a) no sistema.
  2. O comentário deve ser existir.
## 5. Pós-condições
  1. O sistema rceberá a solicitação de análise do comentário denunciado.

## 6. Fluxo Principal
Extends [CDU-16](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/fatoracao/Doc/Analise/Casos%20de%20Uso/CDU-16-Visualizar%20Receita.md)
1. O usuário clica em um dos comentários e verifica que o mesmo possui aspectos ofensivos de acordo às regras da plataforma.
2. O usuário clica na opção de denúncia localizada no canto superior direito do comentário.
3. O sistema retorna opções clicáveis como: "Inapropriado", "Ofensivo", "Spam" e "Outros".
4. O usuário seleciona a opção que melhor se qualifica.
5. O sistema retorna uma mensagem informando que o comentário será encaminhado para o setor administrativo da aplicação e retornará uma notificação com resultado da análise.

## 7. Situações de erro
 
## 8. Fluxos alternativos

## 9. Regras de negócio
  
