from pydantic import BaseModel


class LogCreate(BaseModel):
    usuario_id: int
    usuario_destino_id: int
    nombre_archivo: str
    ruta_archivo: str
    accion: int
    modulo: str
