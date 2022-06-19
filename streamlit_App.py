import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError
def get_fruityvice_data(this_fruit_choice):
    responce = requests.get("https://fruityvice.com/api/fruit/"+user_input)
    streamlit.text(responce.json())
    normalize = pandas.json_normalize(responce.json())
    return normalize


try:
  user_input = streamlit.text_input("eneter your fruit","Kiwi")
  if not user_input:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(user_input)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
    streamlit.error()


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list= my_fruit_list.set_index('Fruit')
#selectfruit = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit),['Apple'])
selectfruit=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple'])

showfruit = my_fruit_list.loc[selectfruit]
streamlit.dataframe(showfruit)
streamlit.dataframe(my_fruit_list)
streamlit.dataframe(showfruit)

streamlit.stop()
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
if streamlit.button('Grt Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row = get_fruit_load_list()
    streamlit.dataframe(my_data_row)

    

        

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit');")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)
user_input2 = streamlit.text_input("eneter your fruit","Kiwi")
