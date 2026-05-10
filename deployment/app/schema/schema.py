from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), '..', 'env', '.env')
load_dotenv(env_path)

logger = logging.basicConfig(
    level=int(os.getenv('LOG_LEVEL', '20')),
    format="%(asctime)s [%(levelname)s] : %(message)s"
)
logger = logging.getLogger(__name__)


class TaskCreate(BaseModel):
    titulo: str = Field(min_length=1, description="Título de la tarea")
    contenido: str = Field(min_length=1, description="Contenido de la tarea")
    deadline: datetime = Field(description="Fecha de vencimiento")

    @field_validator('deadline')
    def deadline_check(cls, value):
        if value <= datetime.now(timezone.utc):
            raise ValueError('deadline debe estar en el futuro')
        return value

class TaskUpdate(BaseModel):
    completada: bool = Field(description="Estado de completado")

class TaskDelete(BaseModel):
    borrada: bool = Field(description="Tarea borrada")

class TaskResponse(BaseModel):
    id: int
    titulo: str
    contenido: str
    deadline: datetime
    completada: bool
    fecha_creacion: datetime
