import requests
import app_db

def get_movie_by_genre(genre_id):
    url=f'https://www.moviesapi.ir/api/v1/genres/{genre_id}/movies'
    response=requests.get(url)


    if response.status_code!=200:

        return"ERROR"
    else:
        data=response.json()
        title={'title'}
        poster={'poster'}
        genre={'genre'}
        return data,title,poster,genre


def get_movie_by_page(page):
    url=f'https://www.moviesapi.ir/api/v1/movies?page={page}'

    response=requests.get(url)

    if response.status_code!=200:
        return "ERROR"
    
    else:
        data=response.json()
        title={'title'}
        poster={'poster'}
        genre={'genre'}
        return data,title,poster,genre







if __name__=="__main__":
    result=get_movie_by_genre(genre_id=1),get_movie_by_page(page=1)
    result2=app_db.insert_list_of_movies(movies_list='')
    print(result,result2)

