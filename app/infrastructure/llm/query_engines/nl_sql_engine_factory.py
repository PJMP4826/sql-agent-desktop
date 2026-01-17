import logging
from typing import List, Optional
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core import SQLDatabase
from llama_index.core.prompts import PromptTemplate
from app.application.ports.llm_port import LLMPort
from app.application.agents.sql_agent.prompts.sql_prompts import SQLPrompts

logger = logging.getLogger(__name__)


class NLSQLEngineFactory:

    @staticmethod
    def create_engine(
        sql_database: SQLDatabase,
        llm_client: LLMPort,
        tables: List[str],
        business_context: Optional[str] = None,
        synthesize_response: bool = False,
        verbose: bool = False,
    ) -> NLSQLTableQueryEngine:
        """
        Crear NLSQLTableQueryEngine configurado

        Args:
            sql_database: SQLDatabase de LlamaIndex
            llm_client: Cliente LLM
            tables: Lista de tablas a incluir
            business_context: Contexto de negocio opcional
            synthesize_response: Si sintetizar respuesta en lenguaje natural
            verbose: Si mostrar SQL generado

        Returns:
            NLSQLTableQueryEngine configurado
        """
        try:
            logger.info(f"Crando NLSQLTableQueryEngine")

            if business_context:
                prompt_template = SQLPrompts.get_text_to_sql_prompt(
                    include_business_context=True
                )

                prompt_str = SQLPrompts.format_with_context(business_context)
                prompt_template = PromptTemplate(prompt_str)
            else:
                prompt_template = SQLPrompts.get_text_to_sql_prompt(
                    include_business_context=False
                )

            engine = NLSQLTableQueryEngine(
                sql_database=sql_database,
                tables=tables,
                llm=llm_client.get_llm_model(),
                embed_model=llm_client.get_embed_model(),
                text_to_sql_prompt=prompt_template,
                synthesize_response=synthesize_response,
                verbose=verbose,
            )

            logger.info("NLSQLTableQueryEngine creado")
            return engine

        except Exception as e:
            logger.exception(f"Error creando NLSQLTableQueryEngine: {e}")
            raise
