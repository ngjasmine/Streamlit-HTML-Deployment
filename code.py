import streamlit as st
import streamlit.components.v1 as components

# Specify html code below
components.html(
    """
    <style>
    body {
    background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fdata&psig=AOvVaw3u7cbEH1XjGNTkk1g-emvy&ust=1686627651460000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCIjO-OPnvP8CFQAAAAAdAAAAABAE');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
    }
    <h1> My Portfolio </h1>
    <div> I am a junior data scientist specialising in Python and Machine Learning.</div>
    <hr />
    <div> Project 1 - <a href="http://www.github.com" target="_blank">GitHub Link</a> </div>
    <div> Project 2 - <a href="http://www.github.com" target="_blank">GitHub Link</a> </div>
    """,
    height=600,
)
