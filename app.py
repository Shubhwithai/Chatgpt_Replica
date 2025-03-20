import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

# Page configuration
st.set_page_config(
    page_title="ChatGPT Replica 🤖",
    page_icon="🗣️",
    layout="wide"
)

# Initialize session state
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! How can I assist you today?"}
        ]
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferWindowMemory(
            k=3, 
            return_messages=True
        )

# Initialize LLM and conversation chain
@st.cache_resource
def get_conversation_chain(api_key: str):
    llm = ChatOpenAI(
        model="gpt-4o",  # Latest OpenAI model as of March 2025
        api_key=api_key,
        temperature=0.7
    )
    return ConversationChain(
        llm=llm,
        memory=st.session_state.memory
    )

# Main app
def main():
    # Initialize session state
    initialize_session_state()

    # UI Header
    st.title("ChatGPT Replica 🤖")
    st.subheader("🖤 Made using Python + Langchain + Streamlit")

    # Sidebar for API key and settings
    with st.sidebar:
        st.header("Settings")
        api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key")
        
        if api_key:
            st.success("API Key loaded")
        else:
            st.warning("Please enter your API key to continue")
            return

        # st.markdown("---")
        # st.info("This chatbot uses OpenAI's GPT-4o model with a 3-message memory window.")

    # Initialize conversation chain with API key
    conversation = get_conversation_chain(api_key)

    # Chat interface
    chat_container = st.container()
    
    # Display chat history
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message immediately
        with chat_container:
            with st.chat_message("user"):
                st.markdown(prompt)

        # Generate and display assistant response
        with chat_container:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        response = conversation.predict(input=prompt)
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

    # Clear chat button
    if st.button("Clear Chat History"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! How can I assist you today?"}
        ]
        st.session_state.memory.clear()
        st.rerun()

if __name__ == "__main__":
    main()
