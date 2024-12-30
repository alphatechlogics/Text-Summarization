# 🚀 Text Summarization App

A streamlined and efficient web-based application for **summarizing text**, built using 🧠 `LangChain`, 🌟 `Streamlit`, and the **Gemma2-9b-It** language model.

---

## ✨ Features

- 📝 **Text Summarization**: Generate concise and to-the-point summaries of any input text, regardless of length.
- ⚡ **Powered by Cutting-Edge LLM**: Utilizes the **Gemma2-9b-It** model via LangChain for accurate and context-aware summaries.
- 💻 **User-Friendly Interface**: Simple, fast, and intuitive interface for seamless text summarization.

---

## 🤖 About the Model: Gemma2-9b-It

The **Gemma2-9b-It** model, created by Google, is a lightweight yet powerful **open large language model** designed for a variety of text generation tasks, including summarization. This app leverages the model's capabilities to produce **concise and to-the-point summaries**.

### Key Features

- **Expertise in Summarization**: Designed to produce high-quality, contextually relevant summaries that respect the nuances of the input text.
- **Scalability**: Efficiently handles varying input lengths while maintaining summary quality.
- **Efficient Deployment**: Optimized for environments with limited resources, such as laptops, desktops, or cloud infrastructure.
- **Open-Source**: Provides accessible innovation, fostering development in Responsible AI.

### Model Information

- **Type**: Text-to-text, decoder-only large language model.
- **Training Data**:
  - Trained on 8 trillion tokens from diverse sources, including web documents, code, and mathematical texts.
  - Focus on high-quality English-language data.
- **Evaluation Benchmarks**:
  - Achieves state-of-the-art results in summarization and text generation.
  - Benchmarks include:
    - **MMLU (5-shot)**: 71.3%
    - **ARC-e (0-shot)**: 88.0%
    - **GSM8K (5-shot)**: 68.6%
- **Maximum Token Limit**: Capable of processing up to **8,192 tokens**, ensuring robust handling of lengthy texts.

### Model Training and Hardware

- **Hardware**: Trained using **TPUv5p** (Tensor Processing Units), which provide high performance and scalability.
- **Software**: Built with **JAX** and **ML Pathways**, allowing efficient training and deployment.

### Intended Usage

- **Primary Tasks**:
  - Text summarization for research papers, reports, and long-form content.
  - General text generation and reasoning tasks.
- **Limitations**:
  - Model outputs rely on training data quality and may not always provide accurate factual statements.
  - Context ambiguity and subtle language nuances can affect response quality.

### Ethical Considerations

- **Bias Mitigation**: Rigorous filtering applied to training data to minimize biases and harmful content.
- **Privacy**: Data preprocessing ensures removal of Personally Identifiable Information (PII).
- **Responsible Use**: Users are encouraged to implement content safety measures and adhere to guidelines provided in the **Responsible Generative AI Toolkit**.

### Why Gemma2-9b-It?

This model combines cutting-edge technology with accessibility, making it a perfect choice for developers and researchers seeking powerful, open large language models tailored for Responsible AI development.

For more technical details, visit the [Gemma Model Page](https://huggingface.co/google/gemma-2-9b-it).

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/text-summarization-app.git
cd text-summarization-app
```

### 2. **Set up a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

### 3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

### **\*4. Configure API Key**

- Add your GROQ_API_KEY to Streamlit secrets.
- If running locally, create a .env file in the root directory:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 4. **Run the app:**

```bash
streamlit run app.py
```

## 🎮 Usage

1. Open the app in your browser (default: http://localhost:8501).
2. Get your summary instantly!
