import streamlit as st
import app_db
import app_api

title=st.title('simple streamlit')

option=st.sidebar.selectbox('Enter Your Option:',('CALL MOVIE LIST BY PAGE','SHOW ALL MOVIES','CALL MOVIES BY GENRE'))

if option=='CALL MOVIE LIST BY PAGE':

      page_id=st.number_input('ENTER PAGE NUMBER:',min_value=1,max_value=25)
      result=app_api.get_movie_by_page(page_id)
      
      if st.button("SHOW MOVIE LIST"):
       
       if result!="ERROR":
           
           st.write(result)
       
       else:
         st.error('YOUR REQUEST CAN NOT BE SEND!!!')

if option=='CALL MOVIES BY GENRE':

   genre_id=st.number_input(('enter a genre id:'))

   result=app_api.get_movie_by_genre(genre_id)

   if st.button('SHOW MOVIES'):

    if result!='ERROR':

         st.write(result)

    else:
        st.error('YOUR REQUEST CAN NOT BE SEND!!!')     



