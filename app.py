import streamlit as st
import json
import os
from dotenv import load_dotenv
from autogen import GroupChat, GroupChatManager
import autogen

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(page_title="AutoGen Chatbot", page_icon="🤖", layout="wide")
st.title("AutoGen Azure OpenAI Chatbot")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_initialized" not in st.session_state:
    st.session_state.chat_initialized = False

if "manager" not in st.session_state:
    st.session_state.manager = None

if "agents" not in st.session_state:
    st.session_state.agents = None

# Load team configuration
@st.cache_resource
def load_team_config():
    with open('team-config.json', 'r') as f:
        return json.load(f)

team_config = load_team_config()

def initialize_chat():
    # Configure OpenAI
    config_list = [
        {
            "model": team_config["config"]["model_client"]["config"]["model"],
            "api_type": "azure",
            "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
            "api_base": os.getenv("AZURE_OPENAI_ENDPOINT"),
            "api_version": os.getenv("AZURE_OPENAI_API_VERSION"),
            "deployment_name": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        }
    ]

    # Create agents from team config
    agents = []
    for participant in team_config["config"]["participants"]:
        if participant["provider"].endswith("MultimodalWebSurfer"):
            websurfer = autogen.UserProxyAgent(
                name=participant["config"]["name"],
                description=participant["config"]["description"],
                is_termination_msg=lambda x: "TERMINATE" in x.get("content", ""),
            )
            agents.append(websurfer)
        elif participant["provider"].endswith("AssistantAgent"):
            assistant = autogen.AssistantAgent(
                name=participant["config"]["name"],
                system_message=participant["config"]["system_message"],
                llm_config={"config_list": config_list},
            )
            agents.append(assistant)
        elif participant["provider"].endswith("UserProxyAgent"):
            user_proxy = autogen.UserProxyAgent(
                name=participant["config"]["name"],
                description=participant["config"]["description"],
                is_termination_msg=lambda x: "TERMINATE" in x.get("content", ""),
            )
            agents.append(user_proxy)

    # Create group chat
    groupchat = GroupChat(
        agents=agents,
        messages=[],
        max_round=team_config["config"]["termination_condition"]["config"]["conditions"][0]["config"]["max_messages"]
    )
    
    manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})
    
    return manager, agents

# Sidebar with configuration status
st.sidebar.title("Configuration Status")
if os.getenv("AZURE_OPENAI_API_KEY"):
    st.sidebar.success("Azure OpenAI API Key: Configured")
else:
    st.sidebar.error("Azure OpenAI API Key: Not Configured")
    
if os.getenv("AZURE_OPENAI_ENDPOINT"):
    st.sidebar.success("Azure OpenAI Endpoint: Configured")
else:
    st.sidebar.error("Azure OpenAI Endpoint: Not Configured")

# Chat interface
st.write("This chatbot uses AutoGen with Azure OpenAI to provide intelligent responses using multiple agents.")

# Initialize chat if not already done
if not st.session_state.chat_initialized:
    try:
        manager, agents = initialize_chat()
        st.session_state.manager = manager
        st.session_state.agents = agents
        st.session_state.chat_initialized = True
    except Exception as e:
        st.error(f"Error initializing chat: {str(e)}")

# Chat input
user_input = st.text_input("Your message:", key="user_input")

if st.button("Send"):
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        try:
            # Get response from AutoGen
            response = st.session_state.manager.initiate_chat(
                st.session_state.agents[0],
                message=user_input
            )
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": str(response)})
            
        except Exception as e:
            st.error(f"Error getting response: {str(e)}")
        
        # Clear input using the form_submit_button
        st.session_state.user_input = ""

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Assistant: {message['content']}") 