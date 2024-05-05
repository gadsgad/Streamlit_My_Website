import streamlit as st

#First Project (Super Stores Dashboard) Date:
st.title("Projects")
st.markdown(" ## 1. Super Stores Sales Analysis")
st.markdown("### **:Grey[Dataset Samples]** ")

# To add 2 columns to the page
col1, col2 = st.columns(2)

with col1:
   container = st.container(border=True)
   container.write("**:blue[Orders list]**")
   container.image("Pages\Assets\P1_Sample1.jpg")

with col2:
   container = st.container(border=True)
   container.write("**:blue[Orders Breakdown]**")
   container.image("Pages\Assets\P1_Sample2.jpg")

# Adding Container and a video inside it.
container = st.container(border=True)
container.write("**:blue[Sales Dashboard Video]**")
container.video("Pages\Assets\Video.mp4")


col1, col2 = st.columns(2)

with col1:
    st.link_button("Power BI Report", "https://app.powerbi.com/home?experience=power-bi")

with col2:
    st.link_button("Dataset File", "https://docs.google.com/spreadsheets/d/1mqTKq0mZivEm4af8ufwhcLJ8CbOULgpd/edit?usp=drive_link&ouid=109175424967829999422&rtpof=true&sd=true")

    
    
st.divider()

#-------------------------------------------------------------------------------------

#2. The Second Project (Bank Customer Churn Rate Dashboard) Date:
st.markdown(" ## 2. Money Bank Customer Churn Rate")
st.markdown("#### **:Grey[Dashboard Samples]** ")

# Creating Containers with Dashboard images
container = st.container(border=True)
container.write("**:blue[Home Page]**")
container.image("Pages\Assets\P2_Dash 1.jpg")

container = st.container(border=True)
container.write("**:blue[Home Page]**")
container.image("Pages\Assets\P2_Dash 1.jpg")

container = st.container(border=True)
container.write("**:blue[Country]**")
container.image("Pages\Assets\P2_Dash 2.jpg")

container = st.container(border=True)
container.write("**:blue[Product]**")
container.image("Pages\Assets\P2_Dash 3.jpg")





#______________________________________________________________________
#The following code used to control the container's height and width.
# st.markdown('''
#             <style>
#             .fullHeight {height : 10vh;
#                   width : 100}
#             </style>''', unsafe_allow_html = True)

# container = st.container(border= True)
# container.markdown("<iframe scr='linke', class = 'fullHeight'></iframe>", unsafe_allow_html = True)
    # st.markdown('''
    #         <style>
    #         .fullHeight {height : 30vh;
    #               width : 40vh}
    #         </style>''', unsafe_allow_html = True)

    # container = st.container(border= True)
    # container.markdown("<iframe scr='linke', class = 'fullHeight'></iframe>", unsafe_allow_html = True)
    # container.image("Pages\Assets\P1_Sample2.jpg")