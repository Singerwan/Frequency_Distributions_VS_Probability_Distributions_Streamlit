import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
from itertools import combinations
from streamlit_option_menu import option_menu

with st.sidebar:
        selected= option_menu(menu_title="Main",
        options=["Frequency_distribution Probability_distribution"]
                  ,icons=["house"],menu_icon="cast",default_index=0)
        
if selected=="Frequency_distribution Probability_distribution":
    st.text(" ")

st.subheader("Frequency_distribution Probability_distribution")
Frequency_distribution   =["Oragnize raw data into table form",
    "Are Jumpstart to graphs",
    "Show what actually happend(REALITY)"]
Probability_distribution =["Describe what will probability happedn based on assigned probability for every possible outcome.",
    """All probabilities are between impossible to certain
   <span style="color:cyan">0-1 inclusive</span>. 
    <br><span style="color:yellow">Sum up to 1</span> 
    <br>
    | area under curve is 1<br><hr>
    eg: roll a die$\\frac{
    \\textcolor{red}{\\overbrace{\\boxed{\\Huge \\text{1 + 1 + 1 + 1 + 1 + 1}}}^{\\Huge 1 , 2, 3 ,4 ,5 ,6}}}{\\Huge \\textcolor{cyan}{6}}=1$
    <hr>
    <table><th>X</th><th>Probability Distribution<br>P(X)-Roll once</th><th>Frequency-Distribution<br>-Counts Roll 30Times</th>
    <th>Why do we need it and what's the use case?</th>
        <tr><td>1</td><td>$\\frac{1}{6}$</td><td>7</td><td>Business|sales</td></tr>
        <tr><td>2</td><td>$\\frac{1}{6}$</td><td>5</td><td>Insurance</td></tr>
        <tr><td>3</td><td>$\\frac{1}{6}$</td><td>6</td><td>Medical</td></tr>
        <tr><td>4</td><td>$\\frac{1}{6}$</td><td>5</td><td>Weather|Stocks</td></tr>
        <tr><td>5</td><td>$\\frac{1}{6}$</td><td>4</td><td>Daily life</td></tr>
        <tr><td>6</td><td>$\\frac{1}{6}$</td><td>3</td><td>Risk|engineering</td></tr>
    <tr><td>Die <br>6_Sides</td>
            <td style="color:cyan;background-color:indigo">Theoretically <br>equal probability<br>prep work done</td>
            <td style="color:black;background-color:cyan">Actually happen  <br>unless scaled up 1m</td>
            <td style="color:yellow;background-color:black">descion | prediction</td></tr>
    </table>
    """,
                           "Can be in table form,graph,or even a formula"]
df_style=pd.DataFrame({"Frequency_distribution":Frequency_distribution,"Probability_distribution":Probability_distribution}).style.\
set_table_styles([{"selector":"th","props":"border:solid yellow 2px"},
                  {"selector":"td","props":"border:dotted cyan 1.4px"},
                  {"selector":" ","props":"border:solid yellow 2px"}])

st.image("Frequency_Prob.png")
