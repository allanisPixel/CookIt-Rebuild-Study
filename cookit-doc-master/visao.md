# Documento de visão
# CookIt
## 1. Resumo

O software **CookIt** é um sistema web pensando em facilitar o preparo de alimentos mediante a necessidade do usuário que não encontra praticidade durante o processo. 
Considerando principalmente, barreiras que dificultam ao fazer pratos que não envolvam os ingredientes que possui em mãos e ou criatividade quando o assunto é cozinha. 
CookIt tem por sua vez, o intuito de proporcionar ao usuário o acesso facilitado através de filtros de busca que o estimulem a cozinhar receitas tirando a necessidade 
de comer fora de casa.

## 2. Cliente
<p>
Cliente não real/Concreto
</p>

## 3. Problema
### 3.1 Inesperiencia na cozinha
<p>
O usuário quer descobrir o que é possivel fazer com o que ele possui de ingredientes em casa.
<p/>

### 3.2 Falta de ingredientes
<p>
O usuário não quer comprar ingredientes extras para conseguir fazer uma receita,
no momento em que ele a lê. Inclusive ele quer saber se é possível haver 
substituições para evitar isso. 
</p>

### 3.3 Extra: Encontrar receitas com restrição
<p>
O usuário pode possuir restrições alimentares, pussui dificuldade de encontrar receitas
que atendam essas restrições e tambem quer saber se há alguma maneira de execultar uma
receita que possuiem ingredientes os quais eles são restritos, com os ingredientes que
eles podem consumir. 
</p>

## 4. Escopo
### 4.1. O Cookit é:
- Um buscador de receitas por meio de filtros e/ou palavras-chaves;
- Um livro de receitas virtual.
    
### 4.2. O Cookit não é:
- Um serviço de delivery;
- Um serviço de video-aulas.
- Um site especializado em nutrição.

### 4.3. O Cookit faz:
- Efetua busca de receitas por nome e filtros (Quero que tenha, Quero que não tenha);
- Possibilita cadastro de usuário(perfil);
- Possibilita visualização de detalhamento da receita(Ingredientes Padrão/Alternativo);
- Compartilhamento de receitas pelo usuário;
- Upload de receitas pelo usuário;
- Filtragem por nível de complexidade da receita;
- Indica receitas veganas;
- Avaliação pública da receita.

### 4.4. O Cookit não faz:
- Ranking de receitas (gameficação);
- Restringe as receitas por alérgicos;
- Possibilita altera receitas de outros usuários;
- Registra validade da receita;
- Possibilitar chat entre os usuários;
- Verificação de direitos autorais;
- Se responsabiliza por danos causados pelo consumo das receitas.

## 5. Usuários
### 5.1. Público em Geral:
<p>
Os usuarios do CookIt estão em uma faixa de idade entre 15 e 30 anos, possuem alguns ingredientes em casa com os quais não sabe bem o que fazer. Esses usuarios possuem pouco tempo para exercitar a culinaria e ou tambem pouca experiencia, más buscam preparar seu alimento em casa, economizando.Esse mesmo usuario tambem pode está buscando novas combinções e possibiliades com os ingredientes que ele possui no momento. 
</p> 
 
## 6. Requisitos funcionais
 * Buscar Receitas por Nome: possibilitar ao usuário a busca de receitas simplesmente pelo nome delas.
 * Buscar Receitas por Filtro: possibilitar ao usuário quando estiver logado no sistema buscar por receitas restringindo a busca com base em seus gostos.
 * Receitas Favoritas: possibilitar ao usuário quando logado no sistema adicionar as receitas de sua preferência na lista de favoritos.
 * Cadastrar Receitas: possibilitar ao usuário quando logado no sistema adicionar suas próprias receitas na plataforma.
 * Validar Ingredientes: possibilitar ao administrador quando logado no sistema validar novos ingredientes e adicioná-los ao banco de dados para geração de “tags” facilitando o filtro de busca.
 * Avaliar e Comentar Receitas: possibilitar os usuarios avaliarem a receita atraves de estrelas e fazerem comentários com criticas ou sujestões.
 * Recomendar Receitas: permitir que o sistema recomende novas receitas baseando-se em escolhas prévias dos usuários logados na plataforma.
 * Gerenciar perfis de usuários: o sistema terá a necessidade de estabelecer níveis de acesso de acordo ao papel do usuário.

## 7. Requisitos não-funcionais
 * Plataforma Web:Página web com funcionalidades de busca, filtragem e visualização de receitas pelos usuários.
 * Django Framework:Plataforma de desenvolvimento web back-end.
 * Vue:Plataforma de desenvolvimemto front-end.
 * Django Rest:Plataforma de desenvolvimemto da API.
 * Login Externo:Acessar o sistema a partir de outras redes como Facebook e Google.
 * Design Responsivo:Acesso a multiplataforma do sistema.
 * Banco de Dados:Sistemas de Gestão de Base de Dados PostgreSQL.
 * Docker:Plataforma para instalação de denpendencias da arquitetura do projeto.

## 8. Regras de negócio
- [RN01] O usuário não pode cadastrar duas contas com um mesmo e-mail.
- [RN02] O usuário pode avaliar a receita de 0 a 5.
- [RN03] o comentário da receita tem até 250 caracteres.
