from app import Coluna
from pytest import mark

@mark.live_fixture
def test_coluna_deve_ter_um_nome():
    assert Coluna("Fazendo").nome == "Fazendo"