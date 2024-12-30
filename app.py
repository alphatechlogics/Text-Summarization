from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain import PromptTemplate
import streamlit as st

# Initialize LangChain ChatGroq
api_key = st.secrets["GROQ_API_KEY"]  # Retrieve the API key from Streamlit secrets
llm = ChatGroq(groq_api_key=api_key, model="gemma2-9b-it")

# Function to summarize text
def summarize_text(text):
    template = """
    You are an expert at summarizing text. Based on the length of the input text, provide a concise, very short, not lengthy and to-the-point summary.
    Text: {text}
    """
    prompt = PromptTemplate(input_variables=["text"], template=template)
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    result = llm_chain.run({"text": text})
    return result

# Streamlit app
st.set_page_config(layout="wide")
st.title("Text Summarization")

# User input for text
text_input = st.text_area("Enter the text to summarize:", height=300)

# Generate summary on button click
if st.button("Summarize"):
    with st.spinner("Processing..."):
        try:
            summary = summarize_text(text_input)
            st.subheader("Summary:")
            st.success(summary)
        except Exception as e:
            st.error(f"Error: {e}")
