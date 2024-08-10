from src.rag_pipeline import answer_question

def chatbot():
    print("Chatbot LLM com RAG: Pergunte algo sobre o conteúdo do PDF.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit"]:
            print("Encerrando o chatbot.")
            break
        response = answer_question(user_input)
        print(f"Bot: {response}")
