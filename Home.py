import streamlit as st
import time


def stream_line(sentence, sleep_time=0.02):
    for word in sentence.split():
        yield word + " "
        time.sleep(sleep_time)


def main():
    st.page_link("pages/Documentation.py", label='')
    st.header('Introducing :blue[PicCalcBot]:robot_face:: Your Handy Math Solver App!')
    container = st.container(border=False)
    container.write_stream(stream_line(
        'Ever wish you had a personal math whiz in your pocket? Well, now you do, with PicCalcBot – the coolest math '
        'solver app for your Android device!'))
    container.write_stream(stream_line(
        'PicCalcBot makes math easy-peasy by using your phone\'s camera to solve math problems. Whether you\'re stuck '
        'on a tricky algebra equation or need help with calculus, just snap a pic or upload a photo, and PicCalcBots '
        'will do the rest!'))
    container.write_stream(stream_line('No more scratching your head over math homework. With PicCalcBot, you can say '
                                       'goodbye to math stress and hello to quick and accurate solutions.'))
    container.write_stream(
        stream_line('So why wait? Download PicCalcBot now and let the math magic begin! Math class just '
                    'got a whole lot cooler!'))


if __name__ == '__main__':
    main()