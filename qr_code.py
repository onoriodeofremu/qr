import streamlit as st
import qrcode
from io import BytesIO
from datetime import datetime

# --- Page config ---
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔳",
    layout="centered"
)

# --- Title & description ---
st.title("🔳 QR Code Generator")
st.write("Paste or type any URL below and get a QR code you can download instantly.")

# --- Input form ---
with st.form("qr_form"):
    url = st.text_input(
        "Enter your URL",
        placeholder="https://example.com"
    )
    filename = st.text_input(
        "File name (optional)",
        placeholder="my-qr-code"
    )
    submitted = st.form_submit_button("Generate QR Code")

# --- Handle submission ---
if submitted:
    if not url.strip():
        st.error("Please enter a URL first.")
    else:
        # Ensure the URL looks reasonable
        clean_url = url.strip()
        if not clean_url.startswith(("http://", "https://")):
            clean_url = "https://" + clean_url

        # Generate the QR code image
        qr = qrcode.QRCode(
            version=None,                      # auto-size
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(clean_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save to an in-memory buffer so the user can download it
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Build a safe file name
        safe_name = (filename.strip() or "qrcode")
        safe_name = "".join(c for c in safe_name if c.isalnum() or c in "-_")
        if not safe_name:
            safe_name = "qrcode"

        st.success("✅ Your QR code is ready!")
        st.image(buffer, caption=f"QR code for: {clean_url}", use_container_width=False)

        st.download_button(
            label="⬇️ Download PNG",
            data=buffer.getvalue(),
            file_name=f"{safe_name}.png",
            mime="image/png"
        )

# --- Footer ---
st.divider()
st.caption("Built with Streamlit + qrcode")