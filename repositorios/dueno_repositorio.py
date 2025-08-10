"""
Repositorio para la gestión de dueños en memoria.
"""

from typing import List, Optional, Dict
from interfaces.repositorio_interface import RepositorioInterface
from entidades.dueno_entidad import DuenoEntidad


class DuenoRepositorio(RepositorioInterface[DuenoEntidad]):
    """
    Repositorio para gestionar dueños en memoria.
    """
    
    def __init__(self):
        self._duenos: Dict[str, DuenoEntidad] = {}
    
    def guardar(self, dueno: DuenoEntidad) -> DuenoEntidad:
        """
        Guarda un dueño en el repositorio.
        """
        if not isinstance(dueno, DuenoEntidad):
            raise ValueError("El objeto debe ser una instancia de DuenoEntidad")
        
        if self.existe(dueno.id):
            raise ValueError(f"Ya existe un dueño con el ID: {dueno.id}")
        
        # Verificar que el email no esté duplicado
        if self.obtener_por_email(dueno.email) is not None:
            raise ValueError(f"Ya existe un dueño con el email: {dueno.email}")
        
        self._duenos[dueno.id] = dueno
        return dueno
    
    def obtener_por_id(self, id_dueno: str) -> Optional[DuenoEntidad]:
        """
        Obtiene un dueño por su ID.
        """
        if not id_dueno or not id_dueno.strip():
            return None
        
        return self._duenos.get(id_dueno.strip())
    
    def obtener_todos(self) -> List[DuenoEntidad]:
        """
        Obtiene todos los dueños del repositorio.
        """
        return list(self._duenos.values())
    
    def actualizar(self, dueno: DuenoEntidad) -> bool:
        """
        Actualiza un dueño existente.
        """
        if not isinstance(dueno, DuenoEntidad):
            raise ValueError("El objeto debe ser una instancia de DuenoEntidad")
        
        if not self.existe(dueno.id):
            return False
        
        # Verificar que el email no esté duplicado en otro dueño
        dueno_existente = self.obtener_por_email(dueno.email)
        if dueno_existente and dueno_existente.id != dueno.id:
            raise ValueError(f"Ya existe otro dueño con el email: {dueno.email}")
        
        self._duenos[dueno.id] = dueno
        return True
    
    def eliminar(self, id_dueno: str) -> bool:
        """
        Elimina un dueño del repositorio.
        """
        if not id_dueno or not id_dueno.strip():
            return False
        
        if id_dueno in self._duenos:
            del self._duenos[id_dueno]
            return True
        
        return False
    
    def contar_total(self) -> int:
        """
        Cuenta el total de dueños en el repositorio.
        """
        return len(self._duenos)
    
    def existe(self, id_dueno: str) -> bool:
        """
        Verifica si existe un dueño con el ID dado.
        """
        if not id_dueno or not id_dueno.strip():
            return False
        
        return id_dueno in self._duenos
    
    # Métodos específicos para dueños
    def obtener_por_email(self, email: str) -> Optional[DuenoEntidad]:
        """
        Obtiene un dueño por su email.
        """
        if not email or not email.strip():
            return None
        
        email_buscar = email.strip().lower()
        
        for dueno in self._duenos.values():
            if dueno.email.lower() == email_buscar:
                return dueno
        
        return None
    
    def obtener_por_telefono(self, telefono: str) -> Optional[DuenoEntidad]:
        """
        Obtiene un dueño por su teléfono.
        """
        if not telefono or not telefono.strip():
            return None
        
        telefono_buscar = telefono.strip()
        
        for dueno in self._duenos.values():
            if dueno.telefono == telefono_buscar:
                return dueno
        
        return None
    
    def buscar_por_nombre(self, nombre: str) -> List[DuenoEntidad]:
        """
        Busca dueños por nombre o apellido.
        """
        if not nombre or not nombre.strip():
            return []
        
        nombre_buscar = nombre.strip().lower()
        duenos_encontrados = []
        
        for dueno in self._duenos.values():
            nombre_completo = dueno.nombre_completo.lower()
            if nombre_buscar in nombre_completo:
                duenos_encontrados.append(dueno)
        
        return duenos_encontrados
    
    def obtener_activos(self) -> List[DuenoEntidad]:
        """
        Obtiene todos los dueños activos.
        """
        return [dueno for dueno in self._duenos.values() if dueno.activo]
    
    def obtener_inactivos(self) -> List[DuenoEntidad]:
        """
        Obtiene todos los dueños inactivos.
        """
        return [dueno for dueno in self._duenos.values() if not dueno.activo]
    
    def obtener_con_perros(self) -> List[DuenoEntidad]:
        """
        Obtiene dueños que tienen al menos un perro.
        """
        return [dueno for dueno in self._duenos.values() if dueno.cantidad_perros() > 0]
    
    def obtener_sin_perros(self) -> List[DuenoEntidad]:
        """
        Obtiene dueños que no tienen perros.
        """
        return [dueno for dueno in self._duenos.values() if dueno.cantidad_perros() == 0]
    
    def obtener_por_cantidad_perros(self, cantidad_min: int, cantidad_max: int = None) -> List[DuenoEntidad]:
        """
        Obtiene dueños dentro de un rango de cantidad de perros.
        """
        if cantidad_min < 0:
            return []
        
        duenos_en_rango = []
        
        for dueno in self._duenos.values():
            cantidad = dueno.cantidad_perros()
            if cantidad_max is None:
                if cantidad >= cantidad_min:
                    duenos_en_rango.append(dueno)
            else:
                if cantidad_min <= cantidad <= cantidad_max:
                    duenos_en_rango.append(dueno)
        
        return duenos_en_rango
    
    def buscar_por_direccion(self, direccion: str) -> List[DuenoEntidad]:
        """
        Busca dueños por dirección (búsqueda parcial).
        """
        if not direccion or not direccion.strip():
            return []
        
        direccion_buscar = direccion.strip().lower()
        duenos_encontrados = []
        
        for dueno in self._duenos.values():
            if direccion_buscar in dueno.direccion.lower():
                duenos_encontrados.append(dueno)
        
        return duenos_encontrados
    
    def obtener_estadisticas(self) -> dict:
        """
        Obtiene estadísticas generales de los dueños.
        """
        total = self.contar_total()
        
        if total == 0:
            return {
                'total': 0,
                'activos': 0,
                'inactivos': 0,
                'con_perros': 0,
                'sin_perros': 0,
                'promedio_perros_por_dueno': 0
            }
        
        activos = len(self.obtener_activos())
        con_perros = len(self.obtener_con_perros())
        total_perros = sum(dueno.cantidad_perros() for dueno in self._duenos.values())
        
        return {
            'total': total,
            'activos': activos,
            'inactivos': total - activos,
            'con_perros': con_perros,
            'sin_perros': total - con_perros,
            'promedio_perros_por_dueno': round(total_perros / total, 2) if total > 0 else 0
        }