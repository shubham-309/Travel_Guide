from chain.utils import *
from chain.datastores.datastore import *
import os, enum
from chain.chain_with_chat_history import ChainWithChatHistory
from chain.constants import MemoryType, ChainType


class Session:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.set_complete = False
        if hasattr(self, "initialized"):
            return
        self.initialized = True
        print("Initializing Session")
        self.init_default_state()
        self.init_datasource()
        self.init_retreivers()
        self.set_complete = True

    def init_datasource(self):
        self.datastore_name = "Pinecone"
        init_datastore(self.datastore_name)

    def update_sources(self, show_sources):
        self.show_sources = show_sources
        self.init_retreivers()
        print(f"The new value is {self.show_sources}")

    def update_memory(self, memory):
        print(f"updating memory: {memory}")
        self.memory_type = MemoryType[memory]
        self.init_retreivers()

    def update_chain(self, chain):
        print(f"updating chain: {chain}")
        self.chain_type = ChainType[chain]
        if self.chain_type is ChainType.Map_Rerank:
            self.memory_type = MemoryType.no_memory
        self.init_retreivers()

    def update_temperature(self, temperature):
        self.temperature = temperature
        self.init_retreivers()

    def init_retreivers(self):
        self.coustom_chain = ChainWithChatHistory(
            self.datastore_name,
            self.show_sources,
            self.temperature,
            self.chain_type,
        )

    def init_default_state(self):
        self.show_sources = True
        self.memory_type = MemoryType.no_memory
        self.temperature = 0.1
        self.chain_type = ChainType.Stuff

    def get_answer(self, question):
        return self.coustom_chain.get_answer(question, self.memory_type)

    def get_details(self):
        return f"\n Attach sources: {self.show_sources} \nChain: {self.chain_type.name} \n Memory: {self.memory_type.name} \nTemperature: {self.temperature}"
