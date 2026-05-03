# document-service


*** Begin Patch
*** Add File: tasks.py
+#!/usr/bin/env python3
+from pathlib import Path
+import os
+import sys
+import shutil
+from invoke import task
+
+# Корень проекта
+ROOT = Path(__file__).resolve().parent
+
+def _env(ctx):
+    env = os.environ.copy()
+    env["PYTHONPATH"] = str(ROOT)
+    return env
+
+
+@task
+def setup_dev(ctx):
+    """Установить dev-зависимости и сделать editable установку проекта."""
+    ctx.run("uv sync --all-extras --group dev")
+    ctx.run(f"{sys.executable} -m pip install -e .", env=_env(ctx))
+
+
+@task
+def install_editable(ctx):
+    """Установить проект в editable-режиме (pip install -e .)."""
+    ctx.run(f"{sys.executable} -m pip install -e .", env=_env(ctx))
+
+
+@task
+def run_storage(ctx):
+    """Запуск точки входа storage с PYTHONPATH, как модуль."""
+    ctx.run("uv run \"python -m src.composite.storage\"", env=_env(ctx))
+
+
+@task
+def run_api(ctx, host="0.0.0.0", port=8000, reload=True):
+    """Запуск FastAPI через uvicorn. Опционально с hot-reload."""
+    cmd = f"uvicorn src.application.main:app --host {host} --port {port}"
+    if reload:
+        cmd += " --reload"
+    ctx.run(cmd, env=_env(ctx))
+
+
+@task
+def test(ctx):
+    """Запуск тестов через pytest (через uv)."""
+    ctx.run("uv run pytest tests/", env=_env(ctx))
+
+
+@task
+def lint(ctx):
+    """Запуск Ruff для проверки кода."""
+    ctx.run("uv run ruff check .", env=_env(ctx))
+
+
+@task
+def format(ctx):
+    """Проверка/форматирование кода Ruff."""
+    ctx.run("uv run ruff format .", env=_env(ctx))
+
+
+@task
+def pre_commit(ctx):
+    """Запуск pre-commit хуков."""
+    ctx.run("uv run pre-commit run --all-files", env=_env(ctx))
+
+
+@task
+def clean(ctx):
+    """Очистка кэшей и артефактов сборки."""
+    # Удаляем кэши pytest/pycache
+    for p in ROOT.rglob(".pytest_cache"):
+        if p.is_dir():
+            shutil.rmtree(p, ignore_errors=True)
+        else:
+            try:
+                p.unlink()
+            except Exception:
+                pass
+    for p in ROOT.rglob("__pycache__"):
+        shutil.rmtree(p, ignore_errors=True)
+    # Удаляем Ruff кэш и uv.lock, если есть
+    for p in ROOT.rglob(".ruff_cache"):
+        if p.is_dir():
+            shutil.rmtree(p, ignore_errors=True)
+        else:
+            try:
+                p.unlink()
+            except Exception:
+                pass
+    for p in ROOT.rglob("uv.lock"):
+        if p.is_file():
+            p.unlink()
+    print("Cleaned caches and artifacts.")
*** End Patch
