import numpy as np
def simular_gripe(n_simulaciones):
    # Probabilidades dadas
    prob_exposicion = 0.6
    prob_enfermar_si_inoculado = 0.2
    prob_enfermar_si_no_inoculado = 0.9

    enfermos = 0

    for _ in range(n_simulaciones):
        # Simular si las personas están expuestas a la gripe
        expuesto_inoculado = np.random.rand() < prob_exposicion
        expuesto_no_inoculado = np.random.rand() < prob_exposicion

        # Simular si las personas enferman después de la exposición
        enferma_inoculado = expuesto_inoculado and (np.random.rand() < prob_enfermar_si_inoculado)
        enferma_no_inoculado = expuesto_no_inoculado and (np.random.rand() < prob_enfermar_si_no_inoculado)

        # Si al menos uno de ellos se enferma, incrementar el contador
        if enferma_inoculado or enferma_no_inoculado:
            enfermos += 1

    # Calcular la probabilidad de que al menos uno se enferme
    prob_enfermar = enfermos / n_simulaciones

    return prob_enfermar

# Ejecutar la simulación con un gran número de simulaciones para obtener una estimación precisa
n_simulaciones = 1000000
prob = simular_gripe(n_simulaciones)
print(f"La probabilidad estimada de que al menos uno se enferme es {prob}")
