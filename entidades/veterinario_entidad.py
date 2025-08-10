"""
Entidad que representa un veterinario en el sistema.
"""

from datetime import datetime
from typing import List, Optional
import uuid
import re


class VeterinarioEntidad:
    """
    Entidad que representa un veterinario en el sistema.
    """
    
    def __init__(self, nombre: str, apellido: str, cedula_profesional: str, 
                 telefono: str, email: str, especialidad: str):
        self._id = str(uuid.uuid4())
        self._nombre = self._validar_nombre(nombre)
        self._apellido = self._validar_apellido(apellido)
        self._cedula_profesional = self._validar_cedula(cedula_profesional)
        self._telefono = self._validar_telefono(telefono)
        self._email = self._validar_email(email)
        self._especialidad = self._validar_especialidad(especialidad)
        self._fecha_registro = datetime.now()
        self._activo = True
        self._anos_experiencia = 0
        self._consultas_realizadas: List[str] = []
        self._horario_atencion = ""
    
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
    
    def _validar_cedula(self, cedula: str) -> str:
        """Valida que la cédula profesional sea correcta."""
        if not cedula or not cedula.strip():
            raise ValueError("La cédula profesional no puede estar vacía")
        cedula_limpia = re.sub(r'[^\d]', '', cedula)
        if len(cedula_limpia) < 6:
            raise ValueError("La cédula profesional debe tener al menos 6 dígitos")
        return cedula.strip()
    
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
    
    def _validar_especialidad(self, especialidad: str) -> str:
        """Valida que la especialidad sea correcta."""
        if not especialidad or not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía")
        especialidades_validas = [
            "General", "Cirugía", "Dermatología", "Cardiología", 
            "Neurología", "Oncología", "Traumatología", "Nutrición",
            "Medicina Interna", "Anestesiología"
        ]
        especialidad_limpia = especialidad.strip().title()
        # Permitir especialidades personalizadas, no solo las de la lista
        return especialidad_limpia
    
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
        return f"Dr. {self._nombre} {self._apellido}"
    
    @property
    def cedula_profesional(self) -> str:
        return self._cedula_profesional
    
    @property
    def telefono(self) -> str:
        return self._telefono
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def especialidad(self) -> str:
        return self._especialidad
    
    @property
    def fecha_registro(self) -> datetime:
        return self._fecha_registro
    
    @property
    def activo(self) -> bool:
        return self._activo
    
    @property
    def anos_experiencia(self) -> int:
        return self._anos_experiencia
    
    @property
    def consultas_realizadas(self) -> List[str]:
        return self._consultas_realizadas.copy()
    
    @property
    def horario_atencion(self) -> str:
        return self._horario_atencion
    
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
    
    def establecer_especialidad(self, especialidad: str) -> None:
        """Establece una nueva especialidad."""
        self._especialidad = self._validar_especialidad(especialidad)
    
    def establecer_anos_experiencia(self, anos: int) -> None:
        """Establece los años de experiencia."""
        if not isinstance(anos, int) or anos < 0:
            raise ValueError("Los años de experiencia deben ser un número positivo")
        if anos > 50:
            raise ValueError("Los años de experiencia no pueden ser mayores a 50")
        self._anos_experiencia = anos
    
    def establecer_horario_atencion(self, horario: str) -> None:
        """Establece el horario de atención."""
        self._horario_atencion = horario.strip() if horario else ""
    
    def activar(self) -> None:
        """Activa al veterinario en el sistema."""
        self._activo = True
    
    def desactivar(self) -> None:
        """Desactiva al veterinario en el sistema."""
        self._activo = False
    
    # Métodos para gestión de consultas
    def agregar_consulta(self, consulta_id: str) -> bool:
        """Agrega una consulta al historial del veterinario."""
        if not consulta_id or not consulta_id.strip():
            raise ValueError("El ID de la consulta no puede estar vacío")
        
        if consulta_id not in self._consultas_realizadas:
            self._consultas_realizadas.append(consulta_id)
            return True
        return False
    
    def cantidad_consultas(self) -> int:
        """Retorna la cantidad total de consultas realizadas."""
        return len(self._consultas_realizadas)
    
    def es_especialista(self) -> bool:
        """Verifica si es especialista (no general)."""
        return self._especialidad.lower() != "general"
    
    def es_experimentado(self) -> bool:
        """Verifica si tiene experiencia significativa."""
        return self._anos_experiencia >= 5
    
    def puede_atender_casos_complejos(self) -> bool:
        """Determina si puede atender casos complejos."""
        return self.es_especialista() and self.es_experimentado()
    
    def obtener_informacion_completa(self) -> dict:
        """Retorna toda la información del veterinario."""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'nombre_completo': self.nombre_completo,
            'cedula_profesional': self._cedula_profesional,
            'telefono': self._telefono,
            'email': self._email,
            'especialidad': self._especialidad,
            'fecha_registro': self._fecha_registro.isoformat(),
            'activo': self._activo,
            'anos_experiencia': self._anos_experiencia,
            'cantidad_consultas': self.cantidad_consultas(),
            'horario_atencion': self._horario_atencion,
            'es_especialista': self.es_especialista(),
            'es_experimentado': self.es_experimentado()
        }
    
    def __str__(self) -> str:
        return f"{self.nombre_completo} - {self._especialidad}"
    
    def __repr__(self) -> str:
        return f"VeterinarioEntidad(id='{self._id}', nombre='{self.nombre_completo}')"