import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Chọn file Excel (có cột 'Điểm số')", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df)
    scores = df["Điểm số"].tolist()
    st.write(scores)

    def compute_distribution():
        bins = {"90-100": 0, "80-89": 0, "70-79": 0, "60-69": 0, "<60": 0}
        for score in scores:
            if score >= 90:
                bins["90-100"] += 1
            elif score >= 80:
                bins["80-89"] += 1
            elif score >= 70:
                bins["70-79"] += 1
            elif score >= 60:
                bins["60-69"] += 1
            else:
                bins["<60"] += 1
        return bins

    dist = compute_distribution()
    values = dist.values()
    labels = dist.keys()

    fig, ax = plt.subplots(figsize=(1,1))
    ax.pie(values,
           labels=labels,
           autopct='%.1f%%',
           textprops={'fontsize': 3.5})
    ax.axis("equal")
    plt.tight_layout(pad=0.1)
    st.pyplot(fig)
else:
    st.write("Chưa có file nào được upload.")