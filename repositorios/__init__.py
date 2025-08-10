"""
Módulo de repositorios del sistema de gestión de perros.
Contiene las implementaciones para acceso y persistencia de datos.
"""

from .perro_repositorio import PerroRepositorio
from .dueno_repositorio import DuenoRepositorio
from .veterinario_repositorio import VeterinarioRepositorio

__all__ = [
    'PerroRepositorio',
    'DuenoRepositorio',
    'VeterinarioRepositorio'
]

__version__ = '1.0.0'
__author__ = 'Sistema de Gestión de Perros'