from langchain import PromptTemplate


template = """Answer the question in around 600 words as truthfully as possible from the context given to you. The answer should in the form of Bulleted list so explain it in a better way.
    If you do not know the answer to the question, simply respond with "I don't know. Can you ask another question".
    If questions are asked where there is no relevant context available, simply respond with "I don't know. Please ask a question relevant to the documents"
    Context: {context_str}
    {chat_history}
    Human: {question}
    Assistant:"""

question_prompt = PromptTemplate(
    input_variables=["context_str", "question", "chat_history"],
    template=template,
)

refine_template = (
    "The original question is as follows: {question}\n"
    "We have provided an existing answer, including sources: {existing_answer}\n"
    "We have the opportunity to refine the existing answer"
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{context_str}\n"
    "------------\n"
    "Given the new context, refine the original answer to better "
    "answer the question."
    "If you do update it, please update the sources as well. "
    "If the context isn't useful, return the original answer."
)
refine_prompt = PromptTemplate(
    input_variables=["context_str", "question", "existing_answer"],
    template=refine_template,
)
