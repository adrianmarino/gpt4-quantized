from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any


def to_lang_chain_llm(model):
    class LLMConnector(LLM):

        @property
        def _llm_type(self) -> str:
            return "custom"

        def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
            return model(prompt)

        @property
        def _identifying_params(self) -> Mapping[str, Any]:
            return {}
    
    return LLMConnector()
