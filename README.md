## Projeto AppEventos
Projeto com o objetivo de inicialmente construir um design de classes coeso e claro, para criar uma estrutura orientada a objetos consistente e de fácil manutenção.

### Como o projeto está estruturado?

- **Abstrações :** Contém as classes que servem de base para a existência de outras, uma estrutura padrão para classes derivadas implementarem determinado comportamento. Pode conter classes normais, e classes de comportamento ( interfaces ).

- **Documentação :** Contém a modelagem das classes. Possui o arquivo de requisitos do projeto, e imagem + arquivo(tipo) com o diagrama.

- **Enums :** Nessa pasta estão os Enums implementados em python, onde cada um deles definem constantes e alguns atributos essenciais para poder servir de suporte à algumas implementações.

- **Modelo** : As classes responsável por implementar as entidades que interagem dentro do sistema, fazendo ele funcionar.

- **Testes :** Pacote responsável pelos testes de integridade e comportamento dos objetos que serão criados ao londo da app.
### E como ta a modelagem ?

![documentação/Diagrama%20AppEventos.png](Modelagem Dssign de Classes)

### E como executar ele ?

O projeto inicialmente não possui dependência.
Então é só dá um clone e começar a dá uma mexida. :+1:

```python
git clone https://github.com/Marlysson/AppEvents.git
cd AppEvents
...coding...
```

#### E para contribuir ?

Assim como em qualquer outro projeto os passos são basicamente esses.

```python
git clone https://github.com/Marlysson/AppEvents.git
git branch <funcionalidade> #Criar um branch para a sugestão
git push origin funcionalidade
```

E mandar um Pull Request do seu novo branch no repositório original.

