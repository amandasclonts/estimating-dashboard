import streamlit as st
import base64

# --- Config ---
st.set_page_config(page_title="Estimating AI Dashboard", layout="wide")

# --- Password Gate ---
def check_password():
    def password_entered():
        if st.session_state["password"] == "Wbg3033!":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter password", type="password", on_change=password_entered, key="password")
        st.stop()
    elif not st.session_state["password_correct"]:
        st.error("❌ Incorrect password")
        st.stop()

check_password()

# --- Branding ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
        return f"data:image/jpeg;base64,{encoded}"

encoded_logo = get_base64_image("logo.jpg")
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src="{encoded_logo}" style='width: 375px; margin-bottom: 10px;' />
        <h1 style='color: white; font-size: 36px;'>🧮 Estimating AI Dashboard</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Tabs Layout ---
tabs = st.tabs([
    "Estimate Analyzer", 
    "Takeoff Helper", 
    "Unit Pricing", 
    "Scope Review", 
    "Bid Summary", 
    "More Coming Soon"
])

with tabs[0]:
    st.subheader("📑 Estimate Analyzer")
    st.info("Tool coming soon.")
    st.info("This can show basic project info (name, client, location, scope), estimator assigned, timeline (start/target completion). status, estimated cost.")
    st.info("Automation ideas: Autofill from forms (pdf, word, etc) and AI-generated short project summary based on scope")

with tabs[1]:
    st.subheader("📐 Takeoff Helper")
    st.info("Tool coming soon.")
    st.info("Purpose: Track all material estimates and calculations")
    st.info("What to show: CSV upload or form input for material quantities, Auto-calculated material cost based on price database")
    st.info("Automation ideas: AI-powered OCR to pull takeoffs from drawings or PDFs, Price lookup from vendor APIs or price sheets, Auto-detect errors like unit mismatches or missing quantities")

with tabs[2]:
    st.subheader("💵 Unit Pricing Tool")
    st.info("Tool coming soon.")
    st.info("Purpose: Calculate time and labor cost by task or phase")
    st.info("What to show: Labor hours per task, Cost per crew, Total labor cost")
    st.info("Automation ideas: Use AI to suggest labor hours based on past similar jobs, Pull crew rates from a central table, Predict labor bottlenecks or over-allocations")

with tabs[3]:
    st.subheader("📋 Scope Review Assistant")
    st.info("Tool coming soon.")
    st.info("Purpose: Let AI analyze and optimize estimates")
    st.info("Ideas: Compare your numbers to similar past jobs and flag outlines, Suggest missing line items or hidden costs, Recommend markup based on market trends or workload")

with tabs[4]:
    st.subheader("📊 Bid Summary Generator")
    st.info("Tool coming soon.")
    st.info("Purpose: Visual summary of where money is going")
    st.info("What to show: Pie chart or graph for: material, labor, equipment, subcontractos, overhead, profit")
    st.info("Automation ideas: Auto-generate charts from uploaded Excel/CSV files, Let estimators interactively adjust markup and see live effects")

with tabs[5]:
    st.info("🚧 Stay tuned for more tools here!")
