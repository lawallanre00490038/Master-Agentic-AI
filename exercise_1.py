from langchain.tools import tool, Tool
from langchain.agents import initialize_agent, AgentType
from langchain_community.utilities import SQLDatabase
from model import llm
import requests
import os
import re
from dotenv import load_dotenv
import sys


import warnings
warnings.filterwarnings("ignore")



@tool
def get_weather(city: str):
    """
    Fetches the current weather for a specified city.
    """
    url = f"https://wttr.in/{city}?format=j1" 
    response = requests.get(url)

    if response.status_code != 200:
        return f"Error fetching weather: {response.status_code}"

    data = response.json()
    
    temp = data["current_condition"][0]["temp_C"]
    condition = data["current_condition"][0]["weatherDesc"][0]["value"]


    return f"The weather in {city} is {temp}°C with {condition}."




tools = [get_weather]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)





# query = "I want to know the weather in New York City"
query = "I want to know the sum of weather in New York City and Lagos"


response = agent.invoke(query)
print(response)
print("\n\n")
