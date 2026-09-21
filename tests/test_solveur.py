"""
Fichier : test_solveur.py

Concepts clés de cet exemple:

pytest.raises(...) : Permet de vérifier qu'une exception appropriée
est bien levée si a == 0.

pytest.approx(...) : Indispensable pour comparer des résultats de
division ou de racines carrées sans bloquer sur des micro-arrondis de
nombres flottants (ex: 0.3333333333333333).

@pytest.mark.parametrize : Permet de factoriser les tests en injectant
plusieurs jeu de données (a, b, c) dans une seule fonction de test.
"""

import pytest
from solveur import resoudre_second_degre


# ====================================================
# 1. CAS DU DISCRIMINANT POSITIF (> 0) -> 2 solutions réelles
# ====================================================

def test_deux_solutions_entieres():
    # x^2 - 5x + 6 = 0 => Delta = 25 - 24 = 1 => x1 = 2, x2 = 3
    assert resoudre_second_degre(1, -5, 6) == (2.0, 3.0)


def test_deux_solutions_avec_a_negatif():
    # -x^2 + x + 2 = 0 => x1 = -1, x2 = 2
    assert resoudre_second_degre(-1, 1, 2) == (-1.0, 2.0)


# ====================================================
# 2. CAS DU DISCRIMINANT NUL (= 0) -> 1 solution double
# ====================================================

def test_une_solution_double():
    # x^2 - 4x + 4 = 0 => Delta = 0 => x0 = 2
    assert resoudre_second_degre(1, -4, 4) == (2.0,)


# ====================================================
# 3. CAS DU DISCRIMINANT NÉGATIF (< 0)
# ====================================================

def test_aucune_solution_reelle():
    # x^2 + x + 1 = 0 => Delta = 1 - 4 = -3
    x1, x2 = resoudre_second_degre(1, 1, 1)

    assert type(x1) == complex
    assert type(x2) == complex


# =====================================================
# 4. GESTION DES ERREURS & VALEURS LIMITES
# =====================================================

def test_coefficient_a_nul_leve_exception():
    # Si a = 0, ce n'est pas du second degré
    with pytest.raises(
        ValueError,
        match="Le coefficient 'a' ne peut pas être nul"
    ):
        resoudre_second_degre(0, 2, 3)


def test_solutions_avec_flottants_imprecis():
    # 3x^2 - 10x + 3 = 0 => x1 = 1/3, x2 = 3
    sol1, sol2 = resoudre_second_degre(3, -10, 3)

    assert sol1 == pytest.approx(1 / 3)
    assert sol2 == pytest.approx(3.0)


# =====================================================
# 5. BONUS : TEST PARAMÉTRÉ
# =====================================================

@pytest.mark.parametrize(
    "a, b, c, resultat_attendu",
    [
        (1, -3, 2, (1.0, 2.0)),
        (1, -2, 1, (1.0,)),
        (1, 0, 4, (-2j, 2j)),
    ],
)
def test_resolution_parametree(a, b, c, resultat_attendu):
    assert resoudre_second_degre(a, b, c) == resultat_attendu


# =======================================================
# TESTS POUR DELTA NÉGATIF (< 0) -> Solutions complexes
# =======================================================

def test_delta_negatif_solutions_complexes_simples():
    # x^2 + 1 = 0 => z1 = -1j, z2 = 1j
    z1, z2 = resoudre_second_degre(1, 0, 1)

    assert z1 == -1j
    assert z2 == 1j


def test_delta_negatif_partie_reelle_et_imaginaire():
    # x^2 + 2x + 5 = 0
    # sqrt(-16) = 4j => -1 - 2j et -1 + 2j
    z1, z2 = resoudre_second_degre(1, 2, 5)

    assert z1.real == -1.0
    assert z1.imag == -2.0

    assert z2.real == -1.0
    assert z2.imag == 2.0


def test_delta_negatif_avec_imprecision_flottants():
    # x^2 + x + 1 = 0
    z1, z2 = resoudre_second_degre(1, 1, 1)

    assert z1 == pytest.approx(-0.5 - 0.8660254j, abs=1e-5)
    assert z2 == pytest.approx(-0.5 + 0.8660254j, abs=1e-5)