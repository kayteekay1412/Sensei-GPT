# Sensei GPT

Sensei GPT is an interactive learning assistant built with Streamlit and OpenAI's GPT models. The app enables users to learn about any topic by selecting a GPT model and inputting a topic of interest. Once a topic is provided, Sensei GPT generates an informative response to teach the user.

---

## Features

- **Interactive Learning**: Input a topic and get a detailed explanation from GPT.
- **Model Selection**: Choose between OpenAI's `gpt-3.5-turbo` and `gpt-4` models.
  
---

## Technologies Used

- **Streamlit**: Framework for building the interactive web application.
- **OpenAI API**: For generating responses using GPT models.
- **Python**: Backend scripting and logic.

---

## Installation

Follow these steps to set up and run the project locally:

### Prerequisites
- Python 3.7+
- OpenAI API Key

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/kayteekay1412/sensei-gpt.git
   cd sensei-gpt
   ```

2. Add your OpenAI API key:
   ```python
   user = OpenAI(api_key="[ENTER API KEY HERE]")
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8501` to access the app.

---

## Usage

1. Launch the app and choose a GPT model (e.g., `gpt-3.5-turbo` or `gpt-4`).
2. Enter a topic you'd like to learn about in the input box.
3. Click the "Teach me" button.
4. Sensei GPT will generate and display an informative response about your topic.

---

## Example

1. Select `gpt-4` from the dropdown.
2. Input: `Quantum Physics`
3. Click "Teach me".
4. Receive a detailed explanation of quantum physics.

---
