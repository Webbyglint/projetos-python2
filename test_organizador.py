from pathlib import Path

from organizador import categoria_do_arquivo, destino_sem_conflito, organizar


def test_categoria_conhecida():
    assert categoria_do_arquivo(Path("foto.PNG")) == "Imagens"
    assert categoria_do_arquivo(Path("script.py")) == "Codigo"


def test_categoria_desconhecida():
    assert categoria_do_arquivo(Path("arquivo.xyz")) == "Outros"


def test_destino_sem_conflito(tmp_path):
    (tmp_path / "a.txt").write_text("1")
    assert destino_sem_conflito(tmp_path / "a.txt").name == "a_1.txt"


def test_organizar_move_arquivos(tmp_path):
    (tmp_path / "relatorio.pdf").write_text("x")
    (tmp_path / "foto.jpg").write_text("x")
    resumo = organizar(tmp_path, simular=False)
    assert (tmp_path / "Documentos" / "relatorio.pdf").exists()
    assert (tmp_path / "Imagens" / "foto.jpg").exists()
    assert resumo["Documentos"] == 1


def test_simulacao_nao_move(tmp_path):
    (tmp_path / "foto.jpg").write_text("x")
    organizar(tmp_path, simular=True)
    assert (tmp_path / "foto.jpg").exists()
