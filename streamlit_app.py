import streamlit
streamlit.title("My parents new healthy diner")

streamlit.header("Breakfast Menu")

streamlit.text("🥣 Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 Kale,Spinach and Rocket Smmothie")
streamlit.text("🐔 Hard Boiled free range egg")

streamlit.text("🥑🍞 Avocado toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index("Fruit")
streamlit.multiselect("Pick Some fruits :",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)




