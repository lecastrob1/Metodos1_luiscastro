import numpy as np


probabilidades = np.array([
    [0.4, 0.25, 0.3, 0.1],
    [0.2, 0.25, 0.3, 0.1],
    [0.2, 0.25, 0.1, 0.1],
    [0.2, 0.25, 0.3, 0.7]
])

mapeo_bases = {'A': 0, 'C': 1, 'G': 2, 'T': 3, 'U':3}

probabilidades_a_priori = np.array([0.25, 0, 0.5, 0.25])


secuencia = 'TGCTCAAA'


probabilidad_secuencia = probabilidades_a_priori[mapeo_bases[secuencia[0]]]

for i in range(1, len(secuencia)):
    indice_base_actual = mapeo_bases[secuencia[i-1]]
    indice_base_siguiente = mapeo_bases[secuencia[i]]

    probabilidad_secuencia *= probabilidades[indice_base_siguiente][indice_base_actual]
print(f'La probabilidad de la secuencia {secuencia} es {probabilidad_secuencia}')

probabilidadesE = np.array([
    [0.01, 0., 0., 0.7],
    [0.05, 0.01, 0.9, 0.],
    [0.05, 0.09, 0.1, 0.1],
    [0.8, 0., 0., 0.2]
])

secuenciagr = 'ACGAGUUU'
for i in range(0, len(secuenciagr)):
    indice_base_actual = mapeo_bases[secuencia[i]]
    indice_base_siguiente = mapeo_bases[secuenciagr[i]]
    print(indice_base_actual,indice_base_siguiente)
    print(probabilidadesE[indice_base_siguiente][indice_base_actual])

    probabilidad_secuencia *= probabilidadesE[indice_base_siguiente][indice_base_actual]
print(f'La probabilidad de la secuencia {secuenciagr} es {probabilidad_secuencia}')
