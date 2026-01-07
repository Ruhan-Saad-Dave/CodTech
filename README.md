# CodTech

This repository is created for storing the code for the task of my internship.
- Company: CodTech IT Solutions PVT.LTD 
- Duration: 6 weeks 
- Role: Artificial Intelligence 
- Date: 03 Jan 2026 ~ 14 February 2026 
<br>
For my daily journal of the work that I have done everyday, refer to [Devlog](#Devlog).

## Setting Up
Make sure that you have installed the latest Python version, and an IDE for executing the code like VSCode.
- [Download Python](https://www.python.org/downloads/)
- [Download VSCode](https://code.visualstudio.com/download)
To install the dependencies:
```bash
pip install uv
uv sync
```
The code to run each file will be given in the below sections.

### Special Note:
The main code is stored in the "main.py" file of each folder. There is also a "simple.py" file which has the minimum code that fully satisfies the requirement, "main.py" just adds on more features to make it look more impressive. There is also a Jupyter notebook called "main.ipynb" which can be used to increase the execution speed, it is recommended to use the google collab extension for the execution as some of the code takes lots of processing power. There is a discovered bug that despite the code is stored on github, "main.ipynb" sometimes remains empty, to solve that just copy paste the code and execute it, special instruction will be given below for each task.

### Tasks explaination:
#### Task1: Text Summarizer Tool
Create a tool that Summarizes Lengthy Arthicles Using Natural Language Processing Techniques.
<hr>
Hugging Face's "Transformer" library has a function called "pipeline()", in it we can pass different types of arguement like "text-classification", "automatic-speech-recognition", "depth-estimation" and more (Check [here](https://huggingface.co/docs/transformers/en/main_classes/pipelines) for more info), and within these tasks there is one called "summarization".<br>
Behind the function, it uses a pretrained model like "bart-large-cnn", "google-t5/t5-small", etc are used which speciallizes in text summarization. Although the approach doesn't look much like NLP approach, these models use complex NLP techniques to summarize the text. Also in professional scenario, it is always recommended to use pre-trained model instead of building and training one from scratch as it helps to reduce time and cost.<br>
The simple approach maintains a while loop so that the user can keep on summarizing text in the terminal, while the complex approach (main.py) adds features like user interface and summarizing text from a file. The user interface is build using [Gradio](https://www.gradio.app/docs/gradio/chatinterface), which is a python library that sort of builds a website. It is mainly used by Data Scientists and AI Engineers to present the workings of their model to a non-AI related team member. For reading the PDF file, [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) is used, python has built in method to read text files. When user uploads a text or pdf file, the system will read the contents and give this content to the "pipeline" for summarization task.<br>
To execute [Main file of Task1](#Task1/main.py):
```bash
uv run Task1/main.py
```
To execute [Simple version of Task1](#Task1/simple.py):
```bash
uv run Task1/simple.py
```

#### Task2: Speech Recognition System
Build a basic Speech-To-Text system using Pre-trained models and libraries like SpeechRecognition or Wav2Vec.
<hr>
Python has a library called [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), which is able to perform Speech-To-Text tasks. In the background it uses Google Speech recognition for processing the audio into audio.<br>
In the simple file, the system asks the user to speak, and after few seconds the recording stops, and the transcribed text is displayed. All of these are done in the terminal.<br>
For the complex file, Gradio is again used for user interface, and this time [OpenAI Whisper](https://pypi.org/project/openai-whisper/) is used for multilingual purposes to understand the print out non-english languages (it can understand english too). Whisper is also capable of speech translation and language identification. It is trained on a large diversity of data.<br>
To execute [Main file of Task2](#Task2/main.py):
```bash
uv run Task2/main.py
```
To execute [Simple version of Task2](#Task2/simple.py):
```bash
uv run Task2/simple.py
```

#### Task3: Natural Style Transfer
Implement a neural style transfer model to apply artistic styles to photographs.
<hr>
More details coming soon.

#### Task4: Generative Text Model
Create a text generation model using GPT or LSTM to generate coherent paragraphs on specify topics.
<hr>
The easiest way to do this is by using Google Gemini via Langchain. [Langchain](https://docs.langchain.com/oss/python/learn) is a python library that is mainly used for developing AI and agentic application, it supports many models (including API models and ones from huggingface), it also can build pipelines for prompts, file reading, agentic tools etc. [Google Gemini](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai) is used as recently Google gave 1 year pro subscription to all students, so development using it is much easier.<br>
The simple method creates a loop where user can continuosly generate content. Note that the task mentioned about content generation not actual chatbot, so there is no need to maintain history.<br>
The complex method again uses Gradio for user interface, also the user will be able to easily copy the text or regenerate the response.<br>
To execute [Main file of Task4](#Task4/main.py):
```bash
uv run Task4/main.py
```
To execute [Simple version of Task4](#Task4/simple.py):
```bash
uv run Task4/simple.py
```

<br><br><hr>
Thank you for visiting this repo, for more questions please use the "Issues" section on github, or [email me](ruhandave2003@gmail.com)