from langchain import PromptTemplate

template = """Answer the question as truthfully as possible only from the context given to you.
If you do not know the answer to the question, simply respond with "I don't know. Can you ask another question".
If questions are asked where there is no relevant context available, simply respond with "I don't know. Please ask a question relevant to the documents"
Context: {context}
{chat_history}
Question: {question}
"""

question_prompt = PromptTemplate(
    input_variables=["context", "question", "chat_history"],
    template=template,
)

combine_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
This should be in the following format:

Question: [question here]
Answer: [answer here in Answer format]

Answer format:
- The answer should be informative and within the given context.
- The answer length should be around 600 words but the answer should not be overfitted.
- If the answer conatins categories or points, present the answer in bullet point list.
- Break the answer in multiple paragraphs instead of a single long paragraph.

QUESTION: {question}
=========
{summaries}
=========
ANSWER:
"""
combine_prompt = PromptTemplate(
    input_variables=["summaries", "question"],
    template=combine_template,
)
