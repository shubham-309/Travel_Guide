from langchain.output_parsers.regex import RegexParser
from langchain.prompts import PromptTemplate

output_parser = RegexParser(
    regex=r"(.*?)\nScore: (.*)",
    output_keys=["answer", "score"],
)

prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

In addition to giving an answer, also return a score of how fully it answered the user's question. This should be in the following format:



Question: [question here]
Answer: [answer here in Answer format]
Score: [score between 0 and 100]

Answer format:
- The answer should be informative.
- The answer length should be around 600 words but the answer should not be overfitted.
- If the answer can be presented in points, make it as a bulleted point list.


How to determine the score:
- Higher is a better answer
- Better responds fully to the asked question, with sufficient level of detail
- If you do not know the answer based on the context, that should be a score of 0
- Don't be overconfident!
- If none of the answer got 100 score, return the answer with maximum score and maximum length of content.
- If there are tie between scores than provide the answer with maximum length of content as a final answer.

Example #1

Context:
---------
Leading a healthy lifestyle and adopting certain habits can contribute to a longer life span. Regular exercise and Balanced and Nutritious Diet makes you physically healthy. Sufficient Sleep helps in stress management. Maintaining strong social connections and cultivating a support network contributes to mental and emotional health. 
---------
Question: Give me five simple habits that helps in a longer life span?
Helpful Answer: 
Here are five simple habits to promote longevity:
1. Regular Exercise.
2. Balanced and Nutritious Diet
3. Sufficient Sleep
4. Stress Management
5. Social Connections
Score: 95

Example #2

Context:
---------
You are planning a trip to Japan and would like some information about popular tourist destinations in Tokyo.---------
Question: What are some popular tourist destinations in Tokyo?
Helpful Answer: 
There are different tourist places where you can enjoy your trip.
1. Tokyo Tower: A famous landmark with observation decks offering panoramic views of the city.
2.Meiji Shrine: A serene Shinto shrine surrounded by a beautiful forest in the heart of the city.
3.Shibuya Crossing: The world's busiest pedestrian crossing known for its vibrant energy and neon lights.
4.Shinjuku Gyoen National Garden: A spacious park with stunning gardens, perfect for cherry blossom viewing.
5.Tsukiji Fish Market: One of the largest fish markets in the world, offering a unique seafood experience.
6.Tokyo Disneyland/DisneySea: Fun-filled theme parks with exciting attractions and entertainment for all ages.
Score: 100


Begin!

Context:
---------
{context}
---------
Question: {question}
Helpful Answer:"""
PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"],
    output_parser=output_parser,
)
