# [CDU-04] Avaliar receita

## 1. Descrição
- O usuário avalia a receita.

## 2. Atores
1. Usuário - Humano, primário, ativo

## 3. Gatilhos

## 4. Pré-Condições
  1. O usuário(a) precisa estar logado(a) no sistema.

## 5. Pós-Condições
1. A avaliação foi registrada;
2. A avaliação fica visível ao público;
3. O dono da receita recebe uma notificação.

## 6. Fluxo Principal
Extends [CDU-16](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/fatoracao/Doc/Analise/Casos%20de%20Uso/CDU-16-Visualizar%20Receita.md)
1. O sistema exibe, ao final da página, um campo de 5 estrelas (obrigatório) e um campo de comentário (opcional). [Tela](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2020.1/easy-cook/-/blob/master/Doc/Analise/Prototipo/Redesign%20%235/Tela%20receita%20completa.png);
2. O usuário escolhe uma nota de 0 a 5 estrelas, preenche o campo de comentário se desejar e clica em Avaliar;
3. O sistema retorna uma confirmação que a avaliação foi adicionada e notifica dono da receita.

## 7. Fluxo Alternativo

## 8. Situações de Erro

## 9. Regras de Negócio
 - [[RN0X - A Definir]](Doc/visao.md)
