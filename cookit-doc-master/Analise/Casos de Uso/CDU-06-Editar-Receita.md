# [CDU-07] Editar Receita

## 1. Descrição
- O usuário edita uma receita que ele publicou no sistema.

## 2. Atores
- Usuário - Humano, primário, ativo

## 3. Pré-Condições
1. O usuário(a) precisa estar logado(a) no sistema.

## 4. Pós-Condições
1. A edição da receita foi feita e atualizada;

## 5. Fluxo Principal
Extends [CDU-17](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/fatoracao/Doc/Analise/Casos%20de%20Uso/CDU-17-Visualizar%20meu%20perfil.md)
1. O usuário clica em receitas publicadas;
2. O sistema mostra uma lista de todas as receitas que o usuário publicou semelhante ao [prototipo](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20de%20favoritos.png);
3. O usuário clica em um botao de editar receita na receta que ele deseja com visto na [tela de perfil](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20de%20meu%20perfil.png);
4. O sistema o direciona para a tela de edição da receita igual a do [CDU-02](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/fatoracao/Doc/Analise/Casos%20de%20Uso/CDU-02-Cadastro%20de%20receitas.md)mas com campos já preenchidos;
5. O usuário edita a receita e clica em postar;
6. O sistema retorna para o passo “10” com uma mensagem que a receita foi editada com sucesso.

## 6. Fluxo Alternativo

## 7. Situações de Erro
- No passo 13 se o usuário deixar algum campo em branco e clicar em confirmar edição então o sistema o notificara para preencher os campos.
 
## 8. Regras de Negócio
