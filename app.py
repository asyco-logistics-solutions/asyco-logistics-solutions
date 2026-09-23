import base64
import io
import os
import streamlit as st

# ReportLab imports para sa PDF generation
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# Page Configuration
st.set_page_config(
    page_title="ASYCO Logistics Solutions", page_icon="🚛", layout="wide"
)


# Helper function para sa base64 background image
def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None


# Helper function para sa Company Profile PDF
def generate_company_profile_pdf():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
    )
    story = []

    styles = getSampleStyleSheet()

    # Custom Styles
    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=colors.HexColor("#112D4E"),
        spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=12,
        textColor=colors.HexColor("#3F72AF"),
        spaceAfter=12,
    )
    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        textColor=colors.HexColor("#112D4E"),
        spaceBefore=10,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "BodyTextCustom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        textColor=colors.HexColor("#1E293B"),
        leading=14,
        spaceAfter=8,
    )

    # Header
    story.append(Paragraph("ASYCO LOGISTICS SOLUTIONS", title_style))
    story.append(
        Paragraph(
            "Heavy Equipment Rentals & Logistics Services | Established 2023",
            subtitle_style,
        )
    )
    story.append(
        HRFlowable(
            width="100%",
            thickness=1.5,
            color=colors.HexColor("#112D4E"),
            spaceAfter=12,
        )
    )

    # About Us
    story.append(Paragraph("About Our Company", heading_style))
    story.append(
        Paragraph(
            "Established in 2023, ASYCO Logistics Solutions has positioned"
            " itself as a premier and trusted partner for heavy equipment"
            " rentals, specialized heavy hauling, and container drayage logistics"
            " services across the Philippines. Grounded in engineering precision,"
            " rig safety, and reliable site execution, ASYCO delivers seamless"
            " end-to-end transport solutions tailored to infrastructure"
            " development, commercial construction, energy projects, and"
            " industrial operations.",
            body_style,
        )
    )

    # Mission & Vision
    story.append(Paragraph("Our Mission & Vision", heading_style))
    story.append(
        Paragraph(
            "<b>Our Mission:</b> To deliver dependable, engineered, and"
            " uncompromisingly safe heavy haulage and lifting solutions that"
            " drive national infrastructure development through certified"
            " equipment maintenance, rigorous lift planning, dynamic capacity"
            " checks, and continuous professional training.",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>Our Vision:</b> To become the Philippines' most trusted and"
            " benchmark-setting heavy equipment rental and logistics partner"
            " across Luzon, Visayas, and Mindanao by integrating technical"
            " innovation, modern fleet management, and field-tested safety"
            " protocols.",
            body_style,
        )
    )

    story.append(Spacer(1, 8))

    # Equipment Table
    story.append(
        Paragraph("Comprehensive Equipment & Fleet Capabilities", heading_style)
    )

    equipment_data = [
        [
            Paragraph("<b>Equipment Type</b>", body_style),
            Paragraph("<b>Specifications & Capacity</b>", body_style),
        ],
        [
            Paragraph("3-5t Boom Truck", body_style),
            Paragraph(
                "Bed Capacity: 5.5T | Direct Lift Limit: 3.0T", body_style
            ),
        ],
        [
            Paragraph("7t Boom Truck", body_style),
            Paragraph(
                "Bed Capacity: 12.5T | Direct Lift Limit: 7.0T", body_style
            ),
        ],
        [
            Paragraph("10t Boom Truck", body_style),
            Paragraph(
                "Bed Capacity: 15.0T | Direct Lift Limit: 10.0T", body_style
            ),
        ],
        [
            Paragraph("16t Boom Truck", body_style),
            Paragraph(
                "Bed Capacity: 20.0T | Direct Lift Limit: 16.0T", body_style
            ),
        ],
        [
            Paragraph("Mobile Cranes (25T to 300T)", body_style),
            Paragraph(
                "25t, 50t, 80t, 100t, 110t, 150t, 200t, 300t Mobile Cranes",
                body_style,
            ),
        ],
        [
            Paragraph("Trailers & Heavy Hauling", body_style),
            Paragraph(
                "40ft Flatbed (32T), Lowbed (40T), Lowboy (55T), Challenger"
                " (100T)",
                body_style,
            ),
        ],
        [
            Paragraph("Container Drayage & Warehouse", body_style),
            Paragraph(
                "MICT/ATI South Harbor Hauling, Electric Walkie Stackers & Reach"
                " Trucks",
                body_style,
            ),
        ],
    ]

    table = Table(equipment_data, colWidths=[180, 340])
    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F1F5F9")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#112D4E")),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
        ])
    )

    story.append(table)
    story.append(Spacer(1, 10))

    # Contact Info
    story.append(Paragraph("Contact Information", heading_style))
    story.append(
        Paragraph(
            "<b>Office Address:</b> Queens Row West, Molino 3, Bacoor City,"
            " Cavite, Philippines",
            body_style,
        )
    )
    story.append(
        Paragraph(
            "<b>Email:</b> asycologisticssolutions@gmail.com", body_style
        )
    )
    story.append(
        Paragraph(
            "<b>Service Coverage:</b> Luzon, Visayas, and Mindanao", body_style
        )
    )

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()


# Apply Background Styling
bg_base64 = get_base64_of_bin_file("Background.jpg")
if bg_base64:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{bg_base64}");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Custom UI CSS
st.markdown(
    """
    <style>
    .block-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2.5rem !important;
        border-radius: 12px;
        margin-top: 1.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
    }
    
    .block-container p, .block-container span, .block-container label, 
    .block-container div, .block-container h1, .block-container h2, 
    .block-container h3, .block-container h4, .block-container h5, .block-container h6 {
        color: #112D4E !important;
        font-weight: 500;
    }

    input, textarea, .stTextInput input, .stTextArea textarea, .stNumberInput input {
        color: #FFFFFF !important;
        background-color: #1E293B !important;
    }

    [data-testid="stSidebar"] *, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] div, 
    [data-testid="stSidebar"] span {
        color: #FFFFFF !important;
        font-weight: 500;
    }

    .stButton>button, div[data-testid="stFormSubmitButton"]>button, .stDownloadButton>button {
        background-color: #112D4E !important;
        color: #FFFFFF !important;
        border-radius: 6px;
        border: none;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover, div[data-testid="stFormSubmitButton"]>button:hover, .stDownloadButton>button:hover {
        background-color: #3F72AF !important;
        color: #FFFFFF !important;
    }

    @media (max-width: 768px) {
        .block-container {
            padding: 1rem !important;
        }
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", use_container_width=True)

st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation",
    [
        "Home & Services",
        "Company Profile",
        "Instant Rate Calculator",
        "Safety Lift Checker",
        "Book a Transport",
    ],
)

# --- PAGE 1: HOME & SERVICES ---
if page == "Home & Services":
    st.title("ASYCO LOGISTICS SOLUTIONS")
    st.subheader("Heavy Equipment Rentals & Logistics Services")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🚛 Hauling & Fleet")
        st.write(
            "10-wheeler boom trucks, tractor head trailers, and flatbed"
            " transport for heavy cargo."
        )
    with col2:
        st.markdown("### 🏗️ Crane & Lifting")
        st.write(
            "Mobile cranes, boom trucks, and specialized material handling"
            " for site operations."
        )
    with col3:
        st.markdown("### 📦 Warehouse & Transfer")
        st.write(
            "Cross-docking, stacker/reach truck deployment, and site-to-site"
            " machinery transfer."
        )

# --- PAGE 2: COMPANY PROFILE ---
elif page == "Company Profile":
    header_col1, header_col2 = st.columns([3, 1])

    with header_col1:
        st.title("Company Profile")
        st.subheader("ASYCO LOGISTICS SOLUTIONS")
        st.caption("Heavy Equipment Rentals & Logistics Services")
        st.markdown("**Established in 2023**")

    with header_col2:
        st.write(" ")
        st.write(" ")
        pdf_bytes = generate_company_profile_pdf()
        st.download_button(
            label="📥 Download Profile (PDF)",
            data=pdf_bytes,
            file_name="ASYCO_Logistics_Solutions_Company_Profile.pdf",
            mime="application/pdf",
        )

    st.markdown("---")
    st.markdown("### About Our Company")
    st.write(
        "Established in 2023, ASYCO Logistics Solutions has positioned itself"
        " as a premier and trusted partner for heavy equipment rentals,"
        " specialized heavy hauling, and container drayage logistics services"
        " across the Philippines. Grounded in engineering precision, rig"
        " safety, and reliable site execution, ASYCO delivers seamless"
        " end-to-end transport solutions tailored to infrastructure"
        " development, commercial construction, energy projects, and"
        " industrial operations."
    )

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🎯 Our Mission")
        st.write(
            "To deliver dependable, engineered, and uncompromisingly safe"
            " heavy haulage and lifting solutions that drive national"
            " infrastructure development through certified equipment"
            " maintenance, rigorous lift planning, dynamic capacity checks,"
            " and continuous professional training."
        )

    with col2:
        st.markdown("### 👁️ Our Vision")
        st.write(
            "To become the Philippines' most trusted and benchmark-setting"
            " heavy equipment rental and logistics partner across Luzon,"
            " Visayas, and Mindanao by integrating technical innovation, modern"
            " fleet management, and field-tested safety protocols."
        )

    st.markdown("---")
    st.markdown("### 🚚 Comprehensive Fleet & Equipment Capabilities")
    eq_col1, eq_col2 = st.columns(2)

    with eq_col1:
        st.markdown("#### 🏗️ Boom Trucks & Mobile Cranes")
        st.markdown("""
        * **3-5t Boom Truck** — Bed Cap: *5.5T* | Lift Limit: *3.0T*
        * **7t Boom Truck** — Bed Cap: *12.5T* | Lift Limit: *7.0T*
        * **10t Boom Truck** — Bed Cap: *15.0T* | Lift Limit: *10.0T*
        * **16t Boom Truck** — Bed Cap: *20.0T* | Lift Limit: *16.0T*
        * **Mobile Cranes** — 25T, 50T, 80T, 100T, 110T, 150T, 200T, 300T
        """)

    with eq_col2:
        st.markdown("#### 🚛 Trailers & Warehouse")
        st.markdown("""
        * **40ft Flatbed Trailer** — Payload Capacity: *32.0T*
        * **Lowbed Trailer** — Payload Capacity: *40.0T*
        * **Lowboy Trailer** — Payload Capacity: *55.0T*
        * **Challenger Trailer** — Payload Capacity: *100.0T*
        * **Warehouse & Port** — MICT / ATI Drayage, Electric Reach Trucks
        """)

    st.markdown("---")
    st.markdown("### 📍 Contact Information")
    st.write(
        "**Office Address:** Queens Row West, Molino 3, Bacoor City, Cavite,"
        " Philippines"
    )
    st.write("**Email:** asycologisticssolutions@gmail.com")
    st.write("**Service Coverage:** Luzon, Visayas, and Mindanao")

# --- PAGE 3: INSTANT RATE CALCULATOR ---
elif page == "Instant Rate Calculator":
    st.title("Estimated Transport Cost Calculator")
    st.write(
        "Get a quick preliminary quote estimate for your heavy equipment and"
        " hauling requirements."
    )

    equipment_data = {
        "3-5t Boom Truck": {
            "bed_cap": 5.5,
            "lift_cap": 3.0,
            "base": 8000,
            "per_km": 200,
        },
        "7t Boom Truck": {
            "bed_cap": 12.5,
            "lift_cap": 7.0,
            "base": 17500,
            "per_km": 300,
        },
        "10t Boom Truck": {
            "bed_cap": 15.0,
            "lift_cap": 10.0,
            "base": 7000,
            "per_km": 300,
        },
        "16t Boom Truck": {
            "bed_cap": 20.0,
            "lift_cap": 16.0,
            "base": 30500,
            "per_km": 300,
        },
        "25t Mobile Crane": {
            "bed_cap": 0.0,
            "lift_cap": 25.0,
            "base": 15000,
            "per_km": 350,
        },
        "50t Mobile Crane": {
            "bed_cap": 0.0,
            "lift_cap": 50.0,
            "base": 25000,
            "per_km": 450,
        },
        "80t Mobile Crane": {
            "bed_cap": 0.0,
            "lift_cap": 80.0,
            "base": 40000,
            "per_km": 550,
        },
        "100t Mobile Crane": {
            "bed_cap": 0.0,
            "lift_cap": 100.0,
            "base": 55000,
            "per_km": 600,
        },
        "110t Mobile Crane": {
            "bed_cap": 0.0,
            "lift_cap": 110.0,
            "base": 75000,
            "per_km": 650,
        },
        "150t Mobile Crane": {
            "bed_cap": 0.0,
            "lift_cap": 150.0,
            "base": 85000,
            "per_km": 1250,
        },
        "200t Mobile Crane": {
            "bed_cap": 0.0,
            "lift_cap": 200.0,
            "base": 620000,
            "per_km": 2100,
        },
        "300t Mobile Crane": {
            "bed_cap": 0.0,
            "lift_cap": 300.0,
            "base": 680000,
            "per_km": 2900,
        },
        "Flatbed Trailer 40ft": {
            "bed_cap": 32.0,
            "lift_cap": 0.0,
            "base": 18500,
            "per_km": 200,
        },
        "Lowbed Trailer": {
            "bed_cap": 40.0,
            "lift_cap": 0.0,
            "base": 25000,
            "per_km": 200,
        },
        "Lowboy Trailer": {
            "bed_cap": 55.0,
            "lift_cap": 0.0,
            "base": 25000,
            "per_km": 220,
        },
        "Challenger Trailer": {
            "bed_cap": 100.0,
            "lift_cap": 0.0,
            "base": 40000,
            "per_km": 450,
        },
    }

    col1, col2 = st.columns(2)
    with col1:
        vehicle_type = st.selectbox(
            "Equipment / Vehicle Required", list(equipment_data.keys())
        )
        distance_km = st.number_input(
            "Estimated Distance (in KM)", min_value=1, value=25
        )

    with col2:
        cargo_weight = st.number_input(
            "Cargo Weight (Metric Tons)", min_value=0.1, value=5.0, step=0.5
        )
        need_rigging = st.checkbox("Include Rigging & Loading Crew")

    selected = equipment_data[vehicle_type]
    bed_cap = selected["bed_cap"]
    lift_cap = selected["lift_cap"]
    base_rate = selected["base"]
    per_km_rate = selected["per_km"]
    rigging_fee = 5500 if need_rigging else 0

    st.markdown("---")
    has_error = False

    if lift_cap == 0.0 and cargo_weight > bed_cap:
        st.error(
            f"⚠️ **OVERLOAD WARNING:** Cargo ({cargo_weight:.1f}T) exceeds"
            f" maximum bed capacity of **{vehicle_type}** ({bed_cap:.1f}T max)."
        )
        has_error = True
    elif bed_cap == 0.0 and cargo_weight > lift_cap:
        st.error(
            f"⚠️ **OVERLOAD WARNING:** Cargo ({cargo_weight:.1f}T) exceeds"
            " maximum rated lifting capacity of"
            f" **{vehicle_type}** ({lift_cap:.1f}T max)."
        )
        has_error = True
    elif bed_cap > 0.0 and lift_cap > 0.0:
        if cargo_weight > bed_cap:
            st.error(
                f"⚠️ **BED OVERLOAD:** Cargo ({cargo_weight:.1f}T) exceeds bed"
                f" transport limit of **{vehicle_type}** ({bed_cap:.1f}T max)."
            )
            has_error = True
        elif cargo_weight > lift_cap:
            st.warning(
                f"⚠️ **SELF-LOADING LIMIT EXCEEDED:** Cargo ({cargo_weight:.1f}T)"
                f" fits on truck bed ({bed_cap:.1f}T max), but exceeds boom's"
                f" direct lifting limit ({lift_cap:.1f}T max). An auxiliary"
                " mobile crane is required."
            )

    if not has_error:
        total_estimate = base_rate + (distance_km * per_km_rate) + rigging_fee
        st.success("✅ **SAFE PARAMETERS:** Equipment complies with limits.")
        st.markdown(
            f"### **Estimated Total Cost: `PHP {total_estimate:,.2f}`**"
        )
        st.write(f"**Selected Equipment:** {vehicle_type}")
        st.write(f"**Base Mobilization Rate:** PHP {base_rate:,.2f}")
        st.write(
            f"**Distance Charge ({distance_km} KM):** PHP"
            f" {distance_km * per_km_rate:,.2f}"
        )
        if need_rigging:
            st.write(f"**Rigging Crew & Spotter Fee:** PHP {rigging_fee:,.2f}")

# --- PAGE 4: SAFETY LIFT CHECKER ---
elif page == "Safety Lift Checker":
    st.title("Boom Truck & Crane Capacity Safety Check")
    st.write(
        "Evaluate lifting capacity utilization and safety margins based on radius"
        " distance prior to deployment."
    )

    def check_crane_safety_factor(crane_capacity, total_load, dynamic_factor):
        effective_load = total_load * dynamic_factor
        if effective_load <= 0:
            return 0.0
        return crane_capacity / effective_load

    col1, col2 = st.columns(2)
    with col1:
        load_weight = st.number_input(
            "Payload Weight (Metric Tons)", min_value=0.1, value=12.0, step=0.5
        )
        rigging_hook_weight = st.number_input(
            "Hook Block & Rigging Weight (Metric Tons)",
            min_value=0.0,
            value=0.5,
            step=0.1,
        )
        total_gross_load = load_weight + rigging_hook_weight

    with col2:
        radius_m = st.number_input(
            "Operating Radius (Meters)", min_value=1.0, value=6.0, step=0.5
        )
        crane_capacity = st.number_input(
            f"Rated Capacity at {radius_m}m Radius (Metric Tons)",
            min_value=0.1,
            value=25.0,
            step=0.5,
        )
        dynamic_factor = st.slider(
            "Dynamic Factor (Motion/Wind Multiplier)",
            min_value=1.10,
            max_value=1.25,
            value=1.15,
            step=0.01,
        )

    st.markdown("---")
    chart_verified = st.checkbox(
        "I confirm that the entered rated capacity is verified directly from the"
        " official OEM load chart for this radius and outrigger setup."
    )

    if chart_verified:
        fos = check_crane_safety_factor(
            crane_capacity, total_gross_load, dynamic_factor
        )
        effective_load = total_gross_load * dynamic_factor
        utilization = (
            (effective_load / crane_capacity) * 100 if crane_capacity > 0 else 0
        )

        st.markdown(f"### **Computed Factor of Safety: `{fos:.2f}`**")
        st.write(f"**Operating Radius:** {radius_m:.1f} Meters")
        st.write(
            f"**Gross Load (Payload + Rigging):** {total_gross_load:.2f} Tons"
        )
        st.write(
            f"**Dynamic Effective Load ({dynamic_factor:.2f}x):**"
            f" {effective_load:.2f} Tons"
        )
        st.write(f"**Capacity Utilization:** {utilization:.1f}%")

        if fos >= 1.0:
            st.success(
                f"✅ **SAFE OPERATION:** Lift at {radius_m}m radius is within safe"
                " parameters."
            )
        else:
            st.error(
                f"🚨 **WARNING: UNSAFE CONDITION!** Dynamic load exceeds rated"
                f" capacity at {radius_m}m radius."
            )

# --- PAGE 5: BOOK A TRANSPORT ---
elif page == "Book a Transport":
    st.title("Request a Transport Quote")
    st.write(
        "Fill out the details below and our dispatch team will receive your"
        " request directly."
    )

    # Native Streamlit Form with FormSubmit integration
    contact_html = """
    <style>
        .form-container {
            background-color: #1E293B;
            padding: 25px;
            border-radius: 10px;
        }
        .form-group { margin-bottom: 15px; }
        label { color: white; font-size: 14px; display: block; margin-bottom: 5px; }
        input, textarea {
            width: 100%; padding: 10px; border-radius: 5px;
            border: 1px solid #334155; background: #0F172A; color: white;
            box-sizing: border-box;
        }
        button {
            background-color: #112D4E; color: white; font-weight: bold;
            border: none; padding: 12px; border-radius: 6px; cursor: pointer; width: 100%;
        }
        button:hover { background-color: #3F72AF; }
    </style>
    <div class="form-container">
        <form action="https://formsubmit.co/asycologisticssolutions@gmail.com" method="POST" target="_blank">
            <input type="hidden" name="_subject" value="New ASYCO Transport Quote Request">
            <input type="hidden" name="_captcha" value="false">
            <div class="form-group">
                <label>Contact Person / Company Name</label>
                <input type="text" name="name" required>
            </div>
            <div class="form-group">
                <label>Email Address</label>
                <input type="email" name="email" required>
            </div>
            <div class="form-group">
                <label>Phone / Contact Number</label>
                <input type="text" name="phone" required>
            </div>
            <div class="form-group">
                <label>Target Date of Transport</label>
                <input type="date" name="date" required>
            </div>
            <div class="form-group">
                <label>Pickup Location</label>
                <input type="text" name="pickup" required>
            </div>
            <div class="form-group">
                <label>Destination / Dropoff Location</label>
                <input type="text" name="dropoff" required>
            </div>
            <div class="form-group">
                <label>Cargo Description & Dimensions</label>
                <textarea name="cargo" rows="4" required></textarea>
            </div>
            <button type="submit">Submit Request</button>
        </form>
    </div>
    """
    st.components.v1.html(contact_html, height=680, scrolling=True)
