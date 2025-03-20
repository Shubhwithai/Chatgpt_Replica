# ChatGPT Replica 🤖

A simple chatbot built using **Python**, **Langchain**, and **Streamlit**, leveraging OpenAI's **GPT-4o** model for interactive conversations.

## Features
- Interactive chat interface using **Streamlit**
- Conversational memory using **Langchain**
- Supports **GPT-4o** model via OpenAI API
- Sidebar for entering OpenAI API Key
- Chat history persistence
- Option to clear chat history

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/chatgpt-replica.git
   cd chatgpt-replica
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```sh
   streamlit run app.py
   ```

2. Enter your **OpenAI API Key** in the sidebar.
3. Start chatting!

## Dependencies
- **Streamlit**: For building the UI
- **Langchain**: For conversational memory and chaining
- **OpenAI API**: For accessing the GPT-4o model

## Configuration
- You need an OpenAI API key to use this chatbot.
- The chatbot maintains a **3-message memory window** to enhance conversation continuity.

## Future Improvements
- Add support for more LLMs (Llama, Claude, etc.)
- Improve memory handling for long conversations
- Integrate a database for persistent chat history

## License
This project is licensed under the **MIT License**.

---
Made with ❤️ using Python + Langchain + Streamlit.
