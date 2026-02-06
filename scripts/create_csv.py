from __future__ import annotations

from pathlib import Path
import pandas as pd

# Ruta del dataset
DATASET_DIR = Path("data/raw/brain-tumor-mri-scans")


OUT_DIR = Path("data/processed")
OUT_CSV = OUT_DIR / "dataset.csv"

# Extensiones admitidas
IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}


def main() -> None:

    """
    Construye un CSV con las rutas de imágenes y sus etiquetas (clases).

    Recorre las subcarpetas de `DATASET_DIR` (cada una considerada una clase),
    busca imágenes de manera recursiva y crea un DataFrame con dos columnas:
    `img_path` y `label`. Posteriormente, baraja el DataFrame de forma
    reproducible y lo guarda en `OUT_CSV`.

    Returns:
        None
    """
    if not DATASET_DIR.exists():
        raise FileNotFoundError(
            f"Ruta no encontrada: {DATASET_DIR}"
        )

    rows = []
    class_dirs = [p for p in DATASET_DIR.iterdir() if p.is_dir()]
    if not class_dirs:
        raise RuntimeError(
            f"No se encuentra subcarpetas por clase dentro de {DATASET_DIR}."
        )

    for class_dir in sorted(class_dirs):
        label = class_dir.name
        for img_path in class_dir.rglob("*"):
            if img_path.is_file() and img_path.suffix.lower() in IMG_EXTS:
                
                rows.append({"img_path": img_path.as_posix(), "label": label})

    if not rows:
        raise RuntimeError(
            f"No se encuentra imágenes con extensiones {IMG_EXTS} dentro de {DATASET_DIR}."
        )

    df = pd.DataFrame(rows)


    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_CSV, index=False)

    print(f"=======CSV creado en: {OUT_CSV}========")
    print(f"=======Total imágenes: {len(df)}=======")
    print("========Distribución por clase: =========")
    print(df["label"].value_counts())


if __name__ == "__main__":
    main()
