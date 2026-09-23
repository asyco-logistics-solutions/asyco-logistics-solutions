import base64
import os
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="ASYCO Logistics Services", page_icon="🚛", layout="wide"
)


# Helper function to encode local files safely
def get_base64_of_bin_file(bin_file):
  if os.path.exists(bin_file):
    with open(bin_file, "rb") as f:
      data = f.read()
    return base64.b64encode(data).decode()
  return None


# Apply Background Styling Dynamically
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

# Custom UI CSS Styling
st.markdown(
    """
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

    /* Force Native Streamlit Columns to Stack Vertically on Mobile */
    @media (max-width: 768px) {
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }
        .block-container {
            padding: 1rem !important;
        }
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Branding
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
    st.markdown("### Hauling & Fleet")
    st.write(
        "10-wheeler boom trucks, tractor head trailers, and flatbed transport"
        " for heavy cargo."
    )
  with col2:
    st.markdown("### Crane & Lifting")
    st.write(
        "Mobile cranes, boom trucks, and specialized material handling for"
        " site operations."
    )
  with col3:
    st.markdown("### Warehouse & Transfer")
    st.write(
        "Cross-docking, stacker/reach truck deployment, and site-to-site"
        " machinery transfer."
    )

# --- PAGE 2: COMPANY PROFILE ---
elif page == "Company Profile":
  st.title("Company Profile")
  st.subheader("ASYCO LOGISTICS SOLUTIONS")
  st.caption("Heavy Equipment Rentals & Logistics Services")
  st.markdown("**Established in 2023**")
  st.markdown("---")

  st.markdown("### Tungkol sa Aming Kompanya")
  st.write(
      "Itinatag noong 2023, ang ASYCO Logistics Solutions ay isang mabilis na"
      " umuunlad at pinagkakatiwalaang kompanya sa Pilipinas na nagbibigay ng"
      " heavy equipment rentals, specialized heavy hauling, at drayage"
      " logistics services. Sa pamamagitan ng aming expertise sa engineering"
      " precision, rig safety, at maaasahang site execution, naghahatid ang"
      " ASYCO ng kumpleto at laging ligtas na transport solutions para sa mga"
      " proyektong pang-inprastraktura, komersyal na konstruksyon, enerhiya, at"
      " industriyal."
  )

  st.markdown("---")
  col1, col2 = st.columns(2)
  with col1:
    st.markdown("### 🎯 Aming Layunin (Mission)")
    st.write(
        "Ang aming layunin ay magbigay ng maasahan, engineered, at walang"
        " kompromisong ligtas na heavy haulage at lifting solutions na"
        " nagtataguyod sa pag-unlad ng pambansang inprastraktura. Nakatuon kami"
        " sa pagpapanatili ng pinakamataas na pamantayan ng operational safety"
        " sa pamamagitan ng regular na sertipikadong maintenance ng aming mga"
        " kagamitan, maingat na lift planning, dynamic capacity checks, at"
        " tuluy-tuloy na propesyonal na pagsasanay ng aming mga rigger at crane"
        " operators. Sa pagsasama ng makabagong fleet at mabilis na pagtugon sa"
        " pangangailangan ng kliyente, sinisiguro naming natutupad ang bawat"
        " proyekto sa takdang oras at napoprotektahan ang mga mahahalagang"
        " kagamitan ng aming mga kasosyo."
    )

  with col2:
    st.markdown("### 👁️ Aming Pananaw (Vision)")
    st.write(
        "Ang aming pananaw ay maging pinakapinagkakatiwalaan at nangungunang"
        " katuwang sa heavy equipment rental at logistics sa buong Luzon,"
        " Visayas, at Mindanao. Layunin naming pamunuan ang industriya sa"
        " pamamagitan ng paggamit ng makabagong teknolohiya, modernong fleet"
        " management, at subok na mga pamantayan sa kaligtasan sa bawat site"
        " operation. Sa ganitong paraan, nakakatulong kami sa pag-unlad ng"
        " bansa, renewable energy, at komersyal na konstruksyon habang"
        " nagtataguyod ng matatag at pangmatagalang ugnayan sa mga namumuno"
        " sa sektor ng engineering at konstruksyon."
    )

  st.markdown("---")
  st.markdown("### 🚚 Kumpletong Talaan ng Aming Equipment at Fleet")
  st.write(
      "Narito ang kumpletong listahan ng aming mga heavy machinery, lifting"
      " equipment, at specialized transport trailers na handang iparenta at"
      " ideploy sa inyong mga proyekto:"
  )

  eq_col1, eq_col2 = st.columns(2)

  with eq_col1:
    st.markdown("#### 🏗️ Boom Trucks & Mobile Cranes")
    st.markdown("""
        * **3-5t Boom Truck** — Bed Capacity: *5.5T* | Direct Lift Limit: *3.0T*
        * **7t Boom Truck** — Bed Capacity: *12.5T* | Direct Lift Limit: *7.0T*
        * **10t Boom Truck** — Bed Capacity: *15.0T* | Direct Lift Limit: *10.0T*
        * **16t Boom Truck** — Bed Capacity: *20.0T* | Direct Lift Limit: *16.0T*
        * **25t Mobile Crane** — Rated Lifting Capacity: *25.0T*
        * **50t Mobile Crane** — Rated Lifting Capacity: *50.0T*
        * **80t Mobile Crane** — Rated Lifting Capacity: *80.0T*
        * **100t Mobile Crane** — Rated Lifting Capacity: *100.0T*
        * **110t Mobile Crane** — Rated Lifting Capacity: *110.0T*
        * **150t Mobile Crane** — Rated Lifting Capacity: *150.0T*
        * **200t Mobile Crane** — Rated Lifting Capacity: *200.0T*
        * **300t Mobile Crane** — Rated Lifting Capacity: *300.0T*
        """)

  with eq_col2:
    st.markdown("#### 🚛 Trailers & Material Handling")
    st.markdown("""
        * **Flatbed Trailer (40ft)** — Bed Payload Capacity: *32.0T*
        * **Lowbed Trailer** — Bed Payload Capacity: *40.0T*
        * **Lowboy Trailer** — Bed Payload Capacity: *55.0T*
        * **Challenger Trailer** — Bed Payload Capacity: *100.0T*
        * **Container Drayage Support** — Direct MICT / ATI South Harbor Hauling
        * **Warehouse Operations** — Electric Walkie Stackers & Reach Trucks
        * **Specialized Rigging Crew** — Certified Spotters, Riggers & Signalmen
        """)

  st.markdown("---")
  st.markdown("### 📍 Lokasyon at Impormasyon sa Pagkontak")
  st.write(
      "**Opisina:** Queens Row West, Molino 3, Bacoor City, Cavite, Philippines"
  )
  st.write("**Email:** asycologisticssolutions@gmail.com")
  st.write("**Sakop na Serbisyo:** Luzon, Visayas, at Mindanao")

# --- PAGE 3: INSTANT RATE CALCULATOR ---
elif page == "Instant Rate Calculator":
  st.title("Estimated Transport Cost Calculator")
  st.write(
      "Kumuha ng paunang tantiya ng halaga para sa inyong heavy equipment at"
      " hauling requirement."
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
        "Cargo Weight (Tons)", min_value=0.1, value=5.0, step=0.5
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
        f"⚠️ **OVERLOAD WARNING:** Cargo ({cargo_weight:.1f}T) exceeds the"
        f" maximum bed capacity of **{vehicle_type}** ({bed_cap:.1f}T max)."
    )
    has_error = True

  elif bed_cap == 0.0 and cargo_weight > lift_cap:
    st.error(
        f"⚠️ **OVERLOAD WARNING:** Cargo ({cargo_weight:.1f}T) exceeds the"
        " maximum rated lifting capacity of **{vehicle_type}**"
        f" ({lift_cap:.1f}T max)."
    )
    has_error = True

  elif bed_cap > 0.0 and lift_cap > 0.0:
    if cargo_weight > bed_cap:
      st.error(
          f"⚠️ **BED OVERLOAD:** Cargo ({cargo_weight:.1f}T) exceeds the bed"
          f" transport limit of **{vehicle_type}** ({bed_cap:.1f}T max)."
      )
      has_error = True
    elif cargo_weight > lift_cap:
      st.warning(
          f"⚠️ **SELF-LOADING LIMIT EXCEEDED:** Cargo ({cargo_weight:.1f}T)"
          f" fits on the truck bed ({bed_cap:.1f}T max), but exceeds the"
          f" boom's direct lifting limit ({lift_cap:.1f}T max). An auxiliary"
          " mobile crane will be required for loading/unloading."
      )

  if not has_error:
    total_estimate = base_rate + (distance_km * per_km_rate) + rigging_fee
    st.success(
        "✅ **SAFE PARAMETERS:** Equipment choice complies with hauling weight"
        " limits."
    )
    st.markdown(f"### **Estimated Total Cost: `PHP {total_estimate:,.2f}`**")
    st.write(f"**Selected Equipment:** {vehicle_type}")
    if bed_cap > 0:
      st.write(f"**Max Bed Capacity:** {bed_cap:.1f} Tons")
    if lift_cap > 0:
      st.write(f"**Max Lifting Capacity:** {lift_cap:.1f} Tons")
    st.write(f"**Base Mobilization Rate:** PHP {base_rate:,.2f}")
    st.write(
        f"**Distance Charge ({distance_km} KM):** PHP"
        f" {distance_km * per_km_rate:,.2f}"
    )
    if need_rigging:
      st.write(f"**Rigging Crew & Spotter Fee:** PHP {rigging_fee:,.2f}")

    st.caption(
        "*Final quotation subject to site survey, working radius, highway"
        " permits, and rigging plan."
    )

# --- PAGE 4: SAFETY LIFT CHECKER ---
elif page == "Safety Lift Checker":
  st.title("Boom Truck & Crane Capacity Safety Check")
  st.write(
      "Evaluate lifting capacity utilization and dynamic safety margins based"
      " on radius distance prior to site deployment."
  )

  def check_crane_safety_factor(crane_capacity, total_load, dynamic_factor=1.15):
    effective_load = total_load * dynamic_factor
    if effective_load == 0:
      return 0
    return crane_capacity / effective_load

  col1, col2 = st.columns(2)
  with col1:
    load_weight = st.number_input(
        "Payload Weight (Tons/KG)", min_value=0.1, value=12.0, step=0.5
    )
    rigging_hook_weight = st.number_input(
        "Hook Block & Rigging Weight (Tons/KG)",
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
        f"Rated Capacity at {radius_m}m Radius (Tons/KG)",
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
      " official manufacturer OEM load chart for this radius and outrigger"
      " setup."
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
    st.write(f"**Gross Load (Payload + Rigging):** {total_gross_load:.2f}")
    st.write(
        f"**Dynamic Effective Load ({dynamic_factor}x):** {effective_load:.2f}"
    )
    st.write(f"**Capacity Utilization:** {utilization:.1f}%")

    if fos >= 1.0:
      st.success(
          f"SAFE OPERATION: Lift at {radius_m}m radius is within safe"
          " parameters."
      )
    else:
      st.error(
          "WARNING: Unsafe condition! Dynamic effective load exceeds crane"
          f" rated capacity at {radius_m}m radius."
      )
  else:
    st.info(
        "💡 Please verify and check the box above to generate the safety factor"
        " calculation."
    )

# --- PAGE 5: BOOK A TRANSPORT ---
elif page == "Book a Transport":
  st.title("Request a Transport Quote")
  st.write(
      "Fill out the details below and our dispatch team will receive your"
      " request directly via email."
  )

  contact_form_html = """
    <style>
        .form-container {
            background-color: #1E293B;
            padding: 20px;
            border-radius: 10px;
            box-sizing: border-box;
            width: 100%;
        }
        .form-row {
            display: flex;
            gap: 15px;
            margin-bottom: 15px;
            flex-wrap: wrap;
        }
        .form-group {
            flex: 1;
            min-width: 250px;
        }
        label {
            color: white;
            font-size: 14px;
            display: inline-block;
            margin-bottom: 5px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #334155;
            background: #0F172A;
            color: white;
            box-sizing: border-box;
            font-size: 14px;
        }
        button {
            background-color: #112D4E;
            color: white;
            font-weight: bold;
            border: none;
            padding: 12px 20px;
            border-radius: 6px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
        }
        button:hover {
            background-color: #3F72AF;
        }
        @media (max-width: 600px) {
            .form-group {
                flex: 1 1 100%;
            }
            .form-container {
                padding: 15px;
            }
        }
    </style>

    <div class="form-container">
        <form action="https://formsubmit.co/asycologisticssolutions@gmail.com" method="POST">
            <input type="hidden" name="_subject" value="New ASYCO Transport Quote Request">
            
            <div class="form-row">
                <div class="form-group">
                    <label>Contact Person / Company Name</label>
                    <input type="text" name="name" required>
                </div>
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" name="email" required>
                </div>
            </div>

            <div class="form-row">
                <div class="form-group">
                    <label>Phone / Contact Number</label>
                    <input type="text" name="phone" required>
                </div>
                <div class="form-group">
                    <label>Target Date of Transport</label>
                    <input type="date" name="date" required>
                </div>
            </div>

            <div class="form-row">
                <div class="form-group">
                    <label>Pickup Location</label>
                    <input type="text" name="pickup" required>
                </div>
                <div class="form-group">
                    <label>Destination / Dropoff Location</label>
                    <input type="text" name="dropoff" required>
                </div>
            </div>

            <div class="form-group" style="margin-bottom: 15px;">
                <label>Cargo Description & Dimensions</label>
                <textarea name="cargo" rows="4" required></textarea>
            </div>

            <button type="submit">Submit Request</button>
        </form>
    </div>
    """

  st.components.v1.html(contact_form_html, height=720, scrolling=True)
