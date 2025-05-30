
import streamlit as st
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os
import asyncio
import nest_asyncio

nest_asyncio.apply()
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    st.error("❌ GEMINI_API_KEY not found in .env file.")
    st.stop()

# Setup Gemini API client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


translator = Agent(
    name="Translator Agent",
    instructions="""
    You are a translator agent. Translate the given input text into the target language specified by the user.
    Your response should only contain the translated sentence.
    """
)

async def translate_text(input_text: str):
    return await Runner.run(translator, input=input_text, run_config=config)

st.set_page_config(page_title="AI Translator", page_icon="🌐")
st.title("🌍 AI Translator Agent (Powered by Gemini)")
language_options = {
    "Urdu": "🇵🇰 Urdu",
    "Spanish": "🇪🇸 Spanish",
    "French": "🇫🇷 French",
    "Chinese": "🇨🇳 Chinese",
    "German": "🇩🇪 German",
    "Arabic": "🇸🇦 Arabic",
    "Hindi": "🇮🇳 Hindi",
    "Turkish": "🇹🇷 Turkish",
    "Russian": "🇷🇺 Russian",
    "Japanese": "🇯🇵 Japanese"
}


language = st.selectbox("Select Target Language", list(language_options.keys()))
text_to_translate = st.text_area("Enter text to translate:")

if st.button("Translate"):
    if not text_to_translate.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("🔄 Translating..."):
            try:
                instruction = f"Translate to {language}: '{text_to_translate}'"
                result = asyncio.run(translate_text(instruction))
                st.success(f"✅ Translation to {language}:")
                st.markdown(f"### 📝 {result.final_output}")
            except Exception as e:
                st.error(f"❌ Error occurred: {str(e)}")

# Optional footer
st.markdown("---")
st.markdown("<small>Made with ❤️ using Gemini + Streamlit</small>", unsafe_allow_html=True)
