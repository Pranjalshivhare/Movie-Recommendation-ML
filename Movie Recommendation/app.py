

import streamlit as st
import pickle
import difflib
import requests



def recommend(movie):
    list_of_all_title = movies_list['title'].tolist()
    find_close_match = difflib.get_close_matches(movie, list_of_all_title)
    close_match = find_close_match[0]
    index_of_movie = movies_list[movies_list.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    st.write('Movies suggested for you : ')
    i = 1
    for movie in sorted_similar_movies:
        index = movie[0]
        # Movie Poster
        title_for_index = movies_list[movies_list.index == index]['title'].values[0]
        if(i<=10):
            st.write(index)

            # st.write(i)
            st.write(i, title_for_index)
            i = i + 1


# def recommend(movie):
#     list_of_all_title = movies_list['title'].tolist()
#     find_close_match = difflib.get_close_matches(movie, list_of_all_title)
#     close_match = find_close_match[0]
#     index_of_movie = movies_list[movies_list.title == close_match]['index'].values[0]
#     similarity_score = list(enumerate(similarity[index_of_movie]))
#     sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
#
#     print('Movies suggested for you : \n')
#     i = 1
#     recommend_movies = []
#     for movie in sorted_similar_movies:
#         index = movie[0]
#         title_for_index = movies_list[movies_list.index == index]['title'].values[0]
#         if (i < 10):
#             recommend_movies.append(title_for_index)
#             # print(i, '.', title_for_index)
#             i = i + 1

movies_list = pickle.load(open('movies.pkl','rb'))
# movies_list = movies_list['title'].values


similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommendation System")


selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies_list['title']
)

if st.button('Click Me'):
    recommend(selected_movie_name)
    # recommendations = recommend(selected_movie_name)
    # for i in recommendations:
    #     st.write(selected_movie_name)










#pip freeze > requirements.txt




