import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

selectfruit = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit),['Apple'])
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),[4,8])
showfruit = datafram.loc(selectfruit)
streamlit.dataframe(showfruit)
streamlit.dataframe(my_fruit_list)


