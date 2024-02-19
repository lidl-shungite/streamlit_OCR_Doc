import streamlit as st
# from Home import stream_line
import os
import time
import pandas as pd
import plotly.express as px


def stream_line(sentence):
    for word in sentence.split():
        yield word + " "


def create_plot(df, mode):
    fig = px.line(data_frame=df, x='Step', y=[f'Train {mode}', f'Validation {mode}'], hover_name='Step',
                     labels={'Step': 'Steps', 'value': f'{mode}', 'variable': 'Dataset'},
                     color_discrete_map={f'Train {mode}': '#1f77b4', f'Validation {mode}': '#ff7f0e'})
    fig.update_layout(xaxis=dict(showgrid=True), yaxis=dict(showgrid=True))
    return fig


def document():
    container = st.container(border=False)
    new_title = '<p style="font-size:50px; font-weight:bold; color: #0d6efd;">PicCalcBot</p>'
    container.markdown(f"{new_title}", unsafe_allow_html=True)
    container.subheader('Introduction to :blue[PicCalcBot] Documentation')
    container.write_stream(stream_line("Welcome to the official documentation for PicCalcBot, the AI-integrated "
                                       "calculator application designed to simplify mathematical operations using the "
                                       "power of artificial intelligence. PicCalcBot offers a user-friendly interface "
                                       "for performing basic arithmetic operations utilizing state-of-the-art "
                                       "technologies "
                                       "across. Unfortunately, addition, subtraction, multiplication, and division are "
                                       "the only available operations for current version of the application."))
    container.divider()
    container.text('')
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
    container.write_stream(
        stream_line("**Docker for Server Side**: Docker is used to ensure consistent, isolated, and portable "
                    "development across different environments and platforms."))
    ex = container.expander("See simple visual explanation on how Docker works", expanded=False)
    ex.image("other_images/docker_meme.jpeg", width=200)
    ex1 = container.expander("See visual explanation on interaction between Flask and Docker", expanded=False)
    ex1.image("other_images/1_jB_sIv780kncRtm3gP6Krg-removebg-preview.png")
    ex2 = container.expander("See visual explanation on how client-side and server-side operates", expanded=False)
    ex2.image("other_images/client-server.png")
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
    container.divider()
    container.text('')
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
    labels_lt = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                 'Nine', 'Addition', 'Subtraction', 'Multiplication', 'Division', 'Open-Bracket', 'Close-Bracket']
    col1 = container.columns(4)
    col2 = container.columns(4)
    col3 = container.columns(4)
    col4 = container.columns(4)
    datadir = "./images"
    for images in os.listdir(datadir):
        data_img.append(images)

    imge_list = [0,1,2,3,4,5,6,7,8,9,'Addition', 'bSubtraction', 'cMultiplication', 'Division','Open-Bracket', 'xClose-Bracket']

    i = 0
    for rows in col1 + col2 + col3 + col4:
        tile = rows.container(height=180, border=False)
        tile.image(f'images/{imge_list[i]}.png', width=75)
        tile.markdown(labels_lt[i])
        i+=1
    container.divider()
    container.text('')
    container.subheader('Building a Model')
    container.write_stream(stream_line("Now, we'll talk about how we utilized Tensorflow to build the architecture of "
                                       "a model. The CNN (Convolutional Neural Network) is built with a total of 13 layers ( 3 Convolution"
                                       " 2D layers, 3 Max Pooling 2D layers, 1 Batch Normalization Layer, 1 Flatten layer, 1 Dropout layer, and "
                                       "finally 4 Fully Connected Dense layers ). If you want to know more in detail "
                                       "about these layers, I encourage you to check the official Tensorflow or Keras "
                                       "documentation website. "))
    container.write_stream(stream_line("The following is a diagram recreating the architecture of the model's hidden "
                                       "layers. I hope the visualization helps you understand how the model is built."))
    container.image('other_images/model_architecture.png')
    container.divider()
    container.text('')
    container.subheader("Training and Validating the Model")
    container.write_stream(stream_line("After building the model, we now commence to train and validate the model "
                                       "using the data. The data is split into 9-part training and 1-part validation, "
                                       "meaning 90% of data is poured into training and 10% into validation. The following"
                                       "are the two graphs representing the learning curve; one for the accuracy and the other"
                                       "for the loss. The learning curve shows how our model's performance changes after each " 
                                       "epoch. Here, loss(error) and accuracy are two metrics used to measure the performance."))

    tab1, tab2 = container.tabs(["Learning Curve ( :blue[Accuracy] )", "Learning Curve ( :blue[Loss] )"])
    with tab1:
        tab1.plotly_chart(create_plot(pd.read_csv("logs/accuracy.csv"), 'Accuracy'), theme="streamlit", use_container_width=True)
    with tab2:
        tab2.plotly_chart(create_plot(pd.read_csv("logs/loss.csv"), 'Loss'), theme="streamlit", use_container_width=True)
    container.divider()
    container.text('')
    container.subheader("Testing of Model")
    container.write_stream(stream_line("Now, we enter the phase of testing each class in the dataset. How this works is"
                                       " by taking a 3000 samples of one class and take 200 samples from other classes."
                                       " Down below is the confusion matrix showing how correct our model is on each "
                                       "class."))
    folders = [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Multiplication",
        "Subtraction",
        "Open-Bracket",
        "Close-Bracket",
        "Addition",
        "Division"]
    acc_scores = ["100", "98.96", "100", "99.9", "99.76", "99.93", "99.96", "99.55", "99.96", "98.18", "99.98", "97.45",
                  "99.89",
                  "98.46", "98.76", "98.55"]
    acc_s = dict(zip(folders, acc_scores))
    cf_option = container.selectbox("", folders, index=None, placeholder="Select class of confusion matrix")
    if cf_option is None:
        container.write("")
        container.write_stream(stream_line(f"You selected : :blue[{cf_option}]"))
    elif cf_option in folders:
        container.write_stream(stream_line(f"You selected : :blue[{cf_option}]"))
        container.write_stream(
            stream_line(f"The model has an accuracy of  :blue[{acc_s[cf_option]}]% on :blue[{cf_option}] class."))
        container.image(f"cf_images/{cf_option}.png")

if __name__ == '__main__':
    document()
