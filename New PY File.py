import streamlit as st
from pathlib import Path

IMG = Path("Assets/methodology")


def render_sources():

    st.title(" Sources & Methodology")

    st.markdown("""
This dashboard visualizes historical transfers of Iranian unmanned aerial systems (UAS) using publicly available information. In addition, the Threat Library serves as a tool for research and analysis. Reported values are simulated. Real world performance might be different. 

The objective of this application is to support exploratory analysis of historical proliferation patterns and Iranian UAV Development. It is intended for research, education, and open-source intelligence (OSINT) visualization.

---

## Primary Data Sources

- United Nations Blast damage Estimator
- SIPRI Arms Transfers Database
- Military Balance (IISS)
- Open-source reporting
- Government publications
- Defence journalism and investigative reporting
- CNAS
- CSIS

---

## Dataset

The dataset records historical export events and includes attributes such as:

- Supplier
- Recipient
- Platform Model
- Year of First Delivery
- Region

Records were standardized, cleaned and geocoded for visualization.

---

## Visualizations

-  Interactive Globe
-  Network Graph
-  Statistical Analysis
-  Dataset Explorer
-  Threat Library

---

## Methodology

1. Collection of open-source records and resources.
2. Validation of recipient and platform information.
3. Standardization of country names.
4. Assigning of geographic coordinates.
5. Building an interactive analytical dashboard using Streamlit and Plotly.

---

## Limitations

This dashboard reflects publicly reported historical transfer events.

Open-source reporting may be incomplete, delayed, or revised over time.

---

## Disclaimer

This project is an independent analytical visualization built using publicly available information.

It is intended solely for research, education, and analytical purposes. 

----

## Note from the Author 

Hello and thank you for visiting my Iranian Drone Proliferation Dashboard and Handbook. I genuinely hoped you liked it. It has taken countless hours of research, drafting, and editing to get this passion project to where it is today. I owe my countless thanks to my teachers, colleagues, and family. To everyone else who inspired me along way I bid my honest thanks and offer my sincerest gratitude. In this project I learned how to collate information from open sources and build something people can cite as Nath.S (2026). 
""")