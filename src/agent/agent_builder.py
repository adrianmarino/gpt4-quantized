from langchain.agents import load_tools
from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from llm import to_lang_chain_llm


class AgentBuilder:
    @staticmethod
    def create(
        model,
        capacities = ['wikipedia', 'google-search', 'wolfram-alpha'],
        agentType  = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose    = True
    ):
        llm = to_lang_chain_llm(model)

        return initialize_agent(
            tools   = load_tools(capacities, llm=llm), 
            llm     = llm, 
            agent   = agentType, 
            verbose = verbose,
            memory  = ConversationBufferMemory(memory_key="chat_history")
        )