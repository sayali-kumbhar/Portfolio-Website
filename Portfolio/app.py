import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as a:
        st.markdown(f"<style>{a.read()}</style>",unsafe_allow_html=True)

local_css(r"Portfolio/style.css")
lottie_data=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_qp1q7mct.json")
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_glp2wakj.json")
lottie_reach_me=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_gaplvsns.json")
img_job_portal_website=Image.open(r"Portfolio/image/job portal.jpeg")
img_blog_website=Image.open(r"Portfolio/image/blog.jpg")
img_flight_fare=Image.open(r"Portfolio/image/flight fare prediction.jpg")
img_health_expense=Image.open(r"Portfolio/image/healthcare.png")
img_twitter_sentiment=Image.open(r"Portfolio/image/twitter sentiment analysis.jpg")
img_fake_news= Image.open(r"Portfolio/image/fake news.jpg")
img_hackerrank_profile=Image.open(r"Portfolio/image/Hackerrank Profile.png")
img_gilbert_research=Image.open(r"Portfolio/image/gilbert research centre.png")
img_applied_AI=Image.open(r"Portfolio/image/Applied AI.png")
                            



# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hi :wave:, I am Sayali Kumbhar")
        st.write(
            """
            Passionate Python Developer 
            | Enthusiastic about Machine Learning 
            | Seeking Opportunities to Innovate and Grow
            """
        )
    
    with right_column:
        st_lottie(lottie_data, height=300, key="data science")



# ---- SKILLS WHICH I HAVE ----
with st.container():
    st.write("---")
    right_column, left_column = st.columns(2)
    with left_column:
        st.header("Skills Which I have")
        st.write("##")
        col1,col2=st.columns(2)
        with col1:
            st.write(
                """
                Prompt Engineering \n
                Programming Proficiency \n
                - Python \n
                Data Manupulation and Analysis \n
                - Numpy \n
                - Pandas \n
                Data Visualization \n
                - Seaborn \n
                - Matplotlib \n
                Machine Learning Tools \n
                - Machine Learning \n
                - Scikit Learn \n""")
        with col2:
            st.write("""
            Model Deployment \n
            - Flask \n
            - Streamlit \n
            Database Skills \n
            - MySQL \n
            - Github \n
            - Git \n
            - Django \n
            - HTML \n
            - CSS \n
            """)
    with right_column:
        st_lottie(lottie_coding, height=600, key="coding")



# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    with st.container():
        image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_job_portal_website,width=200)
    with text_column:
        st.subheader("Job Portal Website")
        st.write(
            """The objective of this python project is to develop an online portal where recruiters can post job requirements, 
            they can search for candidates. Candidates can search for job openings and apply."""
        )
        st.markdown("[Full Source Code...](https://github.com/sayali-kumbhar/job-portal-website-using-Django/tree/main)")
    
    
    with st.container():
        image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_blog_website,width=200)
    with text_column:
        st.subheader("Blog Application")
        st.write(
            """Created Blog Application where I can add my blog and user can share comment on blog"""
        )
        st.markdown("[Full Source Code...](https://github.com/sayali-kumbhar/Blog-Application-using-Django)")


    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_flight_fare,width=200)
        with text_column:
            st.subheader("Flight Fare Prediction Using Machine Learning")
            st.write(
                """The main goal is to predict the fares of the flights based on different factors available in the provided dataset."""
            )
            st.markdown("[Full Source Code...](https://github.com/sayali-kumbhar/Flight-Fare-Prediction-using-machine-learning)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_health_expense,width=200)
    with text_column:
        st.subheader("Healthcare Expense Predictor")
        st.write(
            """The aim of this project is building a web application which
               calculates expenses using Flask Framework"""
        )
        st.markdown("[Full Source Code...](https://github.com/sayali-kumbhar/Implementation-of-Flask-)")


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_twitter_sentiment,width=200)
    with text_column:
        st.subheader("Amazon Fine food Reviews Analysis")
        st.write(
            """Task of this project is from given reviews Determine whether the review is positive/negative."""
        )
        st.markdown("[Full Source Code...](https://github.com/sayali-kumbhar/Amazon-fine-food-reviews-analysis)")


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_fake_news,width=200)
    with text_column:
        st.subheader("Fake News Detection using Machine Learning")
        st.write(
            """In this project I have performed feature extraction on the dataset and detected wether the news is fake or not.
            """
        )
        st.markdown("[Full Source Code...](https://github.com/sayali-kumbhar/Fake-News-Detection-Using-Machine-learning)")
    


#----Experience----

with st.container():
    st.write("----")
    st.header("Experience")
    st.write("##")

    with st.container():
        image_column,text_column=st.columns((1,2))
        with image_column:
            st.image(img_gilbert_research)
        with text_column:
            st.subheader("Data Science and Machine Learning Intern")
            st.write("Company-Gilbert Research Centre")
            st.write("Skills which I have learnt are machine learning,deep learning,computer vision")
            st.markdown("[Certificate of internship completion](https://drive.google.com/file/d/1YqO8bfh2twzBLfv3J28yxKIgws-g1vSM/view?usp=drive_link)")


with st.container():
    image_column,text_column=st.columns((1,2))
    st.write("##")
    with image_column:
        st.image(img_applied_AI)
    with text_column:
        st.subheader("Machine Learning Student")
        st.write("Company-Applied AI")
        st.write("I have learnt data is most important thing and how to find insights from data by applying concepts like Machine Learning ,I have learned skill like Different Data Visualization tools(matplotlib,seaborn),Exploratory data analysis,Basics of Deep Learning,Flask,Streamlit.")
        st.markdown("[Certificate of completion](https://www.appliedaicourse.com/certificate/f8c11903c7)")

#---Certifications---
with st.container():
    st.write("---")
    st.header("Certifications")
    st.write("##")
    st.subheader("British Airways Virtual Experience Program on Forage")
    st.write("I completed practical tasks in: Web scraping to gain company insights Predicting customer buying behaviour")
    st.markdown("[Certificate of completion](https://drive.google.com/file/d/1pdvoaviCk--ECwhKEIn0LtoS6YuaTclr/view?usp=sharing)")
    
                     
#---Additional Information---
with st.container():
    st.write("---")
    st.header("Additional Information")
    st.write("##")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_hackerrank_profile)
        with text_column:
            st.subheader("Hackerrank profile")


# ---- CONTACT ----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("Contact me")
        st.write("##")
        st.write(
            "Email Id: sayalisureshkumbhar@gmail.com")
        st.write("Connect with me on linkedin:-https://www.linkedin.com/in/sayali-kumbhar/""")
        st.write("Follow me on Medium:-https://medium.com/@sayalisureshkumbhar")
    with left_column:
        st_lottie(lottie_reach_me, height=300, key="contact")
