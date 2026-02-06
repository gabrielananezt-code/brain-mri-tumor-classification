from __future__ import annotations

import shutil
from pathlib import Path

import kagglehub


DATASET_SLUG = "rm1000/brain-tumor-mri-scans"
TARGET_DIR = Path("data/raw")

def _copy_tree(src: Path, dst: Path) -> None:
    """
    Copia recursivamente un directorio a otro, reemplazando el destino si existe.

    Si `dst` ya existe, se elimina completamente antes de realizar la copia,
    garantizando que el contenido final sea una réplica limpia de `src`.

    Args:
        src: Ruta del directorio origen que se desea copiar.
        dst: Ruta del directorio destino donde se copiará el contenido.
    """
    
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def main() -> None:
    """
    Descarga el dataset desde KaggleHub y lo copia a `data/raw`.

    Descarga el dataset definido por `DATASET_SLUG` usando KaggleHub y luego
    copia el contenido al directorio:
        `data/raw/brain-tumor-mri-scans`

    El directorio destino se recrea en cada ejecución para evitar inconsistencias
    por ejecuciones previas.

    Returns:
        None
    """
    print(f"========Descargando dataset desde KaggleHub: {DATASET_SLUG} =========")
    downloaded_path = Path(kagglehub.dataset_download(DATASET_SLUG))
    print(f"Ruta: {downloaded_path}")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    dst = TARGET_DIR / "brain-tumor-mri-scans"
    print(f"Copiando a: {dst.resolve()}")
    _copy_tree(downloaded_path, dst)

    print(f"Ruta Dataset: {dst.resolve()}")
    #print("Nota: data/raw está ignorado por .gitignore (no se sube a GitHub).")


if __name__ == "__main__":
    main()
