import streamlit as st
import plotly.express as px
import pickle

countries=pickle.load(open('countries.pkl','rb'))


st.title('World Covid-19')
st.header('Track Covid-19 Cases')
st.subheader('Date: 03 Sep 2021')


selected_criteria = st.selectbox(
'Select a criteria',
[i for i in countries.columns[:-1]])

fig=px.pie(countries,values=[sum(countries[countries['Continent']=='North America'][selected_criteria]),
                      sum(countries[countries['Continent']=='Asia'][selected_criteria]),
                      sum(countries[countries['Continent']=='South America'][selected_criteria]),
                      sum(countries[countries['Continent']=='Europe'][selected_criteria]),
                      sum(countries[countries['Continent']=='Africa'][selected_criteria]),
                      sum(countries[countries['Continent']=='Australia/Oceania'][selected_criteria])],
            names=countries['Continent'].unique(),
            hole=0.5)
fig.update_layout( width=1000,
            height=1000,

title_text='Covid ' + str(selected_criteria) + " Cases by Continents",

annotations=[dict(text='September 03 2021', x=0.5, y=0.5, font_size=30, showarrow=False)])
fig.update_traces(textposition='inside', textinfo='percent+label')

st.container()
st.plotly_chart(fig,use_container_width=True)




selected_country = st.selectbox(
'Select a Country',
[i for i in countries.index])


fig2=px.pie(countries,values=[countries.loc[selected_country]['TotalRecovered'],countries.loc[selected_country]['ActiveCases'],countries.loc[selected_country]['TotalDeaths']],names=['TotalRecovered','Total ActiveCases','TotalDeaths'],
           color_discrete_sequence=px.colors.qualitative.G10_r,hole=0.5)
fig2.update_layout(title= str(selected_country)+' Covid Cases',annotations=[dict(text='September 03 2021', x=0.5, y=0.5, font_size=7, showarrow=False)],width=2000)




fig3=px.pie(countries,values=[countries.loc[selected_country]['NewRecovered'],countries.loc[selected_country]['NewCases'],countries.loc[selected_country]['NewDeaths']],names=['New-Recovered','New Confirmed Cases','New-Deaths'],
           color_discrete_sequence=px.colors.qualitative.G10_r,hole=0.5)
fig3.update_layout(title= str(selected_country)+' Daily Covid Cases',annotations=[dict(text='September 03 2021', x=0.5, y=0.5, font_size=7, showarrow=False)],width=2000)



col1,  col2 = st.columns([1,1])

with col1:
   st.plotly_chart(fig2,use_container_width=True)



with col2:
    st.plotly_chart(fig3, use_container_width=True)


selected_criteria_world = st.selectbox(
'Select a criteria for analysis',
[i for i in countries.columns[:-1]])

fig4=px.bar(countries,x=countries[countries[selected_criteria_world]>0][selected_criteria_world],
            y=countries[countries[selected_criteria_world]>0][selected_criteria_world].index,
            labels={"x":'No. of Cases',"y":'Countries','color':'% of ' + str(selected_criteria_world)},color=(countries[countries[selected_criteria_world]>0][selected_criteria_world]/sum(countries[selected_criteria_world]))*100)
fig4.update_layout( width=800,
            height=2000,
title_text="Covid " + str(selected_criteria_world) +" in the World")


st.container()
st.plotly_chart(fig4)



plz_select_criteria= st.selectbox(
'Select criteria',
[i for i in countries.columns[:-1]])



fig6=px.pie(countries,values=countries[plz_select_criteria],
            names=countries.index,
            hole=0.5)
fig6.update_layout( width=1000,
            height=1000,

title_text="Covid "+ str(plz_select_criteria),

annotations=[dict(text='September 03 2021', x=0.5, y=0.5, font_size=30, showarrow=False)])
fig6.update_traces(textposition='inside', textinfo='percent+label')

st.container()
st.plotly_chart(fig6,use_container_width=True)



