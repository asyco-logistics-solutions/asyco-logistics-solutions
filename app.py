import streamlit as st
import base64
import os

# Page Configuration
st.set_page_config(
    page_title="ASYCO Logistics Services",
    page_icon="🚛",
    layout="wide"
)

# Helper function to encode local files safely
def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# Apply Background Styling Dynamically
bg_base64 = get_base64_of_bin_file('Background.jpg')
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
        unsafe_allow_html=True
    )

# Custom UI CSS Styling
st.markdown("""
    <style>
    .block-container {
        background-color: rgba(255, 255, 255, 0.94);
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
    </style>
""", unsafe_allow_html=True)

# Sidebar Branding
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", use_container_width=True)

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

    selected = equipment_data[vehicle_type]
    bed_cap = selected["bed_cap"]
    lift_cap = selected["lift_cap"]
    base_rate = selected["base"]
    per_km_rate = selected["per_km"]
    rigging_fee = 5500 if need_rigging else 0

    st.markdown("---")

    # FIXED: Comprehensive Capacity & Overload Checks
    has_error = False
    
    # Check 1: Pure Trailers (No Boom/Lift)
    if lift_cap == 0.0 and cargo_weight > bed_cap:
        st.error(f"⚠️ **OVERLOAD WARNING:** Cargo ({cargo_weight:.1f}T) exceeds the maximum bed capacity of **{vehicle_type}** ({bed_cap:.1f}T max).")
        has_error = True
    
    # Check 2: Pure Mobile Cranes (No Cargo Bed)
    elif bed_cap == 0.0 and cargo_weight > lift_cap:
        st.error(f"⚠️ **OVERLOAD WARNING:** Cargo ({cargo_weight:.1f}T) exceeds the maximum rated lifting capacity of **{vehicle_type}** ({lift_cap:.1f}T max).")
        has_error = True
        
    # Check 3: Boom Trucks (Bed + Boom Dynamic Validation)
    elif bed_cap > 0.0 and lift_cap > 0.0:
        if cargo_weight > bed_cap:
            st.error(f"⚠️ **BED OVERLOAD:** Cargo ({cargo_weight:.1f}T) exceeds the bed transport limit of **{vehicle_type}** ({bed_cap:.1f}T max).")
            has_error = True
        elif cargo_weight > lift_cap:
            st.warning(f"⚠️ **SELF-LOADING LIMIT EXCEEDED:** Cargo ({cargo_weight:.1f}T) fits on the truck bed ({bed_cap:.1f}T max), but exceeds the boom's direct lifting limit ({lift_cap:.1f}T max). An auxiliary mobile crane will be required for loading/unloading.")

    # Calculate and display rate if no fatal errors exist
    if not has_error:
        total_estimate = base_rate + (distance_km * per_km_rate) + rigging_fee
        st.success("✅ **SAFE PARAMETERS:** Equipment choice complies with hauling weight limits.")
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
            
        st.caption("*Final quotation subject to site survey, working radius, highway permits, and rigging plan.")

# --- PAGE 3: SAFETY LIFT CHECKER ---
elif page == "Safety Lift Checker":
    st.title("Boom Truck & Crane Capacity Safety Check")
    st.write("Evaluate lifting capacity utilization and dynamic safety margins based on radius distance prior to site deployment.")
    
    def check_crane_safety_factor(crane_capacity, total_load, dynamic_factor=1.15):
        effective_load = total_load * dynamic_factor
        if effective_load == 0:
            return 0
        return crane_capacity / effective_load

    col1, col2 = st.columns(2)
    with col1:
        load_weight = st.number_input("Payload Weight (Tons/KG)", min_value=0.1, value=12.0, step=0.5)
        rigging_hook_weight = st.number_input("Hook Block & Rigging Weight (Tons/KG)", min_value=0.0, value=0.5, step=0.1)
        total_gross_load = load_weight + rigging_hook_weight
        
    with col2:
        radius_m = st.number_input("Operating Radius (Meters)", min_value=1.0, value=6.0, step=0.5)
        crane_capacity = st.number_input(f"Rated Capacity at {radius_m}m Radius (Tons/KG)", min_value=0.1, value=25.0, step=0.5)
        dynamic_factor = st.slider("Dynamic Factor (Motion/Wind Multiplier)", min_value=1.10, max_value=1.25, value=1.15, step=0.01)

    st.markdown("---")
    
    # FIXED: Forced Load Chart Verification Checkbox
    chart_verified = st.checkbox("I confirm that the entered rated capacity is verified directly from the official manufacturer OEM load chart for this radius and outrigger setup.")
    
    if chart_verified:
        fos = check_crane_safety_factor(crane_capacity, total_gross_load, dynamic_factor)
        effective_load = total_gross_load * dynamic_factor
        utilization = (effective_load / crane_capacity) * 100 if crane_capacity > 0 else 0

        st.markdown(f"### **Computed Factor of Safety: `{fos:.2f}`**")
        st.write(f"**Operating Radius:** {radius_m:.1f} Meters")
        st.write(f"**Gross Load (Payload + Rigging):** {total_gross_load:.2f}")
        st.write(f"**Dynamic Effective Load ({dynamic_factor}x):** {effective_load:.2f}")
        st.write(f"**Capacity Utilization:** {utilization:.1f}%")

        if fos >= 1.0:
            st.success(f"SAFE OPERATION: Lift at {radius_m}m radius is within safe parameters.")
        else:
            st.error(f"WARNING: Unsafe condition! Dynamic effective load exceeds crane rated capacity at {radius_m}m radius.")
    else:
        st.info("💡 Please verify and check the box above to generate the safety factor calculation.")

# --- PAGE 4: BOOK A TRANSPORT ---
elif page == "Book a Transport":
    st.title("Request a Transport Quote")
    st.write("Fill out the details below and our dispatch team will receive your request directly via email.")

    # FIXED: Re-enabled FormSubmit captcha to prevent email spam bots
    contact_form_html = """
    <form action="https://formsubmit.co/asycologisticssolutions@gmail.com" method="POST" style="background-color: #1E293B; padding: 20px; border-radius: 10px;">
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
    
    st.components.v1.html(contact_form_html, height=560)
