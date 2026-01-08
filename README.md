# CodTech AI Internship Tasks

This repository contains the projects completed during my Artificial Intelligence internship at CodTech IT Solutions.

### Project Overview
- **Company:** CodTech IT Solutions PVT.LTD
- **Role:** Artificial Intelligence Intern
- **Duration:** 6 Weeks (03 Jan 2026 - 14 Feb 2026)

For a daily journal of my work, please refer to the [DevLog](./DevLog/).

---

## Table of Contents
- [Setup and Installation](#setup-and-installation)
- [Project Structure](#project-structure)
- [Task Explanations](#task-explanations)
  - [Task 1: Text Summarizer Tool](#task-1-text-summarizer-tool)
  - [Task 2: Speech Recognition System](#task-2-speech-recognition-system)
  - [Task 3: Neural Style Transfer](#task-3-neural-style-transfer)
  - [Task 4: Generative Text Model](#task-4-generative-text-model)
- [Usage](#usage)
- [Contact](#contact)

---

## Setup and Installation

To get started, you'll need Python, a code editor like VSCode, and Git installed on your system.

1.  **Prerequisites:**
    - [Download Python](https://www.python.org/downloads/)
    - [Download VSCode](https://code.visualstudio.com/download)
    - [Download Git](https://git-scm.com/install/)

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/Ruhan-Saad-Dave/CodTech.git
    cd CodTech
    ```

3.  **Install dependencies:**
    This project uses `uv` for fast dependency management.
    ```bash
    pip install uv
    uv sync
    ```

---

## Project Structure

Each task is organized into its own folder (e.g., `Task1/`, `Task2/`). Inside each folder, you will find three common files:

-   `main.py`: The primary, feature-rich version of the script, which often includes a Gradio-based user interface.
-   `simple.py`: A minimal, terminal-based version of the script that satisfies the core requirements of the task.
-   `main.ipynb`: A Jupyter Notebook version of the code. This is ideal for experimentation and can offer faster execution for computationally intensive tasks, especially when run on platforms like Google Colab.

> **Note:** There is a known issue where Jupyter Notebooks (`.ipynb`) may appear empty on GitHub. If you encounter this, simply copy the code from the corresponding `main.py` file and paste it into the notebook to execute it.

---

## Task Explanations

### Task 1: Text Summarizer Tool
**Objective:** Create a tool that summarizes lengthy articles using Natural Language Processing techniques.
<hr>
This tool utilizes the `pipeline()` function from Hugging Face's **Transformers** library, a powerful and common approach for summarization tasks. It uses pre-trained models like `bart-large-cnn` that employ complex NLP techniques to generate high-quality summaries. The `main.py` version provides a user-friendly interface using **Gradio**, allowing users to summarize text from direct input or uploaded PDF files (read with **PyMuPDF**).

### Task 2: Speech Recognition System
**Objective:** Build a basic Speech-To-Text system using pre-trained models.
<hr>
The core of this task is the **SpeechRecognition** library, which uses the Google Speech Recognition API to transcribe audio to text. The `main.py` version enhances this by using **OpenAI's Whisper** model for robust, multilingual speech recognition through a **Gradio** interface, offering higher accuracy and language flexibility.

### Task 3: Neural Style Transfer
**Objective:** Implement a neural style transfer model to apply artistic styles to photographs.
<hr>
Neural Style Transfer blends the content of one image with the artistic style of another. This implementation uses a pre-trained model from **TensorFlow Hub** (`magenta/arbitrary-image-stylization-v1-256`), which is highly efficient. The `main.py` script provides a **Gradio** interface where users can upload their own content and style images to create unique, stylized artwork.

### Task 4: Generative Text Model
**Objective:** Create a text generation model using GPT or LSTM to generate coherent paragraphs on specific topics.
<hr>
This task leverages **Google Gemini** through the **LangChain** framework to generate text. LangChain simplifies the process of building AI applications by providing a standard interface for interacting with various language models. The `main.py` version uses **Gradio** to create an interface for generating text on user-specified topics.

---

## Usage

To run any of the scripts, use the `uv run` command from the root directory of the project.

<details>
<summary><b>Task 1 Commands</b></summary>

```bash
# For the Gradio UI version
uv run Task1/main.py

# For the simple terminal version
uv run Task1/simple.py
```
</details>

<details>
<summary><b>Task 2 Commands</b></summary>

```bash
# For the Gradio UI version
uv run Task2/main.py

# For the simple terminal version
uv run Task2/simple.py
```
</details>

<details>
<summary><b>Task 3 Commands</b></summary>

```bash
# For the Gradio UI version
uv run Task3/main.py

# For the simple terminal version
uv run Task3/simple.py
```
</details>

<details>
<summary><b>Task 4 Commands</b></summary>

```bash
# For the Gradio UI version
uv run Task4/main.py

# For the simple terminal version
uv run Task4/simple.py
```
</details>

---

## Contact

Thank you for visiting this repository. For any questions, please use the "Issues" section on GitHub or [email me](mailto:ruhandave2003@gmail.com).
