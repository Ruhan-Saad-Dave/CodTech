from transformers import pipeline 
from typing import List, Dict
import gradio as gr
import pymupdf as fitz

pipe = pipeline("summarization") #Hugging face function, which uses complex NLP techniques under the hood to summaries the text.

def summarize(user_data: Dict , history: List) -> str:
    """
    Used by the interface, receives user input and file uploads.

    Args:
        user_data (dict): Dictionary containing 'text' and 'files' keys.
        history (list): Chat history (not used in this function).
    Returns:
        str: Summarized text.
    """
    try:
        message = user_data.get("text", "")
        files = user_data.get("files", [])

        if files == []: #No file uploaded, just plain text
            summary = pipe(message)
            output = summary[0]['summary_text']
            return output
        elif files != [] and message == "": #when only file is given
            if files[0] == ".txt": #pasted text is treated as .txt file
                with open(files[0], 'r') as f:
                    file_content = f.read()
                summary = pipe(file_content)
                output = summary[0]['summary_text']
                return output
            elif files[0] == ".pdf": #use PyMuPDF to read pdf files
                pdf_reader = fitz.open(files[0])
                text = ""
                for page in pdf_reader:
                    text += page.get_text("text")
                pdf_reader.close()
                summary = pipe(text)
                output = summary[0]['summary_text']
                return output
            else:
                return "Unsupported file format. Please upload a .txt or .pdf file."
        else:
            return "Please provide either text or file, not both."
    except Exception as e:
        return f"An error occurred: {str(e)}"


demo = gr.ChatInterface(fn=summarize,
                        title= "Text Summarization Bot",
                        multimodal=True
                        )
demo.launch()