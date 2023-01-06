# Pytest

Todo teste é formado por 3 etapas:

GWT:
- Given: dado
- When: quando
- Then: então

ou AAA:
- Arrange
- Act
- Assert

Resumo dos feedbacks:
- .: Passou
- F: Falhou
- x: Falha esperada
- X: Falha esperada, mas não falhou
- s: Pulou (skipped)


## Virtualenv

`conda create -n pytest-py310 python=3.10`

Ativando virtualenv:

`conda activate pytest-py310`


## Install:  
`conda install pytest`


## Run

1. Criar um diretório `tests/` ou `test/` na raiz.
2. Criar um arquivo .py com test_*.py ou *_test.py
3. Criar funções de teste dentro do arquivo python
   1. As funções devem começar com `def test_*():`
   2. Apenas um assert por função

Para rodar o pytest, executar no shell:
`pytest`

Opção verbose:
`pytest -v`

Para rodar até a primeira falha de teste:
`pytest -x`

Para debugger:
`pytest --pdb`

Filtrar testes:
`pytest -k "queijo"`
Filtra testes que tenham "queijo" no nome da função.

Mostrar os prints() do código:
`pytest -s`



## Marcações, argumentos e metadados

Fornece a possibilidade de criar grupos de testes.

```python
@mark.tag_name
def test_testa_algo():
    assert 1 == 1
```
onde `tag_name` é o nome da tag.

### XFAIL

Podemos deixar uma marcação de teste que irá falhar e sabemos disso. Por exemplo, o código irá falhar quando for executado em windows, e tá tudo bem:

```python
# Quando a coisa TEM que falhar
@mark.xfail(sys.platform == 'win32')
def test_no_windows_pode_falhar_xfail():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(20) != 'goiabada'
```

### SKIPIF
Pula o teste em alguma situação:

```python
@mark.platform_test
@mark.skipif(sys.platform == 'darvin', reason='sistema diferente')
def test_pode_pular_no_mac():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(20) == 'goiabada'
```


## FIXTURES

Fixture é basicamente uma maneira de "entrar" em um contexto. Ou prover uma ferramenta que precisa de sexecutada "antes" dos testes.

```python
@fixture
def flask_app():
    create_app()
```


## Relatório XML
`pytest --junitxml reports/report.xml`


## Outra lib de teste
- **​Behave**


## Referências
TDD - Kent Beck
- one step test

Learning Pytest 


live debugger: 85


xUnit Patterns - Gerard Mezaros
Um teste é composto por 4 passos:
- Setup - dado
- Exercise - quando
- Verify - entao
- TearDown - desmonta td antes que seja tarde