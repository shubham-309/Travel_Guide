import os
from langchain.chains import ConversationalRetrievalChain, RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI

from chain.prompts import (
    prompt_stuff,
    prompt_refine,
    prompt_map_reduce,
    prompt_map_rerank,
)
from chain.utils import *
from chain.datastores.datastore import *
from chain.constants import MemoryType, ChainType
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks import get_openai_callback
from chain.callbacks.openai_callback import *


class ChainWithChatHistory:
    chat_history = []

    def __init__(self, datastore_name, show_sources, temperature, chain_type):
        self.create_retrievar(
            datastore_name=datastore_name,
            show_sources=show_sources,
            temperature=temperature,
            chain_type=chain_type,
        )

    def create_retrievar(self, datastore_name, show_sources, temperature, chain_type):
        retriever = get_retriever(datastore_name)

        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=temperature,
            verbose=True,
            callbacks=[CustomOpenAICallback()],
        )
        self.chain = self.create_chain(llm, retriever, show_sources, chain_type)

    def create_chain(self, llm, retriever, show_sources, chain_type):
        self.chain_type = chain_type
        match chain_type:
            case ChainType.Stuff:
                return ConversationalRetrievalChain.from_llm(
                    llm=llm,
                    chain_type="stuff",
                    retriever=retriever.as_retriever(),
                    return_source_documents=show_sources,
                    verbose=True,
                    combine_docs_chain_kwargs={"prompt": prompt_stuff.PROMPT},
                )
            case ChainType.Refine:
                return ConversationalRetrievalChain.from_llm(
                    llm=llm,
                    chain_type="refine",
                    retriever=retriever.as_retriever(),
                    return_source_documents=show_sources,
                    combine_docs_chain_kwargs={
                        "refine_prompt": prompt_refine.refine_prompt,
                        "question_prompt": prompt_refine.question_prompt,
                    },
                )
            case ChainType.Map_Reduce:
                return ConversationalRetrievalChain.from_llm(
                    llm=llm,
                    chain_type="map_reduce",
                    retriever=retriever.as_retriever(),
                    return_source_documents=False,
                    combine_docs_chain_kwargs={
                        "combine_prompt": prompt_map_reduce.combine_prompt,
                        "question_prompt": prompt_map_reduce.question_prompt,
                    },
                )

            case ChainType.Map_Rerank:
                return RetrievalQAWithSourcesChain.from_chain_type(
                    llm=llm,
                    chain_type="map_rerank",
                    retriever=retriever.as_retriever(),
                    return_source_documents=False,
                    verbose=True,
                )

    def get_answer(self, question, memory_type):
        with get_openai_callback() as cb:
            if memory_type == MemoryType.no_memory:
                self.chat_history = []
            if self.chain_type is ChainType.Map_Rerank:
                result = self.chain(question)
            else:
                result = self.chain(
                    {"question": question, "chat_history": self.chat_history}
                )
            self.add_in_memory(memory_type, question, result["answer"])
        return result, cb

    def add_in_memory(self, memory_type, question, answer):
        match memory_type:
            case MemoryType.chat_history:
                self.chat_history.append((question, answer))
            case MemoryType.no_memory:
                self.chat_history = []
