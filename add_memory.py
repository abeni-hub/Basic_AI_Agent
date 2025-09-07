from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load AI Model from Ollama
llm = OllamaLLM(model="mistral")

# Initialize chat message history
chat_history = ChatMessageHistory() # Stores the AI conversation history

# Define AI chat Prompt
prompt = PromptTemplate(
    input_variables=["history", "question"],
    template = "Previous conversation:\n{history}\n\nNew question: {question}\nAI response: "
)

def run_chain(function):
    # Retrieve the chat history manually
    chat_history_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history.messages])
    
    # Run AI model with the prompt and chat history
    response = llm.invoke(prompt.format(history=chat_history_text, question=function))

    # Store new user and AI response in chat history
    chat_history.add_user_message(function)
    chat_history.add_ai_message(response)

    return response 

# Interactive CLI chatbot
print("\n Welcome to Your AI Agent with Memory! Ask me anything.")
print("Type 'exit' to quit.\n")

while True:
    question = input("Your Question: ")
    if question.lower() == 'exit':
        print("Goodbye!")
        break
    response = run_chain(question)
    print(f"AI Response: {response}\n")