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

Recomenda-se começar a função de teste ao contrário:
1. Escreve o `assert x == y`
2. Escreve os demais passos da função de teste até chegar no assert
3. Dá o nome para a função de teste

## Virtualenv

`conda create -n pytest-py310 python=3.10`

Ativando virtualenv:

`conda activate pytest-py310`

Se não funcionar de primeira, desativar todos os condas e ativar novamente.


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

Então, na hora de executar os testes, podemos executar somente os testes de uma determinada tag: `pytest -m tag_name`.

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
Fixture também é um jeito de não se repetir código. É usual deixar as fixtures em um arquivo `conftest.py` dentro do diretório `tests/`.

```python
@fixture(scope='function')
def quadro():
    return Quadro() # Fixture

def test_nao_deve_existir_nenhuma_coluna_no_quadro(quadro):
    quantidade_de_colunas = len(quadro.colunas)
    assert quantidade_de_colunas == 0
```
Passamos o nome da fixture no argumento da função de teste.


Quando utilizamos o `yield`, podemos ter uma parte de código executada depois da função de teste também:
```python
@fixture(scope='function')
def quadro():
    print('executado antes da função de teste')
    yield Quadro() # Fixture
    print('executado depois da função de teste')

def test_nao_deve_existir_nenhuma_coluna_no_quadro(quadro):
    quantidade_de_colunas = len(quadro.colunas)
    assert quantidade_de_colunas == 0
```

### "Herança" de fixtures
Uma fixture pode chamar outra para ser executada antes de si. Basta chamar a primeira no argumento da função da fixture em questão:

```python
@fixture(scope='function')
def quadro():
    yield Quadro() # Fixture

@fixture
def quadro_com_coluna(quadro):
    quadro.inserir_coluna(Coluna(fake.pystr()))
    return quadro

@fixture
def quadro_com_colunas(quadro_com_coluna):
    quadro_com_coluna.inserir_coluna(Coluna(fake.pystr()))
    return quadro_com_coluna
```


### Parâmetros para fixture
Podemos passar parametros para fixtures utilizando o `indirect=True`.

```python
@fixture
def quadro_parametrizado(request):
    breakpoint()
    return Quadro()

@mark.parametrize(
    'quadro_parametrizado',
    [
        [1]
    ],
    indirect=True # quando True, parametro é passado para fixture
)
def test_passando_parametros_para_fixture(quadro_parametrizado):
    ...
```

Neste caso, `quadro_parametrizado(request)` recebe o valor `request = [1]`


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