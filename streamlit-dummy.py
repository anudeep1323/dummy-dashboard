import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
    .top-bar {
        background-color: #002C61;
        padding: 10px 20px;
        color: white;
        font-family: 'Helvetica';
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 15px;
    }

    .logo-section {
        display: flex;
        align-items: center;
    }

    .logo-section img {
        height: 40px;
        margin-right: 10px;
    }

    .title-section {
        font-size: 24px;
        font-weight: bold;
        margin-left: 20px;
    }

    .controls-section {
        display: flex;
        align-items: center;
    }

    .controls-section .control-item {
        margin-left: 20px;
        font-size: 14px;
        color: white;
    }

    .controls-section .control-item button {
        background-color: #f8f9fa;
        border: 1px solid #E0E0E0;
        padding: 6px 12px;
        border-radius: 4px;
        color: #002C61;
        cursor: pointer;
    }

    .controls-section .control-item button:hover {
        background-color: #E0E0E0;
    }

    .sidebar {
        background-color: #F7F9FB;
    }

    .nissan-logo {
        text-align: center;
        padding: 0px 0;
        font-size: 60px;
        font-weight: bold;
        color: #000000;
        font-family: 'Helvetica';
    }

    .nissan-subtext {
        text-align: center;
        font-size: 17px;
        letter-spacing: 2px;
        color: #333;
        margin-top: -10px;
        font-family: 'Helvetica';
    }

    .sidebar-content {
        padding: 20px;
    }

    .sidebar-item {
        padding: 10px;
        font-size: 1.1rem;
        color: #333;
        display: flex;
        align-items: center;
    }
    
    .sidebar-item img {
        margin-right: 10px;
    }

    .active {
        background-color: #EDEFF1;
        border-radius: 15px;
        color: #002C61;
        font-weight: bold;
        margin-right: 5px;
    }

    .sidebar-item:hover {
        background-color: #f0f0f0;
        border-radius: 8px;
        color: #002C61;
    }

    .sidebar-item i {
        font-size: 1.2rem;
        margin-right: 10px;
    }

    .section-container {
        background-color: #eeeeee;
        padding: 10px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    
    .section-container1 {
        background-color: #7483a2;
        padding: 5px;
        border-radius: 15px;
        margin-bottom: 20px;
    }

    .section-title {
        color: white;
        font-weight: bold;
        font-size: 1.45em;
        margin-bottom: 10px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        background-color: white;
    }

    th, td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }

    .claim-table th {
        background-color: #7483a2;
        color: white;
        padding: 5px;
        text-align: left;
    }

    .claim-table td {
        padding: 10px;
        border-bottom: 1px solid #7483a2;
    }

    .genai-table th, .genai-table td {
        padding: 12px;
        text-align: left;
    }

    .genai-button {
        background-color: #1c3668;
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1em;
        text-align: center;
        display: inline-block;
    }

    .genai-button:hover {
        background-color: #112947;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="top-bar">
        <div class="logo-section">
            <span class="title-section">VIN - Management</span>
        </div>
        <div class="controls-section">
            <div class="control-item">
                <button>Custom Date Range</button>
            </div>
            <div class="control-item">
                <button>Filter</button>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div class="nissan-logo">NISSAN</div>
    <div class="nissan-subtext">MOTOR CORPORATION</div>
    <div class="sidebar-content">
        <div class="sidebar-item">
            <i>⚡</i> Dashboard
        </div>
        <div class="sidebar-item active">
            <i>📈</i> VIN Management
        </div>
        <div class="sidebar-item">
            <i>👥</i> Supplier
        </div>
        <div class="sidebar-item">
            <i>⚙️</i> Settings
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='section-container1'><h3 class='section-title'>Supplier Performance</h3>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    vin_number = st.selectbox("VIN Number", ["JNBV7ARIEM696855", "ABC12345DEF67890"])

with col2:
    engine_code = st.selectbox("Engine Model Code", ["ALTIMA", "SENTRA", "MAXIMA"])

with col3:
    wmi = st.selectbox("World Manufacturer Identifier", ["USA", "Japan", "Germany"])

with col4:
    model_year = st.selectbox("Model Year", ["2017", "2018", "2019", "2020"])

st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='section-container1'><h3 class='section-title'>Claim Summary</h3>", unsafe_allow_html=True)
    
    claim_data = {
        'Claim No': ['Claim 1', 'Claim 2', 'Claim 3', 'Claim 4'],
        'Part Name': ['Fuel Part', 'AC', 'AC', 'AC'],
        'Supplier Name': ['Supplier 1', 'Decostar', 'Decostar', 'Decostar']
    }
    
    claim_df = pd.DataFrame(claim_data)
    
    st.markdown(claim_df.to_html(classes='claim-table', index=False), unsafe_allow_html=True)

with col2:
    st.markdown("<div class='section-container1'><h3 class='section-title'>Gen AI</h3>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <table class='genai-table'>
            <tr>
                <th>Category</th>
                <th>Details</th>
            </tr>
            <tr>
                <td>Summary</td>
                <td>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ultricies tortor sit amet nunc luctus, vitae rutrum nulla pharetra.</td>
            </tr>
            <tr>
                <td>Root Cause Analysis</td>
                <td>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam bibendum odio nec velit placerat, at consectetur sapien commodo.</td>
            </tr>
        </table>
        """, unsafe_allow_html=True
    )

    st.markdown("<button class='genai-button'>Submit Gen AI Summary</button>", unsafe_allow_html=True)

st.markdown("<div class='section-container1'><h3 class='section-title'>Part Summary</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    customer_complaint = st.selectbox("Customer Complaint", ["76089911", "12345678", "87654321"])

with col2:
    dealer_comments = st.selectbox("Dealer Comments", ["JN1BV7AR1EM696855", "ABC98765", "XYZ12345"])

with col3:
    issue_category = st.selectbox("Issue Category", ["Category 1", "Category 2", "Category 3"])

st.markdown(
    """
    <table class='part-table'>
        <tr>
            <td colspan='3'><strong>Issue Summary</strong></td>
            <td colspan='3'><strong>RCA Category</strong></td>
        </tr>
        <tr>
            <td colspan='3'>Nam vel pretium ipsum. Vestibulum nec purus ut tellus mollis venenatis id non nulla. Praesent hendrerit interdum risus vel sollicitudin.</td>
            <td colspan='3'>Nam vel pretium ipsum. Vestibulum nec purus ut tellus mollis venenatis id non nulla. Praesent hendrerit interdum risus vel sollicitudin.</td>
        </tr>
    </table>
    """,
    unsafe_allow_html=True
)
