import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")


st.header("Performance Metrics")

env_list = ['HCP','AWS']
operation_list = ['Read','Write']
users_list = ['1U', '2U', '3U']
data_list = ['Partitioned','Non Partitioned']
data_size_list = ['100GB','1TB','3TB','10TB']

env_list1 = ['HCP ','AWS ']
operation_list1 = ['Read ','Write ']
users_list1 = ['1U ', '2U ', '3U ']
data_list1 = ['Partitioned ','Non Partitioned ']
data_size_list1 = ['100GB ','1TB ','3TB ','10TB ']

env = st.sidebar.selectbox('Select environment',env_list) 
operation = st.sidebar.selectbox('Select operation',operation_list) 
users = st.sidebar.selectbox('Select users',users_list) 
data = st.sidebar.selectbox('Select data',data_list) 
data_size = st.sidebar.selectbox('Select data size',data_size_list) 

file_name_1 = env+"/"+data_size+"/"+operation+"/"+data+"/"+users
print(file_name_1)s

#data = pd.read_csv(file_name)
# change the queries attribute
#queries = data['queries'].unique()
df = pd.DataFrame(px.data.gapminder())
clist = df['country'].unique()

env_compare = st.selectbox('Select environment',env_list1) 
operation_compare = st.selectbox('Select operation',operation_list1) 
users_compare = st.selectbox('Select users',users_list1) 
data_compare= st.selectbox('Select data',data_list1) 
data_size_compare = st.selectbox('Select data size',data_size_list1) 

file_name_2 = env_compare+"/"+data_size_compare+"/"+operation_compare+"/"+data_compare+"/"+users_compare
print(file_name_2)

col1, col2 = st.columns(2)

fig = px.line(df[df['country'] == country], 
	x = "year", y = "gdpPercap",title = "GDP per Capita")
col1.plotly_chart(fig,use_container_width = True)

fig = px.line(df[df['country'] == country], 
	x = "year", y = "pop",title = "Population Growth")
col2.plotly_chart(fig,use_container_width = True)

