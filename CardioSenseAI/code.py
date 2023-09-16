#  Required Libraries

import pandas as pd
import streamlit as st
from streamlit_option_menu import *
from streamlit_extras import *
from streamlit_extras.keyboard_url import keyboard_to_url
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
import json as js
import pymongo as pm
import time
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#______________________________________________________________________________________________________________________

# Page Config
st.set_page_config(page_title='CardioSense AI By Praveen', layout="wide")


class CardioSense_AI:

    def process(self):
        predict_data = []
        with st.sidebar:
            selected = option_menu(
                menu_title="CardioSense AI",
                options=['Intro', "ML Process"],
                icons=['mic-fill', 'person-square'],
                menu_icon='alexa',
                default_index=0,
            )
        if selected == 'Intro':

            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            # Start Intro
            col1, col2 = st.columns([7, 3])
            with col1:
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color: cyan;'>Howdy ,</span> <span style='color: white;'> I am Praveen</span> </h1>",
                    unsafe_allow_html=True)

                title_text = "<h1 style='color:cyan; font-size: 60px;'>A Data Science Aspirant From India</h1>"
                st.markdown(title_text, unsafe_allow_html=True)

                title_text = "<h6 style='color:white; font-size: 15px;'><span style='color: white;'>I am Detective who finding hidden pattern and insights from complex data to help for business decisions, hit </span><span style='color: cyan;'> 'P' </span><span style='color: white;'>on keyboard to know about me</span></h6>"
                st.markdown(title_text, unsafe_allow_html=True)
                # st.markdown(
                #     "<h1 style='font-size: 80px;'><span style='color: cyan;'>Lets</span> <span style='color: white;'>    Explore</span> </h1>",
                #     unsafe_allow_html=True)

                keyboard_to_url(key="P", url="https://www.linkedin.com/in/praveen-n-2b4004223/")

            with col2:
                file = lottie("cyan_boy_lap2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=500,
                    key=None
                )

            st.write("")
            st.write('')
            st.write("")
            st.write('')
            st.write("")
            st.write("")
            st.write('')
            st.write("")

            # ______________________________________________________________ABOUT PROJECT______________________________________________________________________________________


            st.markdown("<h1 style='font-size: 60px;'><span style='color: white;'>About</span> <span style='color: cyan;'> CardioSense AI</span> </h1>",unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 8, 3])
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie('hospital_symbok.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=570,
                    width=800,
                    key=None
                )
            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([3, 8, 3])
            # with col2:
            title_text = "<h1 style='color:white; font-size: 50px;'>What Has Praveen Done in this project?</h1>"
            st.markdown(title_text, unsafe_allow_html=True)


            col1, col2, col3 = st.columns([3, 8, 3])
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie('boydoubtface.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=550,
                    width=700,
                    key=None
                )
            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([5, 8, 3])
            # with col2:
            col2.markdown("<h1 style='font-size: 80px;'><span style='color: cyan;'>Lets</span> <span style='color: white;'>    Explore</span> </h1>",unsafe_allow_html=True)

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3 = st.columns([3, 8, 3])
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie('down_arrow.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=700,
                    key=None
                )
            #___________________________________________________________________________PROBLEM Statement____________________________________________
            st.write("")
            st.write("")
            st.write("")

            st.markdown("<h1 style='font-size: 60px;'><span style='color: white;'>Problem</span> <span style='color: cyan;'> Statement</span> </h1>",unsafe_allow_html=True)

            col1, col2, col3 = st.columns([4, 8, 3])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.markdown("<h1 style='font-size: 50px;'></span> <span style='color: cyan;'>Patient</span><span style='color: white;'> Heart Disease </span><span style='color:cyan;'> Prediction</span> </h1>",unsafe_allow_html=True)
            col1, col2, col3 = st.columns([3, 8, 3])
            with col2:
                file = lottie('problem_statement.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=570,
                    width=800,
                    key=None
                )
            # st.write("")
            # st.write("")
            # st.write("")
            #_______________________________________________________________________________________STEPS________________________________________________#
            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([6, 8, 3])
            # with col2:
            col2.markdown(
                "<h1 style='font-size: 80px;'><span style='color: cyan;'>View </span> <span style='color: white;'>  Steps</span> </h1>",
                unsafe_allow_html=True)

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3 = st.columns([3, 8, 3])
            with col2:
                file = lottie('down_arrow.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=700,
                    key=None
                )

            # _________________________________________________________Steps 1 __________________________________________________________

            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([3, 23, 3])

            col2.markdown( "<h1 style='font-size: 55px;'><span style='color:white;'>Get Data From </span> <span style='color:cyan;'> Praveen's </span><span style='color:white;'> Github Repository</span> </h1>",unsafe_allow_html=True)
            keyboard_to_url(key="d", url="https://github.com/praveendecode/Datasets/blob/main/Ml_dataset/SugarSense_AI.csv")
            col1, col2, col3 = st.columns([3, 8, 3])
            with col2:
                file = lottie('github.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    height=500,
                    width=700,
                    key=None
                )
            # _________________________________________________________________________________Step 2_____________________________________________________________________________________________________________________
            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([5.7, 23, 3])

            col2.markdown( "<h1 style='font-size: 55px;'><span style='color:white;'>Data</span> <span style='color:cyan;'> Exploration </span><span style='color:white;'>  and </span><span style='color:cyan;'>  Preprocessing</span> </h1>",unsafe_allow_html=True)


            col1,  col3 = st.columns([15, 15])
            # col2.write("")
            # col2.write("")
            with col1:
                file = lottie('dashboard_1.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=680,
                    width=600,
                    key=None
                )
            with col3:
                file = lottie('step2_1.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=680,
                    width=800,
                    key=None
                )
            col3.write("")
            col3.write("")

            # _______________________________________________________________________________step 3_____________________________________________________


            col1, col2, col3 = st.columns([7, 25, 3])

            col2.markdown( "<h1 style='font-size: 60px;'><span style='color:white;'>Model</span> <span style='color:cyan;'>Selection</span><span style='color:white;'>  and </span><span style='color:cyan;'> Training</span> </h1>",unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 10, 3])
            # col2.write("")
            # col2.write("")
            with col2:
                file = lottie('model_training.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=700,
                    width=780,
                    key=None
                )
                # _______________________________________________________________________________step 4_____________________________________________________

            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3 = st.columns([5, 25, 3])

            col2.markdown(
                "<h1 style='font-size: 65px;'><span style='color:white;'>Collect</span> <span style='color:cyan;'> Heart Disease</span><span style='color:white;'> Data From User</span> </h1>",
                unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 10, 3])
            col2.write("")
            col2.write("")
            with col2:
                file = lottie('diabetes_data_2.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=600,
                    width=800,
                    key=None
                )
            #___________________________________________________________________________________________________________________________
            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3 = st.columns([8, 25, 3])

            col2.markdown(
                "<h1 style='font-size: 70px;'><span style='color:white;'>Patient's </span> <span style='color:cyan;'> Cardio </span><span style='color:white;'> Status</span> </h1>",
                unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 10, 3])
            col2.write("")
            col2.write("")
            with col2:
                file = lottie('plus_medical.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=880,
                    key=None
                )

            # ____________________________________________________________step 5_____________________________________________________________

            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3 = st.columns([3, 25, 3])

            col2.markdown(
                "<h1 style='font-size: 50px;'><span style='color:white;'>Finally Here </span> <span style='color:cyan;'> Praveen </span><span style='color:white;'> To Share His Work To You</span> </h1>",
                unsafe_allow_html=True)


            col1, col2, col3 = st.columns([3, 10, 2])

            with col2:
                file = lottie('code_explnation.json')
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=700,
                    width=1000,
                    key=None
                )
            colored_header(
                label="",
                description="",
                color_name="blue-green-70"
            )
        elif selected == 'ML Process':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)
            # Data Collection
            df = pd.read_csv('CardioSense_AI.csv')

            # Data preprocessing
            df['class'] = df['class'].map({'negative':0, 'positive':1})
            # Data Split
            x = df.drop("class", axis=1)
            y = df["class"]
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
            model = DecisionTreeClassifier().fit(x_train, y_train)

            # Patient Input
            col1,col2 ,col3 = st.columns([2,15,2])

            with col2:
               st.markdown( "<h1 style='font-size: 70px;'><span style='color: cyan;'>CardioSense AI </span> <span style='color: white;'>Data </span> <span style='color: cyan;'>Submission</span> </h1>",unsafe_allow_html=True)


               col2.write("")
               col2.write("")
               col2.write("")
               col2.write("")
               col2.write("")
               col2.write("")
               col2.write("")
               col2.write("")

               # ___________________________________________________________________________PROBLEM Statement____________________________________________

               # Gender

            col1 , col2, col3 = st.columns([4,15, 5])

            age_value=0; gender_value=0; impulse_rate=0; highpresure_value=0; lowpressure_value=0; glucose_value=0; kcm_value=0; Troponin_value=0;
           # Gender
            with col2:
               colored_header(
                   label="Select Gender",
                   description="",
                   color_name="blue-green-70")
               gender = st.selectbox('', ['Choose 👇','Female', 'Male'])
               if gender == 'Female':
                   if st.button('Proceed'):
                     gender_value = 0
                     st.success('Your Gender Data Saved ✅')
               elif gender == 'Male':
                   if st.button('Proceed'):
                       gender_value = 1
                       st.success('Your Gender Data Saved ✅')
            col2.write("")
            col2.write("")

           # Age
            with col2 :
               colored_header(
                   label="Provide Age",
                   description="",
                   color_name="blue-green-70")
               age = st.number_input(" ", min_value=0, max_value=110, value=21, step=1)
               if st.button('save'):
                   age_value = age
                   st.success('Your Age Data Saved ✅')
            col2.write("")
            col2.write("")

           # Impulse rate
            with col2:
               colored_header(
                   label="Provide Impulse Rate",
                   description="",
                   color_name="blue-green-70")
               impulse = st.number_input("        ", min_value=0, max_value=110, value=21, step=1)
               if st.button('PROCESS'):
                   impulse_rate = impulse
                   st.success('Your Impulse Rate  Data Saved ✅')

            col2.write("")
            col2.write("")
           # High Presure
            with col2:
               colored_header(
                   label="Provide High Pressure Rate",
                   description="",
                   color_name="blue-green-70")
               highpresure = st.number_input(" ", min_value=42, max_value=223, value=120, step=1)
               if st.button('PROCEED'):
                   highpresure_value = highpresure
                   st.success('Your High Pressure Rate Data Saved ✅')

            col2.write("")
            col2.write("")


            # pressurelow
            with col2:
                with col2:
                    colored_header(
                        label="Provide Low Pressure Rate",
                        description="",
                        color_name="blue-green-70")
                    lowpresure = st.number_input(" ", min_value=38, max_value=154, value=72, step=1)
                    if st.button('SAVE'):
                        lowpressure_value = lowpresure
                        st.success('Your Low Pressure Rate Data Saved ✅')
            # glucose

            with col2 :

                with col2:
                    colored_header(
                        label="Provide Glucose  Rate",
                        description="",
                        color_name="blue-green-70")
                    Glucose = st.number_input(" ", min_value=35, max_value=541, value=146, step=1)
                    if st.button('Store'):
                        glucose_value = Glucose
                        st.success('Your  Glucose Rate Data Saved ✅')
            col2.write("")
            col2.write("")



            # kcm

            with col2:

                with col2:
                    colored_header(
                        label="Provide 	KCM  Rate",
                        description="",
                        color_name="blue-green-70")
                    kcm = st.number_input("                ", min_value=0, max_value=300, value=15, step=1)
                    if st.button('Save'):
                        kcm_value = kcm
                        st.success('Your KCM  Data Saved ✅')
            col2.write("")
            col2.write("")

            # kcm

            with col2:

                with col2:
                    colored_header(
                        label="Provide Troponin Rate",
                        description="",
                        color_name="blue-green-70")
                    Troponin = st.number_input(" ", min_value=0, max_value=10, value=0, step=1)
                    if st.button('STORE'):
                        Troponin_value = Troponin
                        st.success('Your Troponin Rate Data Saved ✅')
            col2.write("")
            col2.write("")

            # Test Value
            test = [age_value,gender_value,impulse_rate,highpresure_value,lowpressure_value,glucose_value,kcm_value,Troponin_value]

            col1, col2, col3 = st.columns([8, 8, 3])
            if col2.button("Get Status"):
                col2.write("")
                col2.write("")
                col2.write("")
                col1, col2, col3 = st.columns([3.5,8 , 3])
                with col2:
                    file = lottie('heart_rate_2.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=470,
                        width=600,
                        key=None
                    )
                st.write("")
                st.write("")
                st.write("")
                with col2:
                    with st.spinner('WAIT FOR YOUR RESULT !!!'):
                        time.sleep(5)

                # Prediction process
                result = model.predict([test])

                result = model.predict([test])
                col1, col2, col3 = st.columns([10,9 ,10])
                if result == "":

                    with col1:
                        file = lottie('star2.json')
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=300,
                            width=400,
                            key=None
                        )

                    with col3:
                        file = lottie('star2.json')
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=400,
                            width=500,
                            key=None
                        )

                    with col2:
                        file = lottie('stareyeblick.json')
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=300,
                            width=400,
                            key=None
                        )
                    col1, col2, col3 = st.columns([5, 9, 2])
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:cyan;'>SugarSense AI Reported : </span> <span style='color:white;'> No Heart Disease</span> </h1>",
                        unsafe_allow_html=True)

                elif result == 1:
                    col1, col2, col3 = st.columns([2, 9, 2])
                    with col2:
                        file = lottie('doctor_sugar.json')
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=600,
                            width=900,
                            key=None
                        )
                    col1, col2, col3 = st.columns([4, 9,2])
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:cyan;'>SugarSense AI Reported : </span> <span style='color:white;'> Heart Diasease (Consult Doctor)</span> </h1>",
                        unsafe_allow_html=True)


# Object Creation :
object = CardioSense_AI()
object.process()
