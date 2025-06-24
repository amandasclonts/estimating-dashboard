import streamlit as st
import base64
import fitz  # PyMuPDF
import docx

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
    "Proposal Checklist",
    "Proposal & Specs",
    "More Coming Soon"
])

with tabs[0]:
    st.subheader("📑 Estimate Analyzer")
    st.info("This can show basic project info (name, client, location, scope), estimator assigned, timeline (start/target completion). status, estimated cost.")
    st.info("Automation ideas: Autofill from forms (pdf, word, etc) and AI-generated short project summary based on scope")

with tabs[1]:
    st.subheader("📐 Takeoff Helper")
    st.info("Purpose: Track all material estimates and calculations")
    st.info("What to show: CSV upload or form input for material quantities, Auto-calculated material cost based on price database")
    st.info("Automation ideas: AI-powered OCR to pull takeoffs from drawings or PDFs, Price lookup from vendor APIs or price sheets, Auto-detect errors like unit mismatches or missing quantities")

with tabs[2]:
    st.subheader("💵 Unit Pricing Tool")
    st.info("Purpose: Calculate time and labor cost by task or phase")
    st.info("What to show: Labor hours per task, Cost per crew, Total labor cost")
    st.info("Automation ideas: Use AI to suggest labor hours based on past similar jobs, Pull crew rates from a central table, Predict labor bottlenecks or over-allocations")

with tabs[3]:
    st.subheader("📋 Scope Review Assistant")
    st.info("Purpose: Let AI analyze and optimize estimates")
    st.info("Ideas: Compare your numbers to similar past jobs and flag outlines, Suggest missing line items or hidden costs, Recommend markup based on market trends or workload")

with tabs[4]:
    st.subheader("📊 Bid Summary Generator")
    st.info("Purpose: Visual summary of where money is going")
    st.info("What to show: Pie chart or graph for: material, labor, equipment, subcontractos, overhead, profit")
    st.info("Automation ideas: Auto-generate charts from uploaded Excel/CSV files, Let estimators interactively adjust markup and see live effects")

with tabs[5]:
    st.subheader("✅ Proposal Checklist")

    uploaded_file = st.file_uploader("Upload a Proposal (PDF or Word)", type=["pdf", "docx"])

    def extract_text_from_pdf(file):
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text

    def extract_text_from_docx(file):
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])

    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            proposal_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
            proposal_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file type.")
            st.stop()

        st.success("✅ Proposal uploaded and text extracted!")
        st.text_area("📄 Extracted Text", proposal_text, height=300)

        st.warning("⚠️ AI checklist comparison will be added once checklist/API is provided.")

with tabs[6]:
    st.subheader("↔️ Proposal & Specs Cross-Check")

    st.markdown("### 📤 Upload Proposal Document")
    proposal_file = st.file_uploader("Upload your proposal (PDF or DOCX)", type=["pdf", "docx"], key="proposal")

    st.markdown("### 📤 Upload Specification Document")
    specs_file = st.file_uploader("Upload specifications (PDF only)", type=["pdf"], key="specs")

    if proposal_file and specs_file:
        import fitz  # PyMuPDF
        from docx import Document
        import io

        def extract_text_from_pdf(file):
            doc = fitz.open(stream=file.read(), filetype="pdf")
            text = ""
            for page in doc:
                text += page.get_text()
            return text

        def extract_text_from_docx(file):
            doc = Document(file)
            return "\n".join([p.text for p in doc.paragraphs])

        # Get proposal text
        if proposal_file.name.endswith(".pdf"):
            proposal_text = extract_text_from_pdf(proposal_file)
        else:
            proposal_text = extract_text_from_docx(proposal_file)

        # Get specs text
        specs_text = extract_text_from_pdf(specs_file)

        # Look for "Thermal and Moisture Protection" section
        if "Thermal and Moisture Protection" in specs_text:
            st.success("Found 'Thermal and Moisture Protection' in specifications.")
            st.markdown("🔍 We'll check that this section is adequately covered in your proposal when checklist logic is added.")
        else:
            st.warning("Could not find 'Thermal and Moisture Protection' in the specs document.")

        # (Placeholder for checklist comparison logic)
        st.info("✅ Document extraction complete. Proposal and specs are ready for checklist logic.")


with tabs[7]:
    st.info("🚧 Stay tuned for more tools here!")
