import streamlit as st
import pandas as pd
import numpy as np

st.title("MY PROJECT")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("I love AI VIET NAM")

st.markdown("# Heading 1")
st.markdown("[AI VIET NAM](https://aivietnam.edu.vn/)")
st.markdown(
    """
1. Machine Learning
2. Deep Learning
"""
)
st.markdown("$\sqrt{2x+2}$")
st.latex("\sqrt{2x+2}")

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")
st.markdown(
    ":violet-badge[:material/star: Favorite] \
:orange-badge[⚠ Needs review] \
:gray-badge[Deprecated]"
)

st.code(
    """
import torch
data = torch.Tensor([1, 2, 3])
print(data)
""",
    language="python",
)

st.write("Hello World")
st.write(12345)
st.write({"a": 1, "b": 2})
st.write(pd.DataFrame({"col1": [1, 2], "col2": [3, 4]}))
st.write("This is **Markdown**", unsafe_allow_html=False)


def get_user_name():
    return "Thai"


with st.echo():
    st.write("This code will be printed")

    def get_email():
        return "thai@gmail.com"

    user_name = get_user_name()
    email = get_email()
    st.write(user_name, email)

st.logo("./logo.png")

st.image("./Theme.png", caption="Theme.", width="stretch")
# st.audio("./audio.mp4")
# st.video("./video.mp4")


def get_name():
    st.write("Thai")


agree = st.checkbox("I agree", on_change=get_name)
if agree:
    st.write("Great!")

st.radio("Your favorite color:", ["Yellow", "Blue"], captions=["Vàng", "Xanh"], index=0)

option = st.selectbox("Your contact:", ("Email", "Home phone", "Mobile phone"))
st.write("Selected:", option)

options = st.multiselect(
    "Your favorite colors:",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)
st.write("You selected:", options)

color = st.select_slider(
    label="Your favorite color:", options=["red", "orange", "violet"], value="orange"
)
st.write("My favorite color is", color)

rating = st.select_slider(
    label="Rate the movie:", options=["Bad", "OK", "Good", "Excellent"], value="Good"
)

range_select = st.select_slider(
    label="Select a range of years:",
    options=[2000, 2005, 2010, 2015, 2020, 2025],
    value=(2005, 2020),
)

st.write(rating)
st.write(range_select)

if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Goodbye")
st.link_button("Go to Google", "https://www.google.com.vn/")

st.divider()

if st.button(
    label="Submit", type="primary", help="Click to submit", use_container_width=True
):
    st.write("Button clicked!")

st.link_button(
    label="Go to Streamlit",
    url="https://streamlit.io",
    type="primary",
    use_container_width=True,
)

title = st.text_input("Movie title:", "Life of Brian")
st.write("The current movie title is", title)

username = st.text_input(
    label="Enter your username",
    value="",
    max_chars=20,
    placeholder="e.g. cornel05",
    key="user_input",
    type="default",
)

password = st.text_input(
    label="Password", type="password", placeholder="Enter password"
)

number = st.number_input(label="Insert a number", value=20)
st.write("The current number is ", number)
values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

age = st.number_input(
    label="Enter your age",
    min_value=0,
    max_value=120,
    value=25,
    step=1,
    key="age_input",
)

number = st.slider(label="Pick a number", min_value=0, max_value=100, value=50, step=5)

range_select = st.slider(
    label="Select a range", min_value=0, max_value=100, value=(20, 80)
)

messages = st.container(height=200, border=True)
if prompt := st.chat_input("Say something"):
    messages.chat_message("user", avatar="👤").write(prompt)
    messages.chat_message("assistant", avatar="🤖").write(f"Echo: {prompt}")

# if prompt := st.chat_input("Say something"):
#     st.write(f"You typed: {prompt}")

# with st.chat_message("user", avatar="👤"):
#     st.write("Hello!")

# with st.chat_message("assistant", avatar="🤖"):
#     st.write("Hi there!")

uploaded_files = st.file_uploader(
    label="Choose files",
    accept_multiple_files=True,
    type=("txt", "md", "csv", "jpeg", "png", "pdf"),
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)

with st.form(key="my_form", clear_on_submit=True, border=True):
    colA, colB, colC = st.columns([3, 1, 1], gap="medium", vertical_alignment="center")
    colA.write("Chiếm 3 phần")
    colB.write("Chiếm 1 phần")
    colC.write("Chiếm 1 phần")
    f_name = colA.text_input("First Name")
    m_name = colB.text_input("Middle Name")
    l_name = colC.text_input("Last Name")
    submitted = st.form_submit_button("Submit", type="primary")

with st.form(key="my_form_2", clear_on_submit=True, border=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    submitted = st.form_submit_button("Submit", type="primary")
    if submitted:
        st.write("First Name:", f_name, " - Last Name:", l_name)

df = pd.DataFrame(
    np.random.randn(7, 5),  # (7,5) is the shape of the DataFrame
    columns=("col %d" % i for i in range(5)),
)
st.dataframe(df)

a, b = st.columns(2)
c, d = st.columns(2)
a.metric(
    label="Temperature", value="30°C", delta="-9°C", delta_color="inverse", border=True
)
b.metric(label="Wind", value="4 mph", delta="2 mph", delta_color="inverse", border=True)
c.metric(label="Humidity", value="77%", delta="5%", border=True)
d.metric(label="Pressure", value="30.34 inHg", delta="-2 inHg", border=True)

st.metric(
    label="Revenue",
    value="$10,000",
    delta="+5%",
    delta_color="normal",  # xanh khi tăng, đỏ khi giảm
)

st.metric(
    label="Error rate",
    value="2.3%",
    delta="-0.7%",
    delta_color="inverse",  # đỏ khi tăng, xanh khi giảm
)

chart_data = pd.DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])
st.write(chart_data)
st.bar_chart(chart_data)

line_data = pd.DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])
st.write(line_data)
st.line_chart(line_data)

st.divider()
row1 = st.columns(3)
row2 = st.columns(3)
for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")

with st.sidebar:
    contact = st.selectbox(
        label="How would you like to be contacted?",
        options=["Email", "Phone", "SMS"]
    )
    
    phone_number = email = ""
    
    if contact in ['SMS', 'Phone']:
        phone_number = st.text_input(label="Enter your phone below:", 
                                     placeholder='e.g. 03124567777', )
    else:
        email = st.text_input(label="Enter your mail below:", 
                              placeholder='e.g. abcxyz@gmail.com')
    
    shipping = st.radio(
        label="Choose a shipping method",
        options=["Standard (5-15 days)", "Express (2-5 days)"]
    )
    st.link_button("Go to Google", "https://www.google.com.vn/")

st.write(phone_number)
st.write(email)
