from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def generate(user_data, history):
    messages = [
    (
        "system",
        "You are a helpful assistant that generates content. You are strictly to generate content based on user input and cannot perform tasks like question answering or summarization.",
    ),
    ("human", "I love programming."),
]
    response = model.invoke(messages)
    
    return response.content

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(placeholder="Ask me anything...")
    gr.ChatInterface(fn=generate,
                        title= "Text generation Bot",
                        chatbot = chatbot,
                        )
demo.launch()