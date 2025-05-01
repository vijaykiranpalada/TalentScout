# TalentScout Hiring Assistant Chatbot

An intelligent, context-aware chatbot built using **Streamlit** and **OpenAI's GPT model** to assist TalentScout, a fictional recruitment agency, 
in screening tech candidates based on their experience and declared tech stack.

## 🚀 Features

- Friendly conversational UI built with **Streamlit**
- Collects essential candidate information (name, email, experience, location, etc.)
- Prompts users to declare their **tech stack**
- Dynamically generates **3-5 technical questions** per tech/tool using GPT
- Gracefully handles errors, unexpected inputs, and exits
- Modular, readable, and well-documented code

## 📁 Project Structure

├── app.py                  # Streamlit app interface
├── utils.py                # Helper functions (validation, LLM prompts)
├── .env                    # Environment file (for OpenAI key)
├── .gitignore              # Prevents sensitive info from being tracked
└── README.md               # Project documentation

## 🧠 Technologies Used

- Python 3.8+
- Streamlit
- OpenAI GPT-3.5/4 (via API)
- dotenv (for environment variable loading)

## 🔐 Environment Setup

1. Clone the repository
   
2. Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate
3. create requirements.txt file
langchain,
langchain-openai,
pydantic,
openai,
re,
streamlit,
python-dotenv,

4. Install dependencies:
pip install -r requirements.txt

5. Create a `.env` file:
OPENAI_API_KEY=your-openai-api-key-here

6.Create a .gitignore File
Ensure sensitive files like .env are not tracked by Git.

## 🖥️ Running the App
streamlit run app.py

⚙️ Technical Details

Libraries Used

streamlit: UI rendering

openai: LLM API for question generation

re, os: Validation and env variable handling

python-dotenv: Environment variable loader (optional)

Model Used

OpenAI GPT

Architectural Decisions

Modular code in app.py and utils.py

Stateless logic managed via Streamlit session state

Questions are dynamically generated per tech stack input

Graceful fallbacks for validation and API errors

✍️ Prompt Design

Prompts are tailored to ensure relevance and accuracy:

Info Gathering: Guided inputs for name, email, phone, etc., using form fields.

Tech Stack: Candidates are asked to list technologies in a comma-separated format.

Question Generation Prompt:

Generate 3-5 technical interview questions to assess proficiency in [TECH]. The questions should be challenging, relevant, and concise.

This system prompt sets the model's role as a technical interviewer, guiding it to stay on-topic and generate skill-based questions.

🚧 Challenges & Solutions

1. Sensitive Data Handling

Challenge: Avoid hardcoding API keys and exposing personal info.
Solution: Environment variables and .gitignore to exclude .env files.

2. Maintaining Context

Challenge: Ensuring a logical conversation flow between form steps.
Solution: Leveraged st.session_state to track candidate progress and inputs.

3. Question Quality Consistency

Challenge: Ensuring that GPT produces relevant, unique questions.
Solution: Used a consistent prompt template with adjusted temperature and max_tokens to balance creativity and relevance.

## 👨‍💻 Author
vijay Kiran Palada – 9059696060
mail: vijaykiran.palada@gmail.com
