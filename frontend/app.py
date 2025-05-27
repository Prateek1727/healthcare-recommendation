import streamlit as st
import requests

st.set_page_config(page_title="MediRecs: Healthcare Recommendation", layout="centered")

st.title("🩺 Personalized Healthcare Recommendation System")

st.write("Enter patient conditions and get personalized plan recommendations.")

# Input section
conditions = st.text_input("Patient Conditions (comma separated)", placeholder="e.g. hypertension, anxiety")

plans_db = [
    {"name": "Low Salt Diet", "condition": "hypertension"},
    {"name": "Cardio Exercise", "condition": "obesity"},
    {"name": "Stress Management", "condition": "anxiety"},
]

if st.button("Get Recommendations"):
    if not conditions.strip():
        st.warning("Please enter at least one condition.")
    else:
        user_profile = {"conditions": [c.strip() for c in conditions.split(",") if c.strip()]}
        try:
            resp = requests.post(
                "http://localhost:8000/recommend",
                json={"user_profile": user_profile, "plans_db": plans_db},
                timeout=10
            )
            if resp.status_code == 200:
                data = resp.json()
                recommendations = data.get("recommendations", [])
                st.subheader("Recommended Plans:")
                if recommendations:
                    for rec in recommendations:
                        st.markdown(f"- **{rec['name']}** (_{rec['condition']}_)")
                else:
                    st.info("No recommendations found for these conditions.")
            else:
                st.error(f"API Error: {resp.status_code} - {resp.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")

st.markdown("---")
st.caption("Powered by MediRecs · Example project")