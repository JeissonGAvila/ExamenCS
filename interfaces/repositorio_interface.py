
"""
Interface base para todos los repositorios del sistema.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')


class RepositorioInterface(ABC, Generic[T]):
    """
    Interface base que define las operaciones comunes para todos los repositorios.
    """
    
    @abstractmethod
    def guardar(self, entidad: T) -> T:
        """
        Guarda una entidad en el repositorio.
        
        Args:
            entidad: La entidad a guardar
            
        Returns:
            T: La entidad guardada
            
        Raises:
            ValueError: Si la entidad es inválida
        """
        pass
    
    @abstractmethod
    def obtener_por_id(self, id_entidad: str) -> Optional[T]:
        """
        Obtiene una entidad por su ID.
        
        Args:
            id_entidad: ID de la entidad a buscar
            
        Returns:
            Optional[T]: La entidad encontrada o None
        """
        pass
    
    @abstractmethod
    def obtener_todos(self) -> List[T]:
        """
        Obtiene todas las entidades del repositorio.
        
        Returns:
            List[T]: Lista de todas las entidades
        """
        pass
    
    @abstractmethod
    def actualizar(self, entidad: T) -> bool:
        """
        Actualiza una entidad existente.
        
        Args:
            entidad: Entidad con datos actualizados
            
        Returns:
            bool: True si se actualizó correctamente
        """
        pass
    
    @abstractmethod
    def eliminar(self, id_entidad: str) -> bool:
        """
        Elimina una entidad del repositorio.
        
        Args:
            id_entidad: ID de la entidad a eliminar
            
        Returns:
            bool: True si se eliminó correctamente
        """
        pass
    
    @abstractmethod
    def contar_total(self) -> int:
        """
        Cuenta el total de entidades en el repositorio.
        
        Returns:
            int: Número total de entidades
        """
        pass
    
    @abstractmethod
    def existe(self, id_entidad: str) -> bool:
        """
        Verifica si existe una entidad con el ID dado.
        
        Args:
            id_entidad: ID a verificar
            
        Returns:
            bool: True si existe la entidad
        """
        pass