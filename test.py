# from visualizations import util
# from visualizations.visualizations import visual_content_prod_country, visual_day_activity, visual_map_prod_country, visual_top_ten_genre, visual_top_ten_timeline, visual_top_ten_view, visual_viewing_timeline
# from icecream import ic

# path = 'csv_files/NetflixViewingHistory.csv'

# df = util.load_csv_file(path)
# ic('Load success')
# util.split_title(df)
# util.split_date(df)
# ic(util.make_day_categorical(df))
# ic('Split success')
# #genres, movie_countries = util.get_imdb_genre_and_country(df)
# #countries = util.get_country_list(movie_countries=movie_countries)
# #ic(util.make_genre_column(df,genres))
# ic('got info')
# #ic(visual_content_prod_country(countries))
# ic(visual_day_activity(df))
# #visual_map_prod_country(countries)
# #visual_top_ten_genre(df)
# visual_top_ten_view(df)
# visual_viewing_timeline(df)
# visual_top_ten_timeline(df)
# ic('info viewed')
# #print(df.head())