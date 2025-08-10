"""
Módulo de entidades del sistema de gestión de perros.
Contiene las clases que representan los objetos de dominio.
"""

from .perro_entidad import PerroEntidad
from .dueno_entidad import DuenoEntidad
from .veterinario_entidad import VeterinarioEntidad

__all__ = [
    'PerroEntidad',
    'DuenoEntidad', 
    'VeterinarioEntidad'
]

__version__ = '1.0.0'
__author__ = 'Sistema de Gestión de Perros'