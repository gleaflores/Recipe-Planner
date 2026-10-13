import streamlit as st
from groq import Groq
import os

# 1. Page Configuration & UI Branding
st.set_page_config(page_title="AI Meal Recipe Planner (Groq)", page_icon="🍳", layout="centered")
st.title("🍳 AI Meal Recipe Planner")
st.write("Turn your leftover ingredients into healthy, structured recipes using Groq & Llama 3!")

# 2. Securely Retrieve the Groq API Key
# Looks for an environment variable. If missing, allows temporary sidebar entry.
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    st.warning("⚠️ Groq API Key missing. Please input your key in the sidebar to test.")
    api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

if api_key:
    # Initialize the official Groq SDK Client
    client = Groq(api_key=api_key)
    
    # 3. User Inputs Form Section
    st.header("1. Your Preferences")
    ingredients = st.text_area("What ingredients do you have? (comma-separated)", 
                               placeholder="e.g., chicken breasts, broccoli, rice, garlic, olive oil")
    
    col1, col2 = st.columns(2)
    with col1:
        diet = st.selectbox("Dietary Restrictions:", 
                            ["None", "Vegetarian", "Vegan", "Gluten-Free", "Keto", "Dairy-Free"])
    with col2:
        goal = st.selectbox("Fitness Goal:", 
                            ["Balanced", "High Protein / Muscle Building", "Low Calorie / Weight Loss", "Quick & Easy"])

    # 4. Trigger Recipe Generation
    if st.button("Generate Recipe ✨", type="primary"):
        if not ingredients.strip():
            st.error("Please enter at least one ingredient.")
        else:
            with st.spinner("Chef Llama is crafting your recipe instantly... Please wait."):
                try:
                    # Constructing the recipe engineering prompt
                    prompt = f"""
                    You are a professional chef and nutritionist. 
                    Create a detailed, healthy recipe using these ingredients: {ingredients}.
                    Respect the following dietary restriction: {diet}.
                    Align the meal structure with this fitness goal: {goal}.
                    
                    Format your response beautifully using clear Markdown sections:
                    - **Recipe Title** (Catchy name)
                    - **Nutritional Overview** (Estimated calories, protein, carbs, fats)
                    - **Prep & Cook Time**
                    - **Ingredients Checklist** (Include items listed plus common pantry staples like salt, water, oil)
                    - **Step-by-Step Cooking Instructions**
                    - **Chef's Tip** (A dynamic variation or storage suggestion)
                    """
                    
                    # Call Groq's high-speed completion API using the Llama 3.3 model endpoint
                    response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant that strictly outputs clean, structured markdown text."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                        max_tokens=2048
                    )
                    
                    # 5. Render Output to UI
                    st.success("Recipe generated successfully!")
                    st.markdown("---")
                    st.markdown(response.choices[0].message.content)
                    
                except Exception as e:
                    st.error(f"An error occurred while connecting to Groq: {e}")
else:
    st.info("Provide a Groq API Key to unlock the recipe generation module.")