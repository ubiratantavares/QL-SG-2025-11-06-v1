# -*- coding: utf-8 -*-

import numpy as np

class QL:

    @staticmethod
    def calcular(E_ki: np.ndarray, E_k: np.ndarray) -> np.ndarray:
        # Converte entradas para arrays NumPy
        E_ki_np = np.array(E_ki, dtype=float)
        E_k_np = np.array(E_k, dtype=float)

        # Totais locais e de referencia
        E_i = E_ki_np.sum()
        E = E_k_np.sum()

        # Evita divisao por zero
        if E_i == 0 or E == 0:
            raise ValueError("Os totais de E_ki ou E_k nao " \
            "podem ser zero para o calculo do QL.")

        # Proporcoes
        s_ki = E_ki_np / E_i
        s_k = E_k_np / E

        # Calculo vetorial do QL, evitando divisao por zero em s_k
        ql_result = np.divide(s_ki, s_k, out=np.zeros_like(s_ki), where=s_k != 0)

        return ql_result
