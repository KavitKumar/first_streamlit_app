import streamlit
import pandas

import requests

responce = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
streamlit.text(responce.json())
normalize = pandas.json_normalize(responce.json())
streamlit.dataframe(normalize)
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list= my_fruit_list.set_index('Fruit')
#selectfruit = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit),['Apple'])
selectfruit=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple'])

showfruit = my_fruit_list.loc[selectfruit]
streamlit.dataframe(showfruit)
streamlit.dataframe(my_fruit_list)
streamlit.dataframe(showfruit)
