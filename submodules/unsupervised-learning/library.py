"""
Funtions for module 3 of the Data Science bootcamp
"""
import random

from scipy.stats import norm, t

from constants import STUDENTS_DS


def z_or_t_score(
        confidence: float = 0.95, distribution: str = 'N', df: int = 99
) -> float:
    """
    Compute Z or T score depending for a given confidence level.
    It uses the critical value for a two-tailed test from a normal
    or t-student distribution.

    INPUT
    confidence: Confidence level for the test
    distribution: Distribution to use. Can be 'N' for normal or 'T'
    for t-student

    RETURNS
    z_alpha_2: Critical value for the test
    """

    assert 0 < confidence < 1, 'Confidence level must be between 0 and 1'

    assert distribution in ['N', 'T'], 'Distribution must be N or T'

    alpha_2 = (1 - confidence) / 2

    if distribution == 'N':

        z_alpha_2 = norm.ppf(1-alpha_2)

        return z_alpha_2

    t_alpha_2 = t.ppf(1-alpha_2, df=df)

    return t_alpha_2


def random_student() -> str:
    """"
    Seleccionar un estudiante al azar de la lista de estudiantes
    de data science.

    RETURNS
    name: Nombre del estudiante seleccionado
    """

    name = random.choice(STUDENTS_DS)

    return name


def n_random_students(n_students: int) -> list:
    """
    Seleccionar n estudiantes al azar de la lista de estudiantes
    de data science.

    INPUT
    n_students: Cantidad de estudiantes a seleccionar

    RETURNS

    students: Lista con los nombres de los estudiantes seleccionados
    """

    students = random.sample(STUDENTS_DS, n_students)

    return students
