#!/usr/bin/env python3
"""Organiza os arquivos de uma pasta em subpastas por categoria."""
import argparse
import shutil
from collections import Counter
from pathlib import Path

CATEGORIAS = {
    "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"},
    "Documentos": {".pdf", ".doc", ".docx", ".txt", ".odt", ".md"},
    "Planilhas": {".xls", ".xlsx", ".csv", ".ods"},
    "Codigo": {".py", ".js", ".html", ".css", ".java", ".sql", ".json"},
    "Compactados": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Audio_Video": {".mp3", ".wav", ".mp4", ".mkv", ".avi"},
}


def categoria_do_arquivo(arquivo: Path) -> str:
    ext = arquivo.suffix.lower()
    for nome, extensoes in CATEGORIAS.items():
        if ext in extensoes:
            return nome
    return "Outros"


def destino_sem_conflito(destino: Path) -> Path:
    """Se já existir um arquivo com o mesmo nome, adiciona um sufixo numérico."""
    if not destino.exists():
        return destino
    contador = 1
    while True:
        novo = destino.with_name(f"{destino.stem}_{contador}{destino.suffix}")
        if not novo.exists():
            return novo
        contador += 1


def organizar(pasta: Path, simular: bool) -> Counter:
    resumo = Counter()
    for arquivo in sorted(pasta.iterdir()):
        if not arquivo.is_file() or arquivo.name.startswith("."):
            continue
        categoria = categoria_do_arquivo(arquivo)
        pasta_destino = pasta / categoria
        destino = destino_sem_conflito(pasta_destino / arquivo.name)

        print(f"{'[SIMULAÇÃO] ' if simular else ''}{arquivo.name} -> {categoria}/")
        if not simular:
            pasta_destino.mkdir(exist_ok=True)
            shutil.move(str(arquivo), str(destino))
        resumo[categoria] += 1
    return resumo


def main() -> None:
    parser = argparse.ArgumentParser(description="Organiza arquivos por tipo")
    parser.add_argument("pasta", type=Path, help="pasta a ser organizada")
    parser.add_argument(
        "--simular", action="store_true",
        help="mostra o que seria feito sem mover nada",
    )
    args = parser.parse_args()

    if not args.pasta.is_dir():
        parser.error(f"'{args.pasta}' não é uma pasta válida.")

    resumo = organizar(args.pasta, args.simular)
    print("\nResumo:")
    if not resumo:
        print("  Nenhum arquivo para organizar.")
    for categoria, qtd in resumo.most_common():
        print(f"  {categoria}: {qtd}")


if __name__ == "__main__":
    main()
