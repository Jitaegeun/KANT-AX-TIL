"""README.md 내용이 첫 번째 셀에 들어간 새 노트북을 만든다.

python new_til.py             -> 오늘 날짜 노트북 (예: 2026.11.10.ipynb)
python new_til.py 2026.11.09  -> 이름을 직접 지정 (0바이트 빈 파일이면 내용을 채운다)
"""
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent

name = sys.argv[1] if len(sys.argv) > 1 else f"{date.today():%Y.%m.%d}"
notebook_path = ROOT / f"{name.removesuffix('.ipynb')}.ipynb"

# 내용이 있는 노트북은 절대 덮어쓰지 않는다
if notebook_path.exists() and notebook_path.stat().st_size > 0:
    sys.exit(f"이미 내용이 있는 파일이라 건드리지 않았어요: {notebook_path.name}")

readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")

notebook = {
    "cells": [
        {"cell_type": "markdown", "metadata": {}, "source": readme.splitlines(keepends=True)},
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": []},
    ],
    "metadata": {"language_info": {"name": "python"}},
    "nbformat": 4,
    "nbformat_minor": 4,
}

notebook_path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"만들었어요: {notebook_path.name}")
