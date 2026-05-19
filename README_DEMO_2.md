# Demo 2 — CI mínimo para proyecto Python con pytest

Curso: Laboratorio de Minería de Datos - ISTEA  
Profesor: Diego Mosquera

## Objetivo

Demostrar cómo GitHub Actions puede validar automáticamente un proyecto Python mínimo cada vez que se hace `push`, se abre un `pull_request` o se ejecuta el workflow manualmente desde GitHub.

## Estructura

```text
gh-actions-python/
├─ src/
│  ├─ __init__.py
│  └─ churn_score.py
├─ tests/
│  └─ test_churn_score.py
├─ requirements.txt
├─ .gitignore
└─ .github/
   └─ workflows/
      └─ ci.yml
```

## Probar localmente en Windows

Desde PowerShell, dentro de la carpeta del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```

Resultado esperado:

```text
3 passed
```

## Subir a GitHub

```powershell
git init
git branch -M main
git add .
git commit -m "Agrega demo 2 con CI Python"
git remote add origin https://github.com/TU_USUARIO/gh-actions-python.git
git push -u origin main
```

Luego abrir en GitHub:

```text
Repositorio → Actions → CI Python
```

## Qué hace el workflow

El archivo `.github/workflows/ci.yml` ejecuta estos pasos:

1. Descarga el repositorio en el runner con `actions/checkout@v4`.
2. Configura Python 3.11 con `actions/setup-python@v5`.
3. Instala las dependencias desde `requirements.txt`.
4. Ejecuta los tests con `pytest -q`.

## Ejercicio didáctico: romper un test

Editar `tests/test_churn_score.py` y cambiar esta línea:

```python
assert score_churn(months_active=24, complaints=0) == 0.2
```

por esta:

```python
assert score_churn(months_active=24, complaints=0) == 0.8
```

Luego:

```powershell
git add .
git commit -m "Rompe test intencionalmente"
git push
```

La ejecución de GitHub Actions debería fallar. El objetivo es entrar al run, abrir el job y leer el step fallido.
