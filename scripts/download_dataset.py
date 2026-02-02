from __future__ import annotations

import shutil
from pathlib import Path

import kagglehub


DATASET_SLUG = "rm1000/brain-tumor-mri-scans"
TARGET_DIR = Path("data/raw")


def _copy_tree(src: Path, dst: Path) -> None:
    """Copia recursivamente src -> dst (reemplaza si existe)."""
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def main() -> None:
    print(f"📥 Descargando dataset desde KaggleHub: {DATASET_SLUG}")
    downloaded_path = Path(kagglehub.dataset_download(DATASET_SLUG))
    print(f"✅ KaggleHub lo descargó en: {downloaded_path}")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    dst = TARGET_DIR / "brain-tumor-mri-scans"
    print(f"📁 Copiando a: {dst.resolve()}")
    _copy_tree(downloaded_path, dst)

    print(f"✅ Dataset listo en: {dst.resolve()}")
    print("ℹ️ Nota: data/raw está ignorado por .gitignore (no se sube a GitHub).")


if __name__ == "__main__":
    main()
