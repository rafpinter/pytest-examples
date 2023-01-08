from app import Quadro, Coluna, Tarefa
from pytest import mark

## TESTES
@mark.live_fixture
def test_nao_deve_existir_nenhuma_coluna_no_quadro(quadro):
    quantidade_de_colunas = len(quadro.colunas)
    assert quantidade_de_colunas == 0

@mark.live_fixture
def test_quando_inserir_uma_coluna_deve_existir_uma_coluna(quadro):
    quadro.inserir_coluna(Coluna(nome='A fazer'))
    assert len(quadro.colunas) == 1

@mark.live_fixture
def test_quando_inserir_a_fazendo_ela_deve_estar_no_quadro(quadro):
    quadro.inserir_coluna(Coluna(nome='Fazendo'))
    assert quadro.colunas[0].nome == 'Fazendo'
    
@mark.live_fixture
def test_quando_inserir_uma_tarefa_no_quadro_ela_deve_estar_na_primeira_coluna(quadro_com_coluna):
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Dormir'))
    assert len(quadro_com_coluna.colunas[0].tarefas) == 1

@mark.live_fixture
def test_quando_inserir_duas_tarefa_no_quadro_elas_devem_estar_na_primeira_coluna(quadro_com_coluna):
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Dormir'))
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Comer'))
    assert len(quadro_com_coluna.colunas[0].tarefas) == 2
    
@mark.live_fixture
def test_quando_mover_cartao_ele_deve_ir_para_coluna_segunte(quadro_com_colunas):
    tarefa = Tarefa('usar mascara')
    quadro_com_colunas.inserir_tarefa(tarefa)
    quadro_com_colunas.mover(tarefa)
    assert tarefa in quadro_com_colunas.colunas[1]

@mark.live_fixture
def test_quando_mover_cartao_ele_deve_ir_ser_removida_da_anterior(quadro_com_colunas):
    tarefa = Tarefa('usar mascara')
    quadro_com_colunas.inserir_tarefa(tarefa)
    quadro_com_colunas.mover(tarefa)
    assert tarefa not in quadro_com_colunas.colunas[0]
    
@mark.live_fixture
def test_exemplo_para_brincar(factory_boy_test):
    # breakpoint()
    ...
    
@mark.live_fixture
@mark.parametrize(
    'quadro_parametrizado',
    [
        [1]
    ],
    indirect=True # quando True, parametro é passado para fixture
)
def test_passando_parametros_para_fixture(quadro_parametrizado):
    ...