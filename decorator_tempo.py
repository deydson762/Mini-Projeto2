import time
from functools import wraps
import logging
from datetime import datetime

# Configurar logging para gravar em arquivo
logging.basicConfig(
    filename='execution.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def decorator_tempo(func):
    """Decorator que mede o tempo de execução de uma função e grava em log."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        duracao = fim - inicio
        
        # Gravar no log
        logging.info(f"Função '{func.__name__}' executada em {duracao:.6f} segundos.")
        
        return resultado
    return wrapper
