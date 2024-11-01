import ell
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Inicializar ell con versionado y logging
ell.init(store='./logdir', verbose=True, autocommit=True)

@ell.complex(model="gpt-4o-mini")
def procesar_historia(historia_actual: str, texto_bruto: str) -> str:
    """
    Eres un asistente médico que ayuda a actualizar historias clínicas.
    Combina la historia actual con el nuevo texto en bruto, asegurando coherencia y precisión.
    """
    return f"""
    Historia actual:
    {historia_actual}

    Nuevo texto en bruto:
    {texto_bruto}

    Por favor, genera una historia clínica actualizada y coherente.
    """

@ell.complex(model="gpt-4o-mini")
def procesar_detalle_atencion(historia_paciente: str, detalle_actual: str, texto_bruto: str) -> str:
    """
    Eres un asistente médico que ayuda a actualizar detalles de atenciones.
    Basándote en la historia del paciente y el nuevo texto en bruto, genera un detalle de atención actualizado.
    """
    return f"""
    Historia del paciente:
    {historia_paciente}

    Detalle actual de la atención:
    {detalle_actual}

    Nuevo texto en bruto:
    {texto_bruto}

    Por favor, genera un detalle de atención actualizado y coherente.
    """
