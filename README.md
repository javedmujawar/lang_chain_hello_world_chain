<!-- steps for setup -->

uv init
uv add langchain langchain-ollama langchain-openai python-dotenv black isort 

<!-- download ollma  -->
any modal that support tool calling
ollama pull qwen3:1.7b
run on local-> ollama serve