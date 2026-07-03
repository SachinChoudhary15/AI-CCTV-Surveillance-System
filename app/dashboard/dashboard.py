

import streamlit as st
import pandas as pd
import os
import glob
from PIL import Image

from app.dashboard.analytics import AnalyticsService

# Services
analytics = AnalyticsService()

# Page Config
st.set_page_config(page_title="AI CCTV Surveillance Dashboard", layout="wide")

# Dashboard Title
st.title("AI CCTV Surveillance Dashboard")

# Metrics Section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Alerts", analytics.get_total_alerts())

with col2:
    telegram_count = analytics.get_alerts_by_type().get("telegram_alert", 0)
    st.metric("Telegram Alerts", telegram_count)

with col3:
    st.metric("Total People Detected", analytics.get_total_people_detected())

with col4:
    st.metric("Today's Alerts", len(analytics.get_todays_alerts()))

# Latest Alerts
st.subheader("Latest Alerts")
latest_alerts = analytics.get_latest_alerts()

if latest_alerts:
    st.dataframe(pd.DataFrame(latest_alerts), width="stretch")

else:
    st.info("No alerts found.")

# Latest Snapshots
st.subheader("Latest Snapshots")
snapshot_folder = "data/snapshots"

if os.path.exists(snapshot_folder):
    snapshots = glob.glob(os.path.join(snapshot_folder, "*.jpg"))
    snapshots.sort(key=os.path.getmtime, reverse=True)

    latest_snapshots = snapshots[:5]
    if latest_snapshots:
        cols = st.columns(len(latest_snapshots))

        for col, snapshot_path in zip(cols, latest_snapshots):
            image = Image.open(snapshot_path)
            col.image(image, caption=os.path.basename(snapshot_path), width="stretch")

    else:
        st.info("No snapshots available.")

else:
    st.warning("Snapshot folder not found.")

