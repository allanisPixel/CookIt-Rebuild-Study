# [CDU-05] Cadastrar usuário 

## 1. Descrição
 - O usuário solicita ao sistema um novo cadastro de perfil. Por sua vez, o sistema 
retorna um formulário para o preenchimento de dados do usuário a qual é completado. Ao final, 
é exibido uma mensagem de confirmação e o novo perfil é adicionado a plataforma.     
## 2. Atores
 1. Usuário - Humano, primário, ativo
## 3. Gatilhos
 
## 4. Pré-condições

## 5. Pós-condições
 1. O usuário terá um perfil cadastrado no sistema.

## 6. Fluxo Principal
 1. O usuario acessa o sistema.
 2. O sistema exibe a [tela principal](https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fgitlab.devops.ifrn.edu.br%2Ftads.cnat%2Fpdsweb%2F2020.1%2Feasy-cook%2F-%2Fblob%2Fmaster%2FDoc%2FAnalise%2FPrototipo%2FRedesign%2520%25235%2FTela%2520inicial.png)
 3. O usuário clica na opção de “Cadastrar-se”.
 4. O sistema exibe um formulário para [cadastro de perfil](https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fgitlab.devops.ifrn.edu.br%2Ftads.cnat%2Fpdsweb%2F2020.1%2Feasy-cook%2F-%2Fblob%2Fmaster%2FDoc%2FAnalise%2FPrototipo%2FRedesign%2520%25235%2FTela%2520de%2520cadastro-1.png).
 5. O usuário preenche o formulário com seu nome de usuário, email e senha.
 6. O usuário clica em "Aceito termos de uso e politica de privacidade do CookIt" e clica em cadastrar.
 7. O sistema exibe uma mensagem informando que o cadastro foi efetuado com sucesso.
 8. O sistema direciona a tela de cadastro para a página de [perfil do usuário](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20de%20meu%20perfil.png).
## 7. Situações de erro
 1. Situação do erro 1: O usuário insere dados inválidos. O email deve seguir o formato padrão e ser unico, o nome de usuario deve ter no minimo 2 caractes e ser unico e a senha deve ter 2 caracteres. 
    - Consequência: O sistema exibe uma mensagem informando que o usuário inseriu dados inválidos no formulário e solicita que o mesmo os informe novamente.
 
## 8. Fluxos alternativos

### Efetuar cadastro pela opção de login.
Alternativamente ao passo 3
1. O usuário clica na opção de “Login”.
2. O sistema exibe a tela de login e indica passo para cadastro, caso usuário não tenha acesso.
3. O usuário clica em “Cadastre-se”.
4. O sistema repete os passos 4 a 6 do fluxo principal.

## 9. Regras de negócio
  - [[RN01 - A Definir]](Doc/visao.md)
  - [[RN02 - A Definir]](Doc/visao.md)

