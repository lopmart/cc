import gc
import os
import multiprocessing
import time
from radon.complexity import cc_visit


# Función que analiza la complejidad ciclomática de un archivo
def analyze_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        complexities = cc_visit(content)
        total_complexity = sum(c.complexity for c in complexities)
        return (file_path, total_complexity)

# Directorio que contiene los archivos de código a analizar
input_dir = '/codigo/'

# Obtener una lista de archivos Python en el directorio
file_paths = [os.path.join(input_dir, file)
              for file in os.listdir(input_dir)
              if file.endswith('.py')]

# Usar multiprocessing.Pool para paralelizar
# el análisis de los archivos

# Numero de procesos a ejecutar
def main(n):
    # calcular tiempo de ejecucion
    inicio = time.time()
    with multiprocessing.Pool(processes=n) as pool:
        results = pool.map(analyze_file, file_paths)
        # Cerrar el pool a nuevas tareas
        pool.close()
        # Esperar a que todas las tareas se completen
        pool.join()
        # calcular tiempo de ejecucion
    fin = time.time()
    # Imprimir los resultados
    for file_path, complexity in results:
        print(f'Archivo: {file_path}, Complejidad Ciclomática: {complexity}')
    print(f"Tiempo total de obtención: {fin - inicio} segundos con {n} procesos")
    # elimina el objeto pool
    del pool
    # forzar la recoleccion de basura
    gc.collect()

if __name__ == "__main__":
    for i in range(3, 4):
        main(i)
