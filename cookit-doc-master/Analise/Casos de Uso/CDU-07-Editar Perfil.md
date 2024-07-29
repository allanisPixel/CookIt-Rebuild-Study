# [CDU-28] Editar Perfil 

## 1. Descrição
 - O usuário efetua alterações de seus dados cadastrados no perfil.
## 2. Atores
 1. Usuário - Humano, primário, ativo
## 3. Gatilhos

## 4. Pré-condições
  1. O usuário(a) precisa estar logado(a) no sistema.
## 5. Pós-condições
  1. O usuário terá seu perfil alterado.

## 6. Fluxo Principal
Extends [CDU-17](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/fatoracao/Doc/Analise/Casos%20de%20Uso/CDU-17-Visualizar%20meu%20perfil.md)
1. O usuário clica na opção de “Editar Perfil”.
2. O sistema solicita a senha do usuário.
3. O usuário preenche o campo senha.
4. O sistema exibe  [formulário de alteração](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/%2351-correcoes-prototipo/Doc/Analise/Prototipo/Redesing%20%234/Tela%20de%20edi%C3%A7%C3%A3o%20de%20perfil.png).
5. O usuário efetua a mudança nos dados de sua preferência e clica em salvar.
6. O sistema exibe uma mensagem informando que os dados foram alterados com sucesso.

## 7. Situações de erro
 1. Situação do erro 1: O usuário insere dados inválidos.
    - Consequência: O sistema exibe uma mensagem informando que o usuário inseriu dados inválidos no formulário e solicita que o mesmo os informe novamente.
 2. Situação do erro 2: O usuário tenta cadastrar email já existente no sistema.
    - Consequência: O sistema exibe uma mensagem informando que o usuário inseriu um email já cadastrado solicitando que insira informações válidas. 


## 8. Fluxos alternativos

## 9. Regras de negócio
 - [[RN03]](Doc/visao.md)
 - [[RN04]](Doc/visao.md)

