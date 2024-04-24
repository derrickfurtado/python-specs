"""Script to seed the database"""

import os, json, pdb
from random import choice, randint
from datetime import datetime

import crud, model, server

os.system("dropdb ratings")                                     ### dropdb from CLI
os.system("createdb ratings")                                   ### createdb from CLI

model.connect_to_db(server.app)                                 ### launch server
model.db.create_all()                                           ### create all blank tables


with open('data/movies.json') as file:                          ### loading data from JSON file
    movie_data = json.loads(file.read())

movies_in_db = []                                               ### create empty list    

for movie in movie_data:                                        ### loop through movie_data list
    title = movie["title"]
    description = movie["overview"]
    img_url = movie["poster_path"]

    format = "%Y-%m-%d"
    release_date = datetime.strptime(movie["release_date"], format)             ### convert date string to date format

    new_movie = crud.create_movie(title, description, release_date, img_url)    ### create new_movie each loop    

    model.db.session.add(new_movie)                           ### add new movie to session
    movies_in_db.append(new_movie)                              ### add new movie to list

model.db.session.commit()                               ### commit movies


with open('data/actor_list.json') as file:
    actor_list = json.loads(file.read())


actor_queue = []
for actor in actor_list:                                ### seed cast_table
    for movie in movie_data:
        movie_title = movie["title"]
        if movie_title in actor:
            actor_info = actor[movie_title]
            first_name = actor_info[0]["1"][0][0]
            last_name = actor_info[0]["1"][0][1]
            full_name = f"{first_name} {last_name}"
            bio = actor_info[0]["1"][0][3]
            format = "%B %d, %Y"
            dob = datetime.strptime(actor_info[0]["1"][0][2], format)

            formatted_dob = datetime(dob.year, dob.month, dob.day)
            new_actor = crud.Cast(full_name, formatted_dob, bio)
            actor_queue.append(new_actor)


cleaned_list = {actor.full_name: actor for actor in actor_queue}.values()
model.db.session.add_all(cleaned_list)
model.db.session.commit()                    ###commit actors after cleaning out duplicates


for actor in actor_list:                                ### seed index_table
    for movie in movie_data:
        movie_title = movie["title"]
        if movie_title in actor:
            movie = model.Movie.query.filter_by(title = movie_title).all()
            movie_id = movie[0].id
            
            first_name = actor[movie_title][0]["1"][0][0]
            last_name = actor[movie_title][0]["1"][0][1]
            full_name = f"{first_name} {last_name}"
            actor = model.Cast.query.filter_by(full_name = full_name).all()
            actor_id = actor[0].id
            
            new_index = crud.Cast_Film_Index(actor_id, movie_id)
            model.db.session.add(new_index)

        else:
            pass


model.db.session.commit()




print("🚨🚨 Ratings Database has been reseeded 🚨🚨")