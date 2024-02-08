import streamlit as st
#from Home import stream_line
import os

def stream_line(sentence):
    for word in sentence.split():
        yield word + " "


def document():
    container = st.container(border=False)
    new_title = '<p style="font-size:50px; font-weight:bold; color: #0d6efd;">PicCalcBot</p>'
    container.markdown(f"{new_title}", unsafe_allow_html=True)
    container.subheader('Introduction to :blue[PicCalcBot] Documentation')
    container.write_stream(stream_line("Welcome to the official documentation for PicCalcBot, the AI-integrated "
                                       "calculator application designed to simplify mathematical operations using the "
                                       "power of artificial intelligence. PicCalcBot offers a user-friendly interface "
                                       "for performing basic arithmetic operations utilizing state-of-the-art "
                                       "technologies"
                                       "across. Unfortunately, addition, subtraction, multiplication, and division are "
                                       "the only available operations for current version of the application."))
    container.subheader("Technologies Utilized")
    container.write_stream(
        stream_line("**AI Integration**: PicCalcBot is developed using TensorFlow, a leading deep learning "
                    "framework, to incorporate artificial intelligence capabilities into its "
                    "calculation process."))
    container.write_stream(
        stream_line("**React Native Frontend**: The frontend or UI of PicCalcBot is built using React Native, "
                    "providing a seamless and intuitive user experience across various mobile devices."))
    container.write_stream(
        stream_line("**Flask and OpenCV Backend**: The backend of PicCalcBot is powered by Flask, a lightweight and "
                    "versatile web framework, along with OpenCV (CV2) for image processing functionalities."))
    container.divider()
    container.subheader("Getting Started")
    container.write_stream(
        stream_line("Whether you're a developer looking to contribute to the project or a user interested in "
                    "utilizing PicCalcBot for your mathematical needs, this documentation serves as a comprehensive "
                    "guide to understanding and using the application effectively. From installation instructions to "
                    "detailed usage guides and API documentation, you'll find everything you need to maximize the "
                    "potential of PicCalcBot. Firstly, we'll dive into the dataset that has been used to train this "
                    "AI model.")
    )
    container.subheader("Dataset: :blue[Handwritten Digits and Operators]")
    container.write_stream(stream_line("The dataset used in this project is taken from Kaggle. It contains a total of "
                                       "333,895 images, with 16 total classes and each class containing 20,868 images. "
                                       "Of course, these 16 classes are numbers from 0 to 9, four mathematical operators"
                                       " ( +, -, * is written as _, division is written as /) and finally two "
                                       "parentheses ( written as ' [ ' and ' ] ' instead of ' ( ' and ' ) ' ) . "
                                       "Each image has the same size or resolution of 28 x 28. "))
    container.text('')
    container.text('')
    data_img = []
    labels_lt = ['Division', 'Addition', 'Subtraction', 'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
                 'Opened-Parenthesis', 'Closed-Parenthesis', 'Multiplication']
    col1 = container.columns(4)
    col2 = container.columns(4)
    col3 = container.columns(4)
    col4 = container.columns(4)
    datadir = "./images"
    for images in os.listdir(datadir):
        data_img.append(images)
    data_img = iter(data_img)
    labels_lt = iter(labels_lt)
    for rows in col1 + col2 + col3 + col4:
        tile = rows.container(height=180, border=False)
        tile.image(f'images/{next(data_img)}',width=75)
        tile.markdown(next(labels_lt))
    container.subheader('Building a Model')
    container.write_stream(stream_line("Now, we'll talk about how we utilized Tensorflow to build the architecture of "
                                       "a model. The Sequential model is built with "))



document()