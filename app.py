import streamlit as st
import base64

# Function to encode image file for CSS background
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Page Configuration
st.set_page_config(
    page_title="ASYCO Logistics Services",
    page_icon="🚛",
    layout="wide"
)

# Apply Background
try:
    bin_str = get_base64_of_bin_file('Background.jpg')
    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bin_str}");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Save 'Background.jpg' on your Desktop to display the background image.")

# Custom Card & Navy/White Text Styling
st.markdown("""
    <style>
    /* Translucent White Card Overlay for Content Readability */
    .block-container {
        background-color: rgba(255, 255, 255, 0.92);
        padding: 2rem !important;
        border-radius: 12px;
        margin-top: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Main Content Area: Navy Blue Text for Paragraphs & Labels */
    .block-container p, .block-container span, .block-container label, 
    .block-container div, .block-container h1, .block-container h2, 
    .block-container h3, .block-container h4, .block-container h5, .block-container h6 {
        color: #112D4E !important;
        font-weight: 500;
    }

    /* Force Typed Input Text, Text Area Text, and Form Values to White */
    input, textarea, .stTextInput input, .stTextArea textarea, .stNumberInput input {
        color: #FFFFFF !important;
        background-color: #1E293B !important;
    }

    /* Sidebar: Force ALL Text & Radio Labels to White */
    [data-testid="stSidebar"] *, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] div, 
    [data-testid="stSidebar"] span {
        color: #FFFFFF !important;
        font-weight: 500;
    }

    h1, h2, h3 {
        font-weight: 700 !important;
    }
    
    /* Custom Button Styling - Bright White Text */
    .stButton>button, div[data-testid="stFormSubmitButton"]>button {
        background-color: #112D4E !important;
        color: #FFFFFF !important;
        border-radius: 6px;
        border: none;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover, div[data-testid="stFormSubmitButton"]>button:hover {
        background-color: #3F72AF !important;
        color: #FFFFFF !important;
    }
    
    /* Target internal button text elements explicitly */
    .stButton>button *, div[data-testid="stFormSubmitButton"]>button * {
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with Logo and Navigation
try:
    st.sidebar.image("logo.png", use_container_width=True)
except Exception:
    st.sidebar.warning("Place 'logo.png' on your Desktop to display your logo here.")

st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["Home & Services", "Instant Rate Calculator", "Safety Lift Checker", "Book a Transport"])

# --- PAGE 1: HOME & SERVICES ---
if page == "Home & Services":
    st.title("ASYCO LOGISTICS SOLUTIONS")
    st.subheader("Heavy Equipment Rentals & Logistics Services")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Hauling & Fleet")
        st.write("10-wheeler boom trucks, tractor head trailers, and flatbed transport for heavy cargo.")
    with col2:
        st.markdown("### Crane & Lifting")
        st.write("Mobile cranes, boom trucks, and specialized material handling for site operations.")
    with col3:
        st.markdown("### Warehouse & Transfer")
        st.write("Cross-docking, stacker/reach truck deployment, and site-to-site machinery transfer.")

# --- PAGE 2: INSTANT RATE CALCULATOR ---
elif page == "Instant Rate Calculator":
    st.title("Estimated Transport Cost Calculator")
    st.write("Get a quick quote estimate for your heavy equipment and hauling requirements.")
    
    # Equipment Database with Bed Payload, Lifting Capacity, Base Rates, and Per-KM Rates
    equipment_data = {
        "3-5t Boom Truck": {"bed_cap": 5.5, "lift_cap": 3.0, "base": 8000, "per_km": 200},
        "7t Boom Truck": {"bed_cap": 12.5, "lift_cap": 7.0, "base": 17500, "per_km": 300},
        "10t Boom Truck": {"bed_cap": 15.0, "lift_cap": 10.0, "base": 7000, "per_km": 300},
        "16t Boom Truck": {"bed_cap": 20.0, "lift_cap": 16.0, "base": 30500, "per_km": 300},
        "25t Mobile Crane": {"bed_cap": 0.0, "lift_cap": 25.0, "base": 15000, "per_km": 350},
        "50t Mobile Crane": {"bed_cap": 0.0, "lift_cap": 50.0, "base": 25000, "per_km": 450},
        "80t Mobile Crane": {"bed_cap": 0.0, "lift_cap": 80.0, "base": 40000, "per_km": 550},
        "100t Mobile Crane": {"bed_cap": 0.0, "lift_cap": 100.0, "base": 55000, "per_km": 600},
        "110t Mobile Crane": {"bed_cap": 0.0, "lift_cap": 110.0, "base": 75000, "per_km": 650},
        "150t Mobile Crane": {"bed_cap": 0.0, "lift_cap": 150.0, "base": 85000, "per_km": 1250},
        "200t Mobile Crane": {"bed_cap": 0.0, "lift_cap": 200.0, "base": 620000, "per_km": 2100},
        "300t Mobile Crane": {"bed_cap": 0.0, "lift_cap": 300.0, "base": 680000, "per_km": 2900},
        "Flatbed Trailer 40ft": {"bed_cap": 32.0, "lift_cap": 0.0, "base": 18500, "per_km": 200},
        "Lowbed Trailer": {"bed_cap": 40.0, "lift_cap": 0.0, "base": 25000, "per_km": 200},
        "Lowboy Trailer": {"bed_cap": 55.0, "lift_cap": 0.0, "base": 25000, "per_km": 220},
        "Challenger Trailer": {"bed_cap": 100.0, "lift_cap": 0.0, "base": 40000, "per_km": 450}
    }

    col1, col2 = st.columns(2)
    with col1:
        vehicle_type = st.selectbox("Equipment / Vehicle Required", list(equipment_data.keys()))
        distance_km = st.number_input("Estimated Distance (in KM)", min_value=1, value=25)
    
    with col2:
        cargo_weight = st.number_input("Cargo Weight (Tons)", min_value=0.1, value=5.0, step=0.5)
        need_rigging = st.checkbox("Include Rigging & Loading Crew")

    # Get selected equipment specs
    selected = equipment_data[vehicle_type]
    bed_cap = selected["bed_cap"]
    lift_cap = selected["lift_cap"]
    base_rate = selected["base"]
    per_km_rate = selected["per_km"]
    rigging_fee = 5500 if need_rigging else 0

    st.markdown("---")

    # Validation Checks
    if lift_cap == 0.0 and cargo_weight > bed_cap:
        st.error(f"⚠️ **OVERLOAD WARNING:** Cargo ({cargo_weight:.1f}T) exceeds the trailer bed capacity of **{vehicle_type}** ({bed_cap:.1f}T max).")
    elif bed_cap == 0.0 and cargo_weight > lift_cap:
        st.error(f"⚠️ **OVERLOAD WARNING:** Cargo ({cargo_weight:.1f}T) exceeds the maximum rated lifting capacity of **{vehicle_type}** ({lift_cap:.1f}T max).")
    elif bed_cap > 0.0 and lift_cap > 0.0 and cargo_weight > bed_cap:
        st.error(f"⚠️ **BED OVERLOAD WARNING:** Cargo ({cargo_weight:.1f}T) exceeds the deck/bed transport limit of **{vehicle_type}** ({bed_cap:.1f}T bed max), even though its boom can lift up to {lift_cap:.1f}T.")
    else:
        total_estimate = base_rate + (distance_km * per_km_rate) + rigging_fee
        
        st.success("✅ **SAFE PARAMETERS:** Operation is within equipment capacity limits.")
        st.markdown(f"### **Estimated Total Cost: `PHP {total_estimate:,.2f}`**")
        st.write(f"**Selected Equipment:** {vehicle_type}")
        if bed_cap > 0:
            st.write(f"**Max Bed Capacity:** {bed_cap:.1f} Tons")
        if lift_cap > 0:
            st.write(f"**Max Lifting Capacity:** {lift_cap:.1f} Tons")
        st.write(f"**Base Mobilization Rate:** PHP {base_rate:,.2f}")
        st.write(f"**Distance Charge ({distance_km} KM):** PHP {distance_km * per_km_rate:,.2f}")
        if need_rigging:
            st.write(f"**Rigging Crew & Spotter Fee:** PHP {rigging_fee:,.2f}")
            
        st.caption("*Final quotation subject to site survey, load radius, highway permits, and rigging plan.")

# --- PAGE 3: SAFETY LIFT CHECKER ---
elif page == "Safety Lift Checker":
    st.title("Boom Truck & Crane Capacity Safety Check")
    st.write("Evaluate lifting capacity utilization and dynamic safety margins based on radius distance prior to site deployment.")
    
    # Custom Crane Safety Function with Radius Consideration
    def check_crane_safety_factor(crane_capacity, total_load, dynamic_factor=1.15):
        """Calculates the factor of safety for a crane lift."""
        effective_load = total_load * dynamic_factor
        if effective_load == 0:
            return 0
        safety_factor = crane_capacity / effective_load
        return safety_factor

    col1, col2 = st.columns(2)
    with col1:
        load_weight = st.number_input("Payload Weight (Tons/KG)", min_value=0.1, value=12.0, step=0.5)
        rigging_hook_weight = st.number_input("Hook Block & Rigging Weight (Tons/KG)", min_value=0.0, value=0.5, step=0.1)
        total_gross_load = load_weight + rigging_hook_weight
        
    with col2:
        radius_m = st.number_input("Operating Radius (Meters)", min_value=1.0, value=6.0, step=0.5)
        crane_capacity = st.number_input(f"Rated Capacity at {radius_m}m Radius (Tons/KG)", min_value=0.1, value=25.0, step=0.5)
        dynamic_factor = st.slider("Dynamic Factor (Motion/Wind Multiplier)", min_value=1.10, max_value=1.25, value=1.15, step=0.01)

    # Calculate FoS using your function
    fos = check_crane_safety_factor(crane_capacity, total_gross_load, dynamic_factor)
    effective_load = total_gross_load * dynamic_factor
    utilization = (effective_load / crane_capacity) * 100 if crane_capacity > 0 else 0

    st.markdown("---")
    st.markdown(f"### **Computed Factor of Safety: `{fos:.2f}`**")
    st.write(f"**Operating Radius:** {radius_m:.1f} Meters")
    st.write(f"**Gross Load (Payload + Rigging):** {total_gross_load:.2f}")
    st.write(f"**Dynamic Effective Load ({dynamic_factor}x):** {effective_load:.2f}")
    st.write(f"**Capacity Utilization:** {utilization:.1f}%")

    if fos >= 1.0:
        st.success(f"SAFE OPERATION: Lift at {radius_m}m radius is within safe parameters.")
    else:
        st.error(f"WARNING: Unsafe condition! Dynamic effective load exceeds crane rated capacity at {radius_m}m radius.")

# --- PAGE 4: BOOK A TRANSPORT ---
elif page == "Book a Transport":
    st.title("Request a Transport Quote")
    st.write("Fill out the details below and our dispatch team will receive your request directly via email.")

    # HTML Form configured with FormSubmit API
    contact_form_html = """
    <form action="https://formsubmit.co/asycologisticssolutions@gmail.com" method="POST" style="background-color: #1E293B; padding: 20px; border-radius: 10px;">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_subject" value="New ASYCO Transport Quote Request">
        
        <div style="display: flex; gap: 15px; margin-bottom: 15px;">
            <div style="flex: 1;">
                <label style="color: white; font-size: 14px;">Contact Person / Company Name</label><br>
                <input type="text" name="name" required style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc; background: #0F172A; color: white;">
            </div>
            <div style="flex: 1;">
                <label style="color: white; font-size: 14px;">Email Address</label><br>
                <input type="email" name="email" required style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc; background: #0F172A; color: white;">
            </div>
        </div>

        <div style="display: flex; gap: 15px; margin-bottom: 15px;">
            <div style="flex: 1;">
                <label style="color: white; font-size: 14px;">Phone / Contact Number</label><br>
                <input type="text" name="phone" required style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc; background: #0F172A; color: white;">
            </div>
            <div style="flex: 1;">
                <label style="color: white; font-size: 14px;">Target Date of Transport</label><br>
                <input type="date" name="date" required style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc; background: #0F172A; color: white;">
            </div>
        </div>

        <div style="display: flex; gap: 15px; margin-bottom: 15px;">
            <div style="flex: 1;">
                <label style="color: white; font-size: 14px;">Pickup Location</label><br>
                <input type="text" name="pickup" required style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc; background: #0F172A; color: white;">
            </div>
            <div style="flex: 1;">
                <label style="color: white; font-size: 14px;">Destination / Dropoff Location</label><br>
                <input type="text" name="dropoff" required style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc; background: #0F172A; color: white;">
            </div>
        </div>

        <div style="margin-bottom: 15px;">
            <label style="color: white; font-size: 14px;">Cargo Description & Dimensions</label><br>
            <textarea name="cargo" rows="4" required style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc; background: #0F172A; color: white;"></textarea>
        </div>

        <button type="submit" style="background-color: #112D4E; color: white; font-weight: bold; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; width: 100%;">
            Submit Request
        </button>
    </form>
    """
    
    st.components.v1.html(contact_form_html, height=520)