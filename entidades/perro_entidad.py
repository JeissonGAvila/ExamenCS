"""
Entidad que representa un perro en el sistema de gestión.
"""

from datetime import datetime
from typing import Optional
import uuid


class PerroEntidad:
    """
    Entidad que representa un perro en el sistema de gestión.
    """
    
    def __init__(self, nombre: str, raza: str, edad: int, peso: float, color: str):
        self._id = str(uuid.uuid4())
        self._nombre = self._validar_nombre(nombre)
        self._raza = self._validar_raza(raza)
        self._edad = self._validar_edad(edad)
        self._peso = self._validar_peso(peso)
        self._color = self._validar_color(color)
        self._fecha_registro = datetime.now()
        self._dueno_id: Optional[str] = None
        self._vacunado = False
        self._observaciones = ""
    
    def _validar_nombre(self, nombre: str) -> str:
        """Valida que el nombre del perro sea correcto."""
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del perro no puede estar vacío")
        if len(nombre.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        return nombre.strip().title()
    
    def _validar_raza(self, raza: str) -> str:
        """Valida que la raza sea correcta."""
        if not raza or not raza.strip():
            raise ValueError("La raza no puede estar vacía")
        return raza.strip().title()
    
    def _validar_edad(self, edad: int) -> int:
        """Valida que la edad sea correcta."""
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero positivo")
        if edad > 25:
            raise ValueError("La edad no puede ser mayor a 25 años")
        return edad
    
    def _validar_peso(self, peso: float) -> float:
        """Valida que el peso sea correcto."""
        if not isinstance(peso, (int, float)) or peso <= 0:
            raise ValueError("El peso debe ser un número positivo")
        if peso > 100:
            raise ValueError("El peso no puede ser mayor a 100 kg")
        return float(peso)
    
    def _validar_color(self, color: str) -> str:
        """Valida que el color sea correcto."""
        if not color or not color.strip():
            raise ValueError("El color no puede estar vacío")
        return color.strip().title()
    
    # Propiedades (Getters)
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def raza(self) -> str:
        return self._raza
    
    @property
    def edad(self) -> int:
        return self._edad
    
    @property
    def peso(self) -> float:
        return self._peso
    
    @property
    def color(self) -> str:
        return self._color
    
    @property
    def fecha_registro(self) -> datetime:
        return self._fecha_registro
    
    @property
    def dueno_id(self) -> Optional[str]:
        return self._dueno_id
    
    @property
    def vacunado(self) -> bool:
        return self._vacunado
    
    @property
    def observaciones(self) -> str:
        return self._observaciones
    
    # Métodos para modificar datos
    def establecer_nombre(self, nombre: str) -> None:
        """Establece un nuevo nombre para el perro."""
        self._nombre = self._validar_nombre(nombre)
    
    def establecer_raza(self, raza: str) -> None:
        """Establece una nueva raza para el perro."""
        self._raza = self._validar_raza(raza)
    
    def establecer_edad(self, edad: int) -> None:
        """Establece una nueva edad para el perro."""
        self._edad = self._validar_edad(edad)
    
    def establecer_peso(self, peso: float) -> None:
        """Establece un nuevo peso para el perro."""
        self._peso = self._validar_peso(peso)
    
    def establecer_color(self, color: str) -> None:
        """Establece un nuevo color para el perro."""
        self._color = self._validar_color(color)
    
    def asignar_dueno(self, dueno_id: str) -> None:
        """Asigna un dueño al perro."""
        if dueno_id and dueno_id.strip():
            self._dueno_id = dueno_id.strip()
        else:
            raise ValueError("El ID del dueño no puede estar vacío")
    
    def remover_dueno(self) -> None:
        """Remueve el dueño del perro."""
        self._dueno_id = None
    
    def marcar_como_vacunado(self) -> None:
        """Marca el perro como vacunado."""
        self._vacunado = True
    
    def marcar_como_no_vacunado(self) -> None:
        """Marca el perro como no vacunado."""
        self._vacunado = False
    
    def agregar_observaciones(self, observaciones: str) -> None:
        """Agrega observaciones sobre el perro."""
        self._observaciones = observaciones.strip() if observaciones else ""
    
    # Métodos de utilidad
    def obtener_edad_en_meses(self) -> int:
        """Retorna la edad del perro en meses."""
        return self._edad * 12
    
    def es_cachorro(self) -> bool:
        """Determina si el perro es un cachorro."""
        return self._edad < 1
    
    def es_adulto(self) -> bool:
        """Determina si el perro es adulto."""
        return 1 <= self._edad <= 7
    
    def es_senior(self) -> bool:
        """Determina si el perro es senior."""
        return self._edad > 7
    
    def tiene_dueno(self) -> bool:
        """Verifica si el perro tiene dueño."""
        return self._dueno_id is not None
    
    def obtener_informacion_completa(self) -> dict:
        """Retorna toda la información del perro."""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'raza': self._raza,
            'edad': self._edad,
            'peso': self._peso,
            'color': self._color,
            'fecha_registro': self._fecha_registro.isoformat(),
            'dueno_id': self._dueno_id,
            'vacunado': self._vacunado,
            'observaciones': self._observaciones,
            'etapa_vida': self._obtener_etapa_vida()
        }
    
    def _obtener_etapa_vida(self) -> str:
        """Determina la etapa de vida del perro."""
        if self.es_cachorro():
            return "Cachorro"
        elif self.es_adulto():
            return "Adulto"
        else:
            return "Senior"
    
    def __str__(self) -> str:
        return f"{self._nombre} ({self._raza}) - {self._edad} años"
    
    def __repr__(self) -> str:
        return f"PerroEntidad(id='{self._id}', nombre='{self._nombre}', raza='{self._raza}')"