"""
Entidad que representa al dueño de perros en el sistema.
"""

from datetime import datetime
from typing import List, Optional
import uuid
import re


class DuenoEntidad:
    """
    Entidad que representa al dueño de perros en el sistema.
    """
    
    def __init__(self, nombre: str, apellido: str, telefono: str, email: str, direccion: str):
        self._id = str(uuid.uuid4())
        self._nombre = self._validar_nombre(nombre)
        self._apellido = self._validar_apellido(apellido)
        self._telefono = self._validar_telefono(telefono)
        self._email = self._validar_email(email)
        self._direccion = self._validar_direccion(direccion)
        self._fecha_registro = datetime.now()
        self._perros_ids: List[str] = []
        self._activo = True
    
    def _validar_nombre(self, nombre: str) -> str:
        """Valida que el nombre sea correcto."""
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if len(nombre.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        return nombre.strip().title()
    
    def _validar_apellido(self, apellido: str) -> str:
        """Valida que el apellido sea correcto."""
        if not apellido or not apellido.strip():
            raise ValueError("El apellido no puede estar vacío")
        if len(apellido.strip()) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres")
        return apellido.strip().title()
    
    def _validar_telefono(self, telefono: str) -> str:
        """Valida que el teléfono sea correcto."""
        if not telefono or not telefono.strip():
            raise ValueError("El teléfono no puede estar vacío")
        telefono_limpio = re.sub(r'[^\d]', '', telefono)
        if len(telefono_limpio) < 8:
            raise ValueError("El teléfono debe tener al menos 8 dígitos")
        return telefono.strip()
    
    def _validar_email(self, email: str) -> str:
        """Valida que el email sea correcto."""
        if not email or not email.strip():
            raise ValueError("El email no puede estar vacío")
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron_email, email.strip()):
            raise ValueError("El formato del email no es válido")
        return email.strip().lower()
    
    def _validar_direccion(self, direccion: str) -> str:
        """Valida que la dirección sea correcta."""
        if not direccion or not direccion.strip():
            raise ValueError("La dirección no puede estar vacía")
        if len(direccion.strip()) < 10:
            raise ValueError("La dirección debe ser más específica")
        return direccion.strip()
    
    # Propiedades (Getters)
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def apellido(self) -> str:
        return self._apellido
    
    @property
    def nombre_completo(self) -> str:
        return f"{self._nombre} {self._apellido}"
    
    @property
    def telefono(self) -> str:
        return self._telefono
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def direccion(self) -> str:
        return self._direccion
    
    @property
    def fecha_registro(self) -> datetime:
        return self._fecha_registro
    
    @property
    def perros_ids(self) -> List[str]:
        return self._perros_ids.copy()
    
    @property
    def activo(self) -> bool:
        return self._activo
    
    # Métodos para modificar datos
    def establecer_nombre(self, nombre: str) -> None:
        """Establece un nuevo nombre."""
        self._nombre = self._validar_nombre(nombre)
    
    def establecer_apellido(self, apellido: str) -> None:
        """Establece un nuevo apellido."""
        self._apellido = self._validar_apellido(apellido)
    
    def establecer_telefono(self, telefono: str) -> None:
        """Establece un nuevo teléfono."""
        self._telefono = self._validar_telefono(telefono)
    
    def establecer_email(self, email: str) -> None:
        """Establece un nuevo email."""
        self._email = self._validar_email(email)
    
    def establecer_direccion(self, direccion: str) -> None:
        """Establece una nueva dirección."""
        self._direccion = self._validar_direccion(direccion)
    
    def activar(self) -> None:
        """Activa al dueño en el sistema."""
        self._activo = True
    
    def desactivar(self) -> None:
        """Desactiva al dueño en el sistema."""
        self._activo = False
    
    # Métodos para gestión de perros
    def agregar_perro(self, perro_id: str) -> bool:
        """Agrega un perro a la lista del dueño."""
        if not perro_id or not perro_id.strip():
            raise ValueError("El ID del perro no puede estar vacío")
        
        if perro_id not in self._perros_ids:
            self._perros_ids.append(perro_id)
            return True
        return False
    
    def remover_perro(self, perro_id: str) -> bool:
        """Remueve un perro de la lista del dueño."""
        if perro_id in self._perros_ids:
            self._perros_ids.remove(perro_id)
            return True
        return False
    
    def tiene_perro(self, perro_id: str) -> bool:
        """Verifica si el dueño tiene un perro específico."""
        return perro_id in self._perros_ids
    
    def cantidad_perros(self) -> int:
        """Retorna la cantidad de perros que tiene el dueño."""
        return len(self._perros_ids)
    
    def puede_adoptar_mas_perros(self, limite: int = 5) -> bool:
        """Verifica si el dueño puede adoptar más perros."""
        return self.cantidad_perros() < limite
    
    def obtener_informacion_completa(self) -> dict:
        """Retorna toda la información del dueño."""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'nombre_completo': self.nombre_completo,
            'telefono': self._telefono,
            'email': self._email,
            'direccion': self._direccion,
            'fecha_registro': self._fecha_registro.isoformat(),
            'perros_ids': self._perros_ids.copy(),
            'cantidad_perros': self.cantidad_perros(),
            'activo': self._activo
        }
    
    def __str__(self) -> str:
        return f"{self.nombre_completo} - {self.cantidad_perros()} perro(s)"
    
    def __repr__(self) -> str:
        return f"DuenoEntidad(id='{self._id}', nombre='{self.nombre_completo}')"