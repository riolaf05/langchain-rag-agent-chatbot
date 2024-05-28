# LangChain Agent types

LangChain categorizes agents based on several dimensions:

- model type;

- support for chat history;

- multi-input tools;

- parallel function calling;

- required model parameters.

It is important to choose the option that fits to your use case:

1. OpenAI functions 

There are certain models fine-tuned where input is a bit different than usual. There are special functions that can be called and the role of this agent is to determine when it should be invoked. This agent is designed to work with this kind of OpenAI model. It supports chat history.

2. OpenAI tools 

This agent is designed to work with OpenAI tools, so its role is to interact and determine whether to use e.g. image generation tool or another built-in one. The main difference between OpenAI function is the fact that the function is trying to find the best fitting algorithm/part of an algorithm to do better reasoning, while OpenAI tool is about built-in tools like image generation, and executing code. It supports chat history.

3. XML Agent 

There are models, where reasoning/writing XML is on a very advanced level (a good example is Anthropic Claude's model). If you're operating on XML files, that might be the right one to be considered. It supports chat history.

4. JSON Chat Agent

Several LLMs available in the market are particularly handy when it comes to reading JSON. JSON is also a very common standard of some e.g. entity representation. If you're building some kind of integration that operates on JSON files and the model is supporting it, you can try to use this agent. It supports chat history.

5. Structured chat 

Intended for multi-input tools. It supports chat history.

6. ReAct agent

Made for simple models (LLM - not conversational). It supports chat history.

7. Self-ask with search

This kind of agent supports only one tool as an input. The main goal is to divide your query into smaller ones, use tools to get the answer, and then combine it into a full answer to your question. This kind of agent doesn’t support chat history.

# Setup 

In this project ReAct agent has been used. 

To launch the project:

1. clone project 

```console
git clone https://github.com/riolaf05/langchain-rag-agent-chatbot.git
```

2. populate .env

3. setup

```console
py -m .venv/rag
source .venv/rag/bin/activate
pip install -r requirements.txt
python telegram.py
```

# References

* [Introducing LangChain Agents: 2024 Tutorial with Example](https://brightinventions.pl/blog/introducing-langchain-agents-tutorial-with-example/)

* [Using LangChain ReAct Agents with Qdrant and Llama3 for Intelligent Information Retrieval](https://medium.com/@yash9439/using-langchain-react-agents-with-qdrant-and-llama3-for-intelligent-information-retrieval-b181ce7a5962)