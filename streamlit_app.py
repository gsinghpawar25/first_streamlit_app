import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError

streamlit.title("My parents new healthy diner")

streamlit.header("Breakfast Menu")

streamlit.text("🥣 Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 Kale,Spinach and Rocket Smmothie")
streamlit.text("🐔 Hard Boiled free range egg")

streamlit.text("🥑🍞 Avocado toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')





my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index("Fruit")
fruits_selected=streamlit.multiselect("Pick Some fruits :",list(my_fruit_list.index),["Avocado","Strawberries"])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("please select fruit to get information.")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
  

streamlit.write('The user entered ', fruit_choice)
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()

def get_fruit_load_list():
  with mycnx.cursor as my_curr:
    my_curr.execute("select * from pc_rivery_db.public.fruit_load_list")
    return my_curr.fetchall()

if streamlit.button('Get Fruitload List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows =get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

streamlit.stop()




streamlit.header("Fruit load list contains:")
streamlit.dataframe(my_data_row)
#streamlit.text("select * from pc_rivery_db.public.fruit_load_list")
#streamlit.text(my_data_row)
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

