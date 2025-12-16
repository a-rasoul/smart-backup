import shutil
from pathlib import Path
from datetime import datetime

def smart_backup(source: str, backup_root: str):
    source_path = Path(source)
    backup_root_path = Path(backup_root)

    if not source_path.exists():
        raise FileNotFoundError("Source directory does not exist.")

    now = datetime.now()
    backup_path = backup_root_path / str(now.year) / f"{now.month:02d}" / f"{now.day:02d}"
    backup_path.mkdir(parents=True, exist_ok=True)

    files = [f for f in source_path.iterdir() if f.is_file()]
    copied = 0

    for file in files:
        target = backup_path / file.name

        if target.exists():
            counter = 1
            while target.exists():
                target = backup_path / f"{file.stem}_{counter}{file.suffix}"
                counter += 1

        shutil.copy2(file, target)
        copied += 1

    print("Backup completed successfully.")
    print(f"Files copied: {copied}")
    print(f"Backup location: {backup_path}")

if __name__ == "__main__":
    source_dir = input("Source directory: ").strip()
    backup_dir = input("Backup root directory: ").strip()
    smart_backup(source_dir, backup_dir)
