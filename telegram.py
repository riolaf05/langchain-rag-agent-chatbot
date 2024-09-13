import os
import telepot
from telepot.loop import MessageLoop
import datetime
import time
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain.prompts import SystemMessagePromptTemplate
from langchain.agents import create_tool_calling_agent
import re
from dotenv import load_dotenv
load_dotenv(override=True)

#Tools
from tools.retrieval_eventi import get_relevant_document_tool 
from tools.tavily import web_search_tool 
from tools.utils import get_today_date_tool, get_summarized_text_tool
from tools.aws import ec2_shutdown_tools, ec2_turnon_tools
from prompts.react import prompt_react
from tools.google import get_calendar_events


TELEGRAM_CHAT_ID=os.getenv('TELEGRAM_CHAT_ID')
TELEGRAM_GROUP_ID=os.getenv('TELEGRAM_GROUP_ID')
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

tools = [get_relevant_document_tool, get_today_date_tool, web_search_tool, ec2_shutdown_tools, ec2_turnon_tools, get_calendar_events]

# Initialize ChatGroq model for language understanding
prompt = hub.pull("hwchase17/openai-functions-agent")
model = ChatGroq(model_name="llama3-70b-8192", groq_api_key=GROQ_API_KEY, temperature=0)
system_template = 'Sei un aiutante servizievole.'
system_message_prompt_template = SystemMessagePromptTemplate.from_template(
    system_template)
prompt.messages[0]=system_message_prompt_template

# Create ReAct agent
agent = create_tool_calling_agent(model, tools, prompt)
react_agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True
)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        try:
            response = react_agent_executor.invoke({"input": msg['text'].split(" ")})
            bot.sendMessage(TELEGRAM_GROUP_ID, response['output'])
        
        except Exception as e:
            bot.sendMessage(TELEGRAM_GROUP_ID, "Ho avuto un problema!")
            bot.sendMessage(TELEGRAM_GROUP_ID, e)

    # elif content_type == 'photo':
        # bot.sendPhoto(TELEGRAM_GROUP_ID, )
    else:
        response = bot.sendMessage(TELEGRAM_GROUP_ID, "Non ho capito!")

bot = telepot.Bot(TELEGRAM_CHAT_ID)
bot.setWebhook()
bot.message_loop(on_chat_message)
print('In attesa di nuovi messaggi...')

while 1:
    time.sleep(10)