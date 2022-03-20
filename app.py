
import streamlit as st


def main():
    page = st.sidebar.selectbox("Select a Page",["Project", "raw data","analysed data"])

    #First Page
    if page == "Project":
        homepage()

    #Second Page
    elif page == "raw data":
        analyseddata()
    
    #Third Page
    elif page == "analysed data":
        information()
        
def homepage():
    
    st.title('Project')
    st.write('xxxx')
 
def homepage():
    
    st.title('Raw data')
    st.write('xx')
 
    
def homepage():
    
    st.title('Analysed data')
    st.write('xxx')
 

if __name__ == "__main__":
    main()
    
    
    
