import streamlit
import pandas
import requests
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

#my_data_row = my_cur.fetchone()
streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_row)
fruit_add = streamlit.text_input("What fruit would you like to add?", "jackfruit")
streamlit.write('The user entered', fruit_add)
my_cur.execute("insert into fruit_load_list values ('" + fruit_add + " ')")
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.dataframe(my_data_rows)




streamlit.stop()
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index(
  'Fruit'
)


fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])                            
fruits_to_show = my_fruit_list.loc[fruits_selected]


streamlit.dataframe(fruits_to_show)

streamlit.title('Hey ho, 2 cats singing')

streamlit.header('Oh my god')
streamlit.text('Kale has just eated a dog')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What Fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

fruityvice_response= requests.get("https://fruityvice.com/api/fruit/" + fruit_choice).json()

fruityvice_normalized = pandas.json_normalize(fruityvice_response)
streamlit.dataframe(fruityvice_normalized)
