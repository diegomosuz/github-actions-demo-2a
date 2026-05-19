"""
Módulo de ejemplo para Demo 2 - GitHub Actions.
Curso: Laboratorio de Minería de Datos - ISTEA
Profesor: Diego Mosquera

La función score_churn es deliberadamente simple: no busca ser un modelo real,
sino un caso mínimo para demostrar cómo GitHub Actions ejecuta pruebas automáticas.
"""


def score_churn(months_active: int, complaints: int) -> float:
    """
    Calcula un score simple de riesgo de churn entre 0.0 y 1.0.

    Reglas didácticas:
    - Todo cliente parte de un riesgo base de 0.2.
    - Si tiene menos de 6 meses de antigüedad, se suma 0.4.
    - Si tiene más de 2 reclamos, se suma 0.3.
    - El resultado final se limita a un máximo de 1.0.
    """
    score = 0.2

    if months_active < 6:
        score += 0.4

    if complaints > 2:
        score += 0.3

    return min(score, 1.0)
