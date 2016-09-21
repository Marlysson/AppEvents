# Projeto AppEventos
Projeto com o objetivo de inicialmente construir um design de classes coeso e claro, para criar uma estrutura orientada a objetos consistente e de fácil manutenção.

## Como o projeto está estruturado?

- **Abstrações :** Contém as classes que servem de base para a existência de outras, uma estrutura padrão para classes derivadas implementarem determinado comportamento. Pode conter classes normais, e classes de comportamento ( interfaces ).

- **Documentação :** Contém a modelagem das classes. Possui o arquivo de requisitos do projeto, e imagem + arquivo modelado( no software astah ) com o diagrama.

- **Fábricas :** Aqui ficarão classes responsáveis pela construção de objetos, não expondo o construtor do mesmo, assim , encapsulando o processo de criação dos objetos.

- **Enums :** Nessa pasta estão os Enums implementados em python, onde cada um deles definem constantes e alguns atributos essenciais para poder servir de suporte à algumas implementações.

- **Modelo :** As classes responsáveis por implementar as entidades que interagem dentro do sistema, fazendo ele funcionar.

- **Services :** Nessa pasta estarão localizados as classes que servirão de suporte para representar algum comportamento/abstração de alguma lib built-in do Python , criando uma abstração legível para se trabalhar no modelo.

>Exemplo:

- Abstração da lib date e tratamento de intervalos de tempo.

```python
>>> horario = Horario()
>>> horario.mais("1 dia")
21/09/2016 07:50
```

```python
>>> duracao = Duracao(horario,durando="20 minutos")
>>> duracao.inicio
21/09/2016 07:50
>>> duracao.final
21/09/2016 08:10
```

- **Testes :** Pacote responsável pelos testes de integridade e comportamento dos objetos que serão criados ao longo da app. Cada requisito do pdf que está em documentação há um teste na medida do possível para ele.

## E como está a modelagem ?

![Modelagem Design de Classes](/documentação/Diagrama%20AppEventos.png)

## E como executar ele ?

O projeto inicialmente não possui dependência.
Então é só dá um clone e começar a dá uma mexida. :smile: :+1:

```python
git clone https://github.com/Marlysson/AppEvents.git
cd AppEvents
...coding...
```

#### Testando
> Recomenda-se a versão 3.x do Python.

Basta entrar na pasta **testes** do projeto e rodar o comando:
```python
python3 -m unittest discover
```

Assim rodará todos os testes que estão na pasta respectiva. :+1:


## E para contribuir ?

Assim como em qualquer outro projeto os passos são basicamente esses.

```python
git clone https://github.com/Marlysson/AppEvents.git
git branch <funcionalidade> #Criar um branch para a sugestão
git push origin funcionalidade
```

E mandar um Pull Request do seu novo branch no repositório original.

