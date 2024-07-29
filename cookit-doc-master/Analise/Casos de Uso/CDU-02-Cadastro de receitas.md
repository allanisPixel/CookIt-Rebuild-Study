# [CDU-02] Cadastro de Receitas 

## 1. Descrição
<p> O usuário adiciona uma receita no sistema, visualiza um formulário e o preenche. 
Ao final, é exibida uma mensagem de confirmação e a receita é adicionada a plataforma. <p/>

## 2. Atores
  1. Usuário(a) - humano, primário, ativo.
  
## 3. Gatilhos

## 4. Pré-condições
  1. O usuário(a) precisa estar logado(a) no sistema.
  
## 5. Pós-condições
  1. A receita é cadastrada no sistema.

## 6. Fluxo Principal

1. O usuário clica no botão de cadastrar nova receita, na [página inicial](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsdistribuido/2020.2/cookit/cookit/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20inicial.png); O sistema exibe o formulário de cadastro de receita de acordo com o [prototipo](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsdistribuido/2020.2/cookit/cookit/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20de%20cadastro%20de%20receita.png);
2. O usuário faz upload de fotos;
.  O usuário seleciona os ingredientes, um a um, da seguinte maneira:
- 2.1. O usuário começa a preencher o nome do ingrediente;
- 2.2. O sistema exibe uma lista de ingredientes com base no nome;
- 2.3. O usuário seleciona um dos ingredientes da lista;
- 2.4. O sistema apresenta caracteristicas para cada ingrediente (unidade de medida e quantidade);
- 2.5. O usuario seleciona a unidade de medida preenche a quantidade;
3. O usuário seleciona as categorias, uma a uma, a partir de uma lista predeterminada;
4. O usuário preenche o modo de preparo;
5. O usuário preenche nos campos das caracteristicas essenciais as porções da receita o tempo de preparo e a dificuldade da receita (fácil, medio e dificil, super);
6. O usuário preenche o campo das observações adicionais;
7. O usuario clica em "Publicar";
8. O sistema exibe uma mensagem de sucesso e retorna a [página inicial](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsdistribuido/2020.2/cookit/cookit/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20inicial.png).


## 7. Situações de erro
1. O usuário tenta enviar o formulário de cadastro de receitas vazio ou com algum campo obrigatório vazio (nome, ingredientes, modo de preparo, categorias, porções, tempo de preparo, dificuldade).
- Consequência: o sistema notifica quais campos obrigatórios não foram preenchidos.
2. O sistema detecta que pelo menos 1 o ingrediente da lista não é referenciado no modo de preparo.
- Consequência: o sistema notifica que todos os ingredientes da lista precisam ser referenciados no modod de preparo.

## 8. Fluxos alternativos
  
## 9. Regras de negócio
- [[RN02]](Doc/visao.md)
- [[RN03]](Doc/visao.md)
- [[RN0?]](Doc/visao.md)

