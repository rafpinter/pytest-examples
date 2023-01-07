from pytest import mark, fixture
from src.jogo import brincadeira
import sys

def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    
    # Dado
    entrada = 1
    esperado = 1
    
    # Quando
    resultado = brincadeira(entrada)
    
    # Então
    assert resultado == esperado


def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(2) == 2


def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(3) == 'queijo'


@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(5) == 'goiabada'

@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(10) == 'goiabada'

@mark.goiabada
@mark.smoke
def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(20) == 'goiabada'

@mark.skip(reason='not implemented yet')
def test_quando_brincadeira_receber__1_entao_deve_retornar_None():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(-1) == None


@mark.parametrizado
@mark.parametrize(
    'entrada',
    [5, 10, 20, 25, 35]
)
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    # TDD - Kent Beck - One-step Test
    assert brincadeira(entrada) == 'goiabada'

    
@mark.parametrizado
@mark.parametrize(
    'entrada',
    [3, 6, 9, 12, 18]
)
def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
    # TDD - Kent Beck - One-step Test
    assert brincadeira(entrada) == 'queijo'
    

## NÃO FAZER ESSA ABORDAGEM!!!!!!!
@mark.parametrizado
@mark.parametrize(
    'entrada,esperado',
    [(1,1), (2,2), (3,'queijo'), (4,4), (5,'goiabada')]
)
def test_brincadeira_deve_retornar_o_valor_esperado(entrada, esperado):
    # TDD - Kent Beck - One-step Test
    assert brincadeira(entrada) == esperado


# Quando a coisa TEM que falhar
@mark.xfail()
def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada_xfail1():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(20) == 'goiabada'

# Quando a coisa TEM que falhar, e podemos colocar alguma situação aqui
@mark.xfail(sys.platform == 'win32')
def test_no_windows_pode_falhar_xfail2():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(20) != 'goiabada'


@mark.platform_test
@mark.skipif(sys.platform == 'darvin', reason='sistema diferente')
def test_pode_pular_no_mac():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(20) == 'goiabada'


@mark.stdout
def test_brincadeira_deve_escrever_entrei_na_brincadeira(capsys):
    brincadeira(0)
    resultado = capsys.readouterr()
    assert resultado.out == 'entrei na brincadeira\n'
    
@fixture
def minha_fixture():
    """essa fixture é top mas nao ta ainda funcionando"""
    return 3

@mark.exemplo_fixture
def test_minha_fixture_em_acao(minha_fixture):
    print(minha_fixture)