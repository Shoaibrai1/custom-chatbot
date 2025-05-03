import streamlit as st
import re
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import time


def initialize_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        with st.spinner("Downloading language resources (first time only)..."):
            nltk.download('punkt')
            nltk.download('stopwords')

initialize_nltk()


RULES = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "greetings", "good afternoon", "good evening"],
        "responses": [
            "Hello! Welcome to **AI Vista Solutions**. How can I assist you today?",
            "Hi there! I'm your AI Vista assistant. What can I do for you?",
            "Greetings! I'm ALI from AI Vista Solutions. How may I help you?"
        ]
    },
    "bot_name": {
        "patterns": ["what is your name", "who are you", "your name", "what should I call you"],
        "responses": [
            "I'm **ALI** , your virtual assistant from AI Vista Solutions!",
            "You can call me **ALI** - your friendly AI helper from AI Vista Solutions!",
            "I'm **ALI**, here to assist with all your tech queries."
        ]
    },
     "gratitude": {
        "patterns": [
            "thanks", 
            "thank you", 
            "appreciate it", 
            "thanks a lot",
            "thank you very much",
            "thx"
        ],
        "responses": [
            "You're welcome!  Is there anything else I can help with?",
            "Happy to help! Let me know if you need anything else.",
            "No problem at all! Feel free to ask more questions.",
            "Glad I could assist! Don't hesitate to reach out if you have more questions."
        ]
    },
    "services": {
        "patterns": [
            "what services do you offer", "what do you develop", "can you build a website",
            "what can you create", "tell me about your services", "services", "your services",
            "capabilities", "what do you do"
        ],
        "responses": ["""**Our Services**:
- **Web Development**: React, Angular, Django, Flask
- **Mobile Apps**: Flutter, React Native, Swift
- **AI/ML Solutions**: Custom models, Computer Vision, NLP
- **Cloud Services**: AWS, Azure, GCP deployment
- **DevOps & CI/CD**: Docker, Kubernetes, Terraform

*Let me know if you'd like details about any specific service!*"""]
    },
    "pricing": {
        "patterns": [
            "how much does a website cost", "what are your rates", "pricing",
            "how much do you charge", "cost", "budget", "price"
        ],
        "responses": ["""**Pricing Structure**:
- Basic Website: $1,000 - $5,000
- Custom Web App: $5,000 - $50,000+
- Mobile App: $10,000 - $100,000
- Enterprise Solutions: Custom pricing
- *All projects include free initial consultation*"""]
    },
    "portfolio": {
        "patterns": ["show me your projects", "portfolio", "past work", "examples", "case studies"],
        "responses": [
            "You can explore our portfolio here: [AI Vista Solutions Projects](https://aivistasolutions.com/projects)",
            "Check out our recent work: [Our Portfolio](https://aivistasolutions.com/portfolio)"
        ]
    },
    "contact": {
        "patterns": [
            "how to contact you", "email", "phone number", "get in touch",
            "contact no", "reach you", "contact details"
        ],
        "responses": ["""**Contact Us**:
 Email: contact@aivistasolutions.com  
 Phone: +92 345 1678312  
 Address: DHA Phase 9, Lahore, Pakistan  
 Website: [aivistasolutions.com](https://aivistasolutions.com)"""]
    },
    "hiring": {
        "patterns": [
            "are you hiring", "job openings", "how to apply", "careers",
            "we need developers", "hiring", "jobs", "vacancies"
        ],
        "responses": ["""**Current Openings**:
1. Senior Python Developer (Remote)
2. Frontend Engineer (React)
3. DevOps Specialist
4. AI/ML Engineer

 Apply at: [AI Vista Solutions Careers](https://aivistasolutions.com/careers)  
*We offer competitive salaries and flexible work arrangements!*"""]
    },
    "timeline": {
        "patterns": [
            "how long does a project take", "project duration", "delivery time",
            "when will it be ready", "timeline", "deadline"
        ],
        "responses": ["""**Typical Timelines**:
- MVP Development: 2-3 months
- Enterprise Solution: 6-12 months
- Website: 4-8 weeks
- Mobile App: 3-6 months

*Exact timeline depends on project complexity*"""]
    },
    "location": {
        "patterns": [
            "where are you located", "address", "location", "your office",
            "Software location", "based in", "headquarters"
        ],
        "responses": ["""**Our Locations**:
 **HQ**: Lahore, Pakistan  
 **Development Center**: DHA Phase 9, Lahore  
 **Global Presence**: USA, Germany, UAE"""]
    },
    "technology": {
        "patterns": [
            "what tech do you use", "technology stack", "programming languages",
            "frameworks", "tech stack", "tools"
        ],
        "responses": ["""**Our Tech Stack**:
```

    Frontend-->React
    Frontend-->Angular
    Backend-->Python
    Backend-->Node.js
    Database-->PostgreSQL
    Database-->MongoDB
    DevOps-->AWS
    DevOps-->Docker
```"""]
    },
    "about": {
        "patterns": ["about", "company", "history", "who are you", "background"],
        "responses": ["""**About AI Vista Solutions**:
 Founded in 2015  
 50+ technology experts  
 200+ successful projects delivered  
 Serving clients in 15+ countries

**Why Choose Us?**:
 95% client retention rate  
 Agile development approach  
 Dedicated project managers"""]
    },
    "default": {
        "responses": [
            "I'm not sure I understand. Could you rephrase your question?",
            "Let me connect you to a human expert who can help...",
            "Try asking about our services, pricing, or portfolio!",
            "I'm still learning! Could you ask about our capabilities or services?"
        ]
    }
}

def preprocess_text(text):

    try:
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in stopwords.words('english')]
        return " ".join(tokens)
    except Exception:
        return text.lower()  

def detect_intent(user_input):
   
    processed_input = preprocess_text(user_input)
    for intent, data in RULES.items():
        for pattern in data.get("patterns", []):
            if re.search(r'\b' + re.escape(pattern) + r'\b', processed_input):
                return intent
    return "default"

def get_response(intent):
    
    return random.choice(RULES[intent]["responses"])


def main():
    st.set_page_config(
        page_title="AI Vista Solutions Assistant",
        
        layout="centered",
        initial_sidebar_state="expanded"
    )
    st.markdown(
    """
    <h2 style='text-align: center; color: #4B8BBE; font-family: "Georgia", serif;'>
         Created by <strong>Muhammad Shoaib</strong>
    </h2>
    """,
    unsafe_allow_html=True
        )


    

    
    st.title(" AI Vista Solutions Assistant")
    st.markdown("Ask about our **services**, **pricing**, **careers**, or **technical capabilities**!")

    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm Your AI Vista Solutions Assistant. How can I help you today?"}
        ]

   
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="🤖" if message["role"] == "assistant" else None):
            st.markdown(message["content"])

    
    if prompt := st.chat_input("Type your question here..."):
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        
        with st.spinner("Thinking..."):
            time.sleep(0.5)  
            
           
            try:
                intent = detect_intent(prompt)
                response = get_response(intent)
            except Exception as e:
                response = " Sorry, I encountered an error. Please try again."
                st.error(f"System error: {str(e)}")

        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(response)

        
        st.rerun()

if __name__ == "__main__":
    main()
