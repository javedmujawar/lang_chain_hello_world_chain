from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch
load_dotenv()


tavily = TavilyClient()


@tool
def search(query: str) -> str:
    """
    tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Search for {query}")
    #return "Tokyo weather is sunny"
    return tavily.search(query=query)


llm = ChatOpenAI(temperature=0, model="gemma3:1b")
#tools = [search]
tools =[TavilySearch]
agent = create_agent(model=llm, tools=tools)


def main():
    result = agent.invoke(
        {"messages": HumanMessage(content="What is the weather in Tokyo")}
    )
    print(result)


if __name__ == "__main__":
    main()
