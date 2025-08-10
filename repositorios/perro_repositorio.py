"""
Repositorio para la gestión de perros en memoria.
"""

from typing import List, Optional, Dict
from interfaces.repositorio_interface import RepositorioInterface
from entidades.perro_entidad import PerroEntidad


class PerroRepositorio(RepositorioInterface[PerroEntidad]):
    """
    Repositorio para gestionar perros en memoria.
    """
    
    def __init__(self):
        self._perros: Dict[str, PerroEntidad] = {}
    
    def guardar(self, perro: PerroEntidad) -> PerroEntidad:
        """
        Guarda un perro en el repositorio.
        """
        if not isinstance(perro, PerroEntidad):
            raise ValueError("El objeto debe ser una instancia de PerroEntidad")
        
        if self.existe(perro.id):
            raise ValueError(f"Ya existe un perro con el ID: {perro.id}")
        
        self._perros[perro.id] = perro
        return perro
    
    def obtener_por_id(self, id_perro: str) -> Optional[PerroEntidad]:
        """
        Obtiene un perro por su ID.
        """
        if not id_perro or not id_perro.strip():
            return None
        
        return self._perros.get(id_perro.strip())
    
    def obtener_todos(self) -> List[PerroEntidad]:
        """
        Obtiene todos los perros del repositorio.
        """
        return list(self._perros.values())
    
    def actualizar(self, perro: PerroEntidad) -> bool:
        """
        Actualiza un perro existente.
        """
        if not isinstance(perro, PerroEntidad):
            raise ValueError("El objeto debe ser una instancia de PerroEntidad")
        
        if not self.existe(perro.id):
            return False
        
        self._perros[perro.id] = perro
        return True
    
    def eliminar(self, id_perro: str) -> bool:
        """
        Elimina un perro del repositorio.
        """
        if not id_perro or not id_perro.strip():
            return False
        
        if id_perro in self._perros:
            del self._perros[id_perro]
            return True
        
        return False
    
    def contar_total(self) -> int:
        """
        Cuenta el total de perros en el repositorio.
        """
        return len(self._perros)
    
    def existe(self, id_perro: str) -> bool:
        """
        Verifica si existe un perro con el ID dado.
        """
        if not id_perro or not id_perro.strip():
            return False
        
        return id_perro in self._perros
    
    # Métodos específicos para perros
    def obtener_por_nombre(self, nombre: str) -> List[PerroEntidad]:
        """
        Obtiene perros por nombre.
        """
        if not nombre or not nombre.strip():
            return []
        
        nombre_buscar = nombre.strip().lower()
        perros_encontrados = []
        
        for perro in self._perros.values():
            if nombre_buscar in perro.nombre.lower():
                perros_encontrados.append(perro)
        
        return perros_encontrados
    
    def obtener_por_raza(self, raza: str) -> List[PerroEntidad]:
        """
        Obtiene perros por raza.
        """
        if not raza or not raza.strip():
            return []
        
        raza_buscar = raza.strip().lower()
        perros_encontrados = []
        
        for perro in self._perros.values():
            if raza_buscar in perro.raza.lower():
                perros_encontrados.append(perro)
        
        return perros_encontrados
    
    def obtener_por_dueno(self, id_dueno: str) -> List[PerroEntidad]:
        """
        Obtiene todos los perros de un dueño específico.
        """
        if not id_dueno or not id_dueno.strip():
            return []
        
        perros_del_dueno = []
        
        for perro in self._perros.values():
            if perro.dueno_id == id_dueno:
                perros_del_dueno.append(perro)
        
        return perros_del_dueno
    
    def obtener_por_edad_rango(self, edad_min: int, edad_max: int) -> List[PerroEntidad]:
        """
        Obtiene perros dentro de un rango de edad.
        """
        if edad_min < 0 or edad_max < edad_min:
            return []
        
        perros_en_rango = []
        
        for perro in self._perros.values():
            if edad_min <= perro.edad <= edad_max:
                perros_en_rango.append(perro)
        
        return perros_en_rango
    
    def obtener_cachorros(self) -> List[PerroEntidad]:
        """
        Obtiene todos los cachorros (menos de 1 año).
        """
        return [perro for perro in self._perros.values() if perro.es_cachorro()]
    
    def obtener_adultos(self) -> List[PerroEntidad]:
        """
        Obtiene todos los perros adultos (1-7 años).
        """
        return [perro for perro in self._perros.values() if perro.es_adulto()]
    
    def obtener_seniors(self) -> List[PerroEntidad]:
        """
        Obtiene todos los perros seniors (más de 7 años).
        """
        return [perro for perro in self._perros.values() if perro.es_senior()]
    
    def obtener_vacunados(self) -> List[PerroEntidad]:
        """
        Obtiene todos los perros vacunados.
        """
        return [perro for perro in self._perros.values() if perro.vacunado]
    
    def obtener_sin_dueno(self) -> List[PerroEntidad]:
        """
        Obtiene perros que no tienen dueño asignado.
        """
        return [perro for perro in self._perros.values() if not perro.tiene_dueno()]
    
    def obtener_estadisticas(self) -> dict:
        """
        Obtiene estadísticas generales de los perros.
        """
        total = self.contar_total()
        
        if total == 0:
            return {
                'total': 0,
                'cachorros': 0,
                'adultos': 0,
                'seniors': 0,
                'vacunados': 0,
                'sin_dueno': 0
            }
        
        return {
            'total': total,
            'cachorros': len(self.obtener_cachorros()),
            'adultos': len(self.obtener_adultos()),
            'seniors': len(self.obtener_seniors()),
            'vacunados': len(self.obtener_vacunados()),
            'sin_dueno': len(self.obtener_sin_dueno())
        }