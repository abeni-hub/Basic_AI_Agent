from langchain_ollama import OllamaLLM

#Load AI Model from Ollama
llm = OllamaLLM(model="mistral")

print("\n Welcome to Your AI Agent! Ask me anything.")

while True:
    question = input("Your Question {or type 'exit' to quit}: ")
    if question.lower() == 'exit':
        print("Goodbye!")
        break
    response = llm(question)
    print(f"AI Response: {response}\n")