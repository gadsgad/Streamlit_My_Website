import streamlit as st
import time

st.set_page_config(
    page_title= "Gad Portfolio")

# To color the title with BLUE color 
st.title(":blue[Home]")

# Writting some details on the sidebar
st.sidebar.markdown("# Gad Shoaib")  
st.sidebar.markdown(" ### *Date Scientist* ") 
st.sidebar.markdown(" *SQL, Python, Power BI* ") 


# To make a container and write inside it
container = st.container(border=True)
container.write(""" Our role is enabling you get valuable insights from your data to make accurate decisions. By   
                working together we will be able maximize your business's profit. """)


# To add 2 columns to the page
col1, col2 = st.columns(2)

with col1:
   st.markdown("#### Super Stores Sales")
   # st.image("P1_Dash 1.jpg")
   # To link this picture to the Projects page to read more information...
   st.page_link("Pages/2_Projects.py", label="Read more ...")

with col2:
   st.markdown(" #### Bank Customer Churn Rate")
   st.image("Pages\Assets\P2_Dash 1.jpg")
   # To link this picture to the Projects page to read more information...
   st.page_link("Pages/2_Projects.py", label="Read more ...")

# Adding a line (divider)
st.divider()

st.markdown("### Sales Dashboard for Super Stores ")
st.video("Pages\Assets\Video.mp4")

st.divider()



#____________________________________________________________________________
# To link a page with another page by this code: 
# The first argument "Pages/2_Projects.py" is the only required, others optional.
#  st.page_link("Pages/2_Projects.py", label="Page 1", icon="1️⃣")
#_____________________________________________________________________________




#Just Trying this code_____________________________________________
