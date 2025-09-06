from typing import Iterator

from agno.agent import Agent, RunResponse
from agno.models.google import Gemini
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from agno.workflow import Workflow

from dotenv import load_dotenv

# Cargamos claves API
load_dotenv(override=True)

# Flujo
class CacheWorkflow(Workflow):
    # Descripción
    description: str = "Flujo de trabajo concache"

    # agentes involucrados
    agent = Agent(model=Gemini(id="gemini-2.5-flash", temperature=0))

    # Lógica del proceso
    def run(self, message: str) -> Iterator[RunResponse]:
        """Ejecuta la lógica del flujo
        """
        logger.info(f"Busca en cache '{message}'")
        # Revisamos si existe en la cache
        if self.session_state.get(message):
            logger.info(f"En cache '{message}'")
            yield RunResponse(run_id=self.run_id, content=self.session_state.get(message))
            return

        logger.info(f"No hay cache para '{message}'")
        # Lanzamos contra el agente
        yield from self.agent.run(message, stream=True)

        # Incluimos en cache
        self.session_state[message] = self.agent.run_response.content

# Ejecutar con uv run python workflow.py
if __name__ == "__main__":
    workflow = CacheWorkflow()
    # Primera ejecución (~1s)
    response: Iterator[RunResponse] = workflow.run(message="Cuéntame una broma")
    # Imprimimos respuesta
    pprint_run_response(response, markdown=True, show_time=True)
    # Segunda ejecución (inmediata)
    response: Iterator[RunResponse] = workflow.run(message="Cuéntame una broma")
    # Imprimimos respuesta
    pprint_run_response(response, markdown=True, show_time=True)
