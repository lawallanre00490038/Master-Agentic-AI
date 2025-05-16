
from langchain_groq import ChatGroq
import os
import getpass
from dotenv import load_dotenv
load_dotenv()


models = [
    "meta-llama/llama-4-scout-17b-16e-instruct",
]

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("GROQ_API_KEY")


llm = ChatGroq(
    model= models[0],
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
