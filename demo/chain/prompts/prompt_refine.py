from langchain import PromptTemplate

refine_template = (
    "The original question is as follows: {question}\n"
    "We have provided an existing answer based on tourism principles. "
    "Now, we have an opportunity to refine the answer with additional context below.\n"
    "------------\n"
    "{context_str}\n"
    "------------\n"
    "Given the new context, refine the original answer to better serve the user's query."
    "If the context isn't useful, return the original answer."
)
refine_prompt = PromptTemplate(
    input_variables=["context_str", "question", "existing_answer"],
    template=refine_template,
)
