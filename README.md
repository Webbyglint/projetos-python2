# Organizador de Arquivos

Script em Python que organiza os arquivos de uma pasta em subpastas por tipo
(Imagens, Documentos, Planilhas, Código etc.), tratando nomes duplicados e
oferecendo modo de simulação.

## Uso
```bash
python organizador.py ~/Downloads --simular   # só mostra o que faria
python organizador.py ~/Downloads             # organiza de verdade
```

## Testes
```bash
pip install pytest
pytest
```

## Conceitos aplicados
- `pathlib` e `shutil`
- Tratamento de conflito de nomes
- Modo dry-run (`--simular`)
- Testes automatizados com `pytest` e `tmp_path`
