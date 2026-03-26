# Virtual Resume Chatbot

> An AI chatbot that answers recruiter and hiring manager questions about my experience, skills, and projects — live on HuggingFace Spaces.

[![HuggingFace Spaces](https://img.shields.io/badge/HuggingFace-Spaces-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/spaces)
[![Gradio](https://img.shields.io/badge/Gradio-UI-FF7C00?logo=gradio)](https://gradio.app)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)

---

## What This Is

Instead of a static PDF resume, this is a conversational interface trained on my background. Ask it anything: what projects I've shipped, what stack I work with, what roles I'm targeting, what I did at PM Accelerator. It answers based on actual resume content, not hallucination.

Built as a practical demo of RAG-based personalization — and honestly, a better recruiter experience than scrolling through a PDF.

**Live demo:** [Try it on HuggingFace Spaces →](https://huggingface.co/spaces/jibz33on/virtual-resume-chatbot)

---

## What You Can Ask

- *"What's Jibin's experience with LangChain and RAG?"*
- *"Has he worked with multi-agent systems?"*
- *"What's his most technically complex project?"*
- *"Is he open to remote roles?"*
- *"What's his current tech stack?"*

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| UI / Interface | Gradio |
| Hosting | HuggingFace Spaces |
| Language | Python 3.11 |

---

## How It Works

The chatbot uses a retrieval layer over resume content. The resume is chunked, embedded, and stored so that each user query retrieves the most relevant sections before generating a response. This keeps answers grounded and factual rather than generic.

```
User Query
    → Retrieve relevant resume sections
    → Construct prompt with context
    → LLM generates answer
    → Gradio renders response
```

---

## Running Locally

```bash
git clone https://github.com/jibz33on/virtual-resume-chatbot
cd virtual-resume-chatbot

pip install -r requirements.txt
```

Set your API key:

```bash
export OPENAI_API_KEY=sk-...
```

Launch:

```bash
python src/app.py
```

The Gradio interface opens at `http://localhost:7860`.

---

## Project Structure

```
virtual-resume-chatbot/
├── src/
│   └── app.py          # Main Gradio app
├── data/
│   └── resume.txt      # Resume content (source of truth)
├── requirements.txt
└── README.md
```

---

## Why This Exists

Recruiters scan dozens of profiles. A chatbot that answers specific questions in 5 seconds beats a resume they'll spend 10 seconds on. It also demonstrates the exact thing I build professionally: RAG systems that make information queryable.

---

## Author

**Jibin Kunjumon** — AI Engineer  
[GitHub](https://github.com/jibz33on) · [LinkedIn](https://linkedin.com/in/jibin-kunjumon) · [HuggingFace](https://huggingface.co/jibz33on)
