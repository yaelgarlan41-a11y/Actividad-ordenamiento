def ordenar_inventario_seleccion(codigos):
  """Ordena una lista de códigos de barras de equipos tecnológicos

  utilizando el algoritmo de Ordenamiento por Selección (Selection Sort).
  """
  n = len(codigos)
  for i in range(n - 1):
    indice_minimo = i
    for j in range(i + 1, n):
      if codigos[j] < codigos[indice_minimo]:
        indice_minimo = j

    # Intercambio de valores
    if indice_minimo != i:
      codigos[i], codigos[indice_minimo] = codigos[indice_minimo], codigos[i]

  return codigos


# Ejecución local con el conjunto de datos de la actividad
inventario_dispositivos = [88, 12, 45, 3, 27]
inventario_ordenado = ordenar_inventario_seleccion(inventario_dispositivos)
print("Códigos de barras ordenados:", inventario_ordenado)
