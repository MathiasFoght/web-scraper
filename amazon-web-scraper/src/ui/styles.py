import streamlit as st


def apply_styles() -> None:
    st.markdown(
        """
        <style>
          @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Source+Serif+4:wght@500;700&display=swap');

          :root {
            --surface: #111a24;
            --ink: #e8eef7;
            --muted: #a4b3c5;
            --accent: #14b8a6;
            --accent-soft: #123c3a;
            --border: #223041;
            --card-shadow: 0 16px 30px rgba(0, 0, 0, 0);
          }

          .stApp {
            color: var(--ink);
            font-family: "Space Grotesk", sans-serif;
          }

          h1, h2, h3 {
            font-family: "Source Serif 4", serif !important;
            letter-spacing: 0.2px;
          }

          .hero {
            color: #ffffff;
            border-radius: 14px;
            box-shadow: var(--card-shadow);
            margin-bottom: 1rem;
          }

          .hero p {
            margin: 0.3rem 0 0;
            color: rgba(255, 255, 255, 0.92);
          }

          .subtle {
            color: var(--muted);
            font-size: 0.92rem;
          }

          div[data-testid="stMetric"] {
            background: #000;
            border: 1px solid #233346;
            border-radius: 12px;
            padding: 0.55rem 0.65rem;
          }

          div[data-testid="stButton"] > button {
            border-radius: 10px;
            border: 1px solid #0f766e;
            background: #0f766e;
            color: #ffffff;
            font-weight: 600;
          }

          div[data-testid="stButton"] > button:hover {
            border-color: #0d6d65;
            background: #0d6d65;
            color: #ffffff;
          }

          @media (max-width: 640px) {
            .hero {
              padding: 1rem;
            }
          }
        </style>
        """,
        unsafe_allow_html=True,
    )
