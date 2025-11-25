#!/usr/bin/env python3
"""
This module contains a function that returns
another function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a multiplier and return
    a function that multiply this multiplier to a
    float
    """
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
# On indique un callable en retour avec en liste, ses types de paramètres
# entre crochets et son type de retour Callable[[type_arg_1, type_arg_2],
# type_retour] ensuite dans la définition de la 1ère on définit la seconde,
# ses args, son retour et enfin, on met le retour de la fonction 'parente'
# qui retourne la fonction enfant. Callable fait le lien
