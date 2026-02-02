from __future__ import annotations

from pathlib import Path
import pandas as pd

# Ruta del dataset (ajusta si tu carpeta es distinta)
DATASET_DIR = Path("data/raw/brain-tumor-mri-scans")

# Salida
OUT_DIR = Path("data/processed")
OUT_CSV = OUT_DIR / "dataset.csv"

# Extensiones válidas
IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}


def main() -> None:
    if not DATASET_DIR.exists():
        raise FileNotFoundError(
            f"No encuentro {DATASET_DIR}. Revisa la ruta o ejecuta primero download_dataset.py"
        )

    rows = []
    class_dirs = [p for p in DATASET_DIR.iterdir() if p.is_dir()]
    if not class_dirs:
        raise RuntimeError(
            f"No encontré subcarpetas por clase dentro de {DATASET_DIR}."
        )

    for class_dir in sorted(class_dirs):
        label = class_dir.name
        for img_path in class_dir.rglob("*"):
            if img_path.is_file() and img_path.suffix.lower() in IMG_EXTS:
                # Ruta relativa al proyecto (portable)
                rows.append({"img_path": img_path.as_posix(), "label": label})

    if not rows:
        raise RuntimeError(
            f"No encontré imágenes con extensiones {IMG_EXTS} dentro de {DATASET_DIR}."
        )

    df = pd.DataFrame(rows)

    # Mezcla para que luego el split sea más estable
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_CSV, index=False)

    print(f"✅ CSV creado en: {OUT_CSV}")
    print(f"📌 Total imágenes: {len(df)}")
    print("📌 Distribución por clase:")
    print(df["label"].value_counts())


if __name__ == "__main__":
    main()
