# TravelMentor: Your Personalized Journey Planner

## Instruction to set up the code:

## Clone the Repo using

git clone git remote add origin https://github.com/shubham-309/Travel_Guide.git

## Instruction to create the environment:
1. Create a .env file with following key-values:
  
  INDEX_NAME

  GOOGLE_API_KEY

  PINECONE_API_KEY

  PINECONE_ENV_REGION

For GOOGLE_API_KEY You can make one here :- https://makersuite.google.com/app/prompts/new_freeform

Pinecone :- https://www.pinecone.io/

## Push Documents to Pinecone

1. Store your Documents in the Documents folder.
2. Run the ingestion.py file to Create embedding and Push embeddings to Pinecone

You have successfully pushed your Documents to Pinecone



3. run to create a virtual environment and install dependencies:

-> pipenv install


## Instruction to launch the app: 

streamlit run demo/chat_interface.py
