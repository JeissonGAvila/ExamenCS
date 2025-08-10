"""
Repositorio para la gestión de veterinarios en memoria.
"""

from typing import List, Optional, Dict
from interfaces.repositorio_interface import RepositorioInterface
from entidades.veterinario_entidad import VeterinarioEntidad


class VeterinarioRepositorio(RepositorioInterface[VeterinarioEntidad]):
    """
    Repositorio para gestionar veterinarios en memoria.
    """
    
    def __init__(self):
        self._veterinarios: Dict[str, VeterinarioEntidad] = {}
    
    def guardar(self, veterinario: VeterinarioEntidad) -> VeterinarioEntidad:
        """
        Guarda un veterinario en el repositorio.
        """
        if not isinstance(veterinario, VeterinarioEntidad):
            raise ValueError("El objeto debe ser una instancia de VeterinarioEntidad")
        
        if self.existe(veterinario.id):
            raise ValueError(f"Ya existe un veterinario con el ID: {veterinario.id}")
        
        # Verificar que la cédula profesional no esté duplicada
        if self.obtener_por_cedula(veterinario.cedula_profesional) is not None:
            raise ValueError(f"Ya existe un veterinario con la cédula: {veterinario.cedula_profesional}")
        
        # Verificar que el email no esté duplicado
        if self.obtener_por_email(veterinario.email) is not None:
            raise ValueError(f"Ya existe un veterinario con el email: {veterinario.email}")
        
        self._veterinarios[veterinario.id] = veterinario
        return veterinario
    
    def obtener_por_id(self, id_veterinario: str) -> Optional[VeterinarioEntidad]:
        """
        Obtiene un veterinario por su ID.
        """
        if not id_veterinario or not id_veterinario.strip():
            return None
        
        return self._veterinarios.get(id_veterinario.strip())
    
    def obtener_todos(self) -> List[VeterinarioEntidad]:
        """
        Obtiene todos los veterinarios del repositorio.
        """
        return list(self._veterinarios.values())
    
    def actualizar(self, veterinario: VeterinarioEntidad) -> bool:
        """
        Actualiza un veterinario existente.
        """
        if not isinstance(veterinario, VeterinarioEntidad):
            raise ValueError("El objeto debe ser una instancia de VeterinarioEntidad")
        
        if not self.existe(veterinario.id):
            return False
        
        # Verificar que la cédula no esté duplicada en otro veterinario
        vet_existente_cedula = self.obtener_por_cedula(veterinario.cedula_profesional)
        if vet_existente_cedula and vet_existente_cedula.id != veterinario.id:
            raise ValueError(f"Ya existe otro veterinario con la cédula: {veterinario.cedula_profesional}")
        
        # Verificar que el email no esté duplicado en otro veterinario
        vet_existente_email = self.obtener_por_email(veterinario.email)
        if vet_existente_email and vet_existente_email.id != veterinario.id:
            raise ValueError(f"Ya existe otro veterinario con el email: {veterinario.email}")
        
        self._veterinarios[veterinario.id] = veterinario
        return True
    
    def eliminar(self, id_veterinario: str) -> bool:
        """
        Elimina un veterinario del repositorio.
        """
        if not id_veterinario or not id_veterinario.strip():
            return False
        
        if id_veterinario in self._veterinarios:
            del self._veterinarios[id_veterinario]
            return True
        
        return False
    
    def contar_total(self) -> int:
        """
        Cuenta el total de veterinarios en el repositorio.
        """
        return len(self._veterinarios)
    
    def existe(self, id_veterinario: str) -> bool:
        """
        Verifica si existe un veterinario con el ID dado.
        """
        if not id_veterinario or not id_veterinario.strip():
            return False
        
        return id_veterinario in self._veterinarios
    
    # Métodos específicos para veterinarios
    def obtener_por_cedula(self, cedula: str) -> Optional[VeterinarioEntidad]:
        """
        Obtiene un veterinario por su cédula profesional.
        """
        if not cedula or not cedula.strip():
            return None
        
        cedula_buscar = cedula.strip()
        
        for veterinario in self._veterinarios.values():
            if veterinario.cedula_profesional == cedula_buscar:
                return veterinario
        
        return None
    
    def obtener_por_email(self, email: str) -> Optional[VeterinarioEntidad]:
        """
        Obtiene un veterinario por su email.
        """
        if not email or not email.strip():
            return None
        
        email_buscar = email.strip().lower()
        
        for veterinario in self._veterinarios.values():
            if veterinario.email.lower() == email_buscar:
                return veterinario
        
        return None
    
    def buscar_por_nombre(self, nombre: str) -> List[VeterinarioEntidad]:
        """
        Busca veterinarios por nombre o apellido.
        """
        if not nombre or not nombre.strip():
            return []
        
        nombre_buscar = nombre.strip().lower()
        veterinarios_encontrados = []
        
        for veterinario in self._veterinarios.values():
            nombre_completo = veterinario.nombre_completo.lower()
            if nombre_buscar in nombre_completo:
                veterinarios_encontrados.append(veterinario)
        
        return veterinarios_encontrados
    
    def obtener_por_especialidad(self, especialidad: str) -> List[VeterinarioEntidad]:
        """
        Obtiene veterinarios por especialidad.
        """
        if not especialidad or not especialidad.strip():
            return []
        
        especialidad_buscar = especialidad.strip().lower()
        veterinarios_encontrados = []
        
        for veterinario in self._veterinarios.values():
            if especialidad_buscar in veterinario.especialidad.lower():
                veterinarios_encontrados.append(veterinario)
        
        return veterinarios_encontrados
    
    def obtener_activos(self) -> List[VeterinarioEntidad]:
        """
        Obtiene todos los veterinarios activos.
        """
        return [vet for vet in self._veterinarios.values() if vet.activo]
    
    def obtener_inactivos(self) -> List[VeterinarioEntidad]:
        """
        Obtiene todos los veterinarios inactivos.
        """
        return [vet for vet in self._veterinarios.values() if not vet.activo]
    
    def obtener_especialistas(self) -> List[VeterinarioEntidad]:
        """
        Obtiene veterinarios especialistas (no generales).
        """
        return [vet for vet in self._veterinarios.values() if vet.es_especialista()]
    
    def obtener_generales(self) -> List[VeterinarioEntidad]:
        """
        Obtiene veterinarios de medicina general.
        """
        return [vet for vet in self._veterinarios.values() if not vet.es_especialista()]
    
    def obtener_experimentados(self) -> List[VeterinarioEntidad]:
        """
        Obtiene veterinarios con experiencia significativa (5+ años).
        """
        return [vet for vet in self._veterinarios.values() if vet.es_experimentado()]
    
    def obtener_por_experiencia_minima(self, anos_minimos: int) -> List[VeterinarioEntidad]:
        """
        Obtiene veterinarios con un mínimo de años de experiencia.
        """
        if anos_minimos < 0:
            return []
        
        return [vet for vet in self._veterinarios.values() if vet.anos_experiencia >= anos_minimos]
    
    def obtener_con_mas_consultas(self, cantidad_minima: int) -> List[VeterinarioEntidad]:
        """
        Obtiene veterinarios que han realizado una cantidad mínima de consultas.
        """
        if cantidad_minima < 0:
            return []
        
        return [vet for vet in self._veterinarios.values() if vet.cantidad_consultas() >= cantidad_minima]
    
    def obtener_disponibles_casos_complejos(self) -> List[VeterinarioEntidad]:
        """
        Obtiene veterinarios que pueden atender casos complejos.
        """
        return [vet for vet in self._veterinarios.values() if vet.puede_atender_casos_complejos()]
    
    def buscar_por_telefono(self, telefono: str) -> Optional[VeterinarioEntidad]:
        """
        Busca un veterinario por su teléfono.
        """
        if not telefono or not telefono.strip():
            return None
        
        telefono_buscar = telefono.strip()
        
        for veterinario in self._veterinarios.values():
            if veterinario.telefono == telefono_buscar:
                return veterinario
        
        return None
    
    def obtener_estadisticas(self) -> dict:
        """
        Obtiene estadísticas generales de los veterinarios.
        """
        total = self.contar_total()
        
        if total == 0:
            return {
                'total': 0,
                'activos': 0,
                'inactivos': 0,
                'especialistas': 0,
                'generales': 0,
                'experimentados': 0,
                'promedio_experiencia': 0,
                'total_consultas': 0
            }
        
        activos = len(self.obtener_activos())
        especialistas = len(self.obtener_especialistas())
        experimentados = len(self.obtener_experimentados())
        
        total_experiencia = sum(vet.anos_experiencia for vet in self._veterinarios.values())
        total_consultas = sum(vet.cantidad_consultas() for vet in self._veterinarios.values())
        
        return {
            'total': total,
            'activos': activos,
            'inactivos': total - activos,
            'especialistas': especialistas,
            'generales': total - especialistas,
            'experimentados': experimentados,
            'promedio_experiencia': round(total_experiencia / total, 2) if total > 0 else 0,
            'total_consultas': total_consultas
        }