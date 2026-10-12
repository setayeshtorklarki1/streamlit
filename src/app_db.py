import sqlite3

DB_name='Moviesapiinfo.db'
def init_db():
    conn=sqlite3.connect(DB_name)
    conn.close()

init_db()

def create_table(DB_name,table_name='MoviesData'):
    query=f'''CREATE TABLE IF NOT EXISTS {table_name}
 (id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT,
 year  INTEGER,
 imdb_rating REAL,
 genres TEXT,
 poster TEXT)'''
    conn=sqlite3.connect(DB_name)
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()    

create_table(DB_name,table_name='MoviesData')

def insrt_record(title,year,imdb_rating,genres,poster):
    query=f'''INSERT INTO MoviesData (title,year,imdb_rating,genres,poster)
    
    VALUES(?,?,?,?,?)
    
    '''
    conn=sqlite3.connect(DB_name)
    cursor=conn.cursor()
    cursor.execute(query,(title,year,imdb_rating,genres,poster))
    conn.commit()
    conn.close()

###############

# insrt_record('Inception',2001,7.8,'Action , Drama','http://test.com')

 
def insert_list_of_movies(movies_list):
    for item  in movies_list:
        
        title=item['title']
        
        year=item['year']
        
        imdb_rating=item['imdb_rating']
        
        genres=','.join(item['genres'])
        
        poster=item['poster']
        
        insrt_record(title,year,imdb_rating,genres,poster)
    
    return f'{len(movies_list)} Record Inserted Successfully'


# movies_list=[{"title":'God Futher',"year":2020,'imdb_rating':7.8,"genres":'Action , Drama','poster':'http://test.com'},
             
#              {'title':"Dark Night","year":2004,'imdb_rate':6.3,"genres":"Action,Mystory",'poster':'http://test.com'}]


# print(insert_list_of_movies(movies_list))
