# Reflexões sobre o Exercício de Composição em Programação Orientada a Objetos

## Perguntas para Reflexão:

### 1. Como a composição facilita a criação de relações complexas entre objetos?
A composição permite que a gente construa objetos mais complexos juntando outros objetos. É como montar um quebra-cabeça: você tem várias peças que se encaixam de diferentes maneiras, criando algo novo. Isso facilita a criação de relações porque não precisamos ficar presos a uma hierarquia rígida. Se quisermos adicionar ou mudar algo, é só trocar uma peça, sem precisar remodelar todo o quebra-cabeça. Além disso, ela promove uma maior reutilização de código, já que podemos usar os mesmos componentes em contextos diferentes.

### 2. Qual é a vantagem de usar composição em vez de herança neste exercício?
A grande vantagem de usar composição aqui é a flexibilidade. Com herança, a gente acaba criando uma estrutura de classes que pode se tornar complexa e difícil de gerenciar, especialmente se precisar mudar alguma coisa mais tarde. A composição nos permite ter classes mais simples e independentes, o que facilita a manutenção e a adição de novas funcionalidades. Outra coisa é que, se quisermos, podemos até substituir um componente por outro mais facilmente, sem quebrar todo o sistema. Isso torna o código mais leve e adaptável.

### 3. Como o encapsulamento é utilizado nas classes Aluno, Curso e Escola?
O encapsulamento é uma forma de proteger nossos dados e métodos, e isso é super importante nas classes que criamos. Por exemplo, as classes `Aluno`, `Curso` e `Escola` podem ter atributos que não devem ser acessados diretamente de fora, como a lista de alunos dentro do `Curso`. Usar métodos públicos, como `adicionar_aluno` ou `mostrar_info`, nos permite controlar como esses dados são acessados e modificados. Assim, garantimos que, mesmo que alguém queira interagir com a classe, só pode fazê-lo de maneira segura e controlada. Isso ajuda a manter a integridade dos dados.

### 4. Como você pode estender este sistema para incluir novas funcionalidades, como notas dos alunos e professores para cada curso?
Para estender o sistema, eu poderia começar criando uma classe nova, tipo `Nota`, que armazenasse informações sobre as notas dos alunos em cada curso. Assim, a gente poderia associar uma nota específica a um aluno e a um curso. Também poderia adicionar uma classe `Professor` para gerenciar quem ensina quais cursos e como os alunos estão se saindo. Isso faria o sistema crescer de forma mais organizada. Além disso, poderia incluir métodos para calcular a média das notas e exibir relatórios de desempenho dos alunos. Dessa forma, o sistema ficaria mais completo e útil, cobrindo mais aspectos do ambiente escolar.
