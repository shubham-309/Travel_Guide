import enum


class MemoryType(enum.Enum):
    no_memory = 0
    chat_history = 1


class ChainType(enum.Enum):
    Stuff = 0
    Refine = 1
    Map_Reduce = 2
    Map_Rerank = 3
