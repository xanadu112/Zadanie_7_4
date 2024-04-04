import random
from datetime import date

class Movie():
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.num_play = 0

    def play(self, another_play=1):
        self.num_play += another_play
    
    def __str__(self):
        return f'{self.title} ({self.year})'

class Series(Movie):
    def __init__(self, num_episode, num_season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_episode = num_episode
        self.num_season = num_season
    
    def __str__(self):
        return f'{self.title} S{self.num_season:02d} E{self.num_episode:02d}'
    

def get_movies(lib):
    return get_onetype(lib, Movie)
    
def get_series(lib):
    return get_onetype(lib, Series)        

def get_onetype(lib, onetype):
    lib_only_onetype = [i for i in lib if type(i) == onetype]
    return sorted(lib_only_onetype, key=lambda p: p.title)              

def search(search_title, lib):
    found_title = [i for i in lib if search_title == i.title]
    return found_title

def generate_views(lib):
    rnd_mov = random.choice(lib)
    rnd_mov.play(another_play = random.choice(range(1, 101)))

def ten_generate_views(lib):
    for j in range(10):
        generate_views(lib)

def top_titles(lib, num_top=3):
    top_list = sorted(lib, key=lambda q: q.num_play, reverse=True)
    return top_list[:num_top]
    

if __name__ == "__main__":
    print("Biblioteka filmów\n")

    movie_1 = Movie(title="The Wild Bunch", year="1969", genre="Western")
    movie_2 = Movie(title="Duel", year="1971", genre="Thriller")
    movie_3 = Movie(title="The Exorcist", year="1973", genre="Horror")
    movie_4 = Movie(title="The Caine Mutiny Court-Martial", year="2023", genre="War Drama")
    movie_5 = Movie(title="Gladiator", year="2000", genre="Historical Drama")
    movie_6 = Movie(title="The Sound and the Fury", year="1959", genre="Drama")
    movie_7 = Movie(title="From Here to Eternity", year="1953", genre="War Movie")
    movie_8 = Movie(title="The Thin Red Line", year="1998", genre="War Drama")
    movie_9 = Movie(title="Citizen Kane", year="1941", genre="Drama")
    movie_10 = Movie(title="Ordet", year="1955", genre="Drama")
    series_1 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=1, num_season=1)
    series_2 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=2, num_season=1)
    series_3 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=3, num_season=1)
    series_4 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=4, num_season=1)
    series_5 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=5, num_season=1)
    series_6 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=6, num_season=1)
    series_7 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=7, num_season=1)
    series_8 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=8, num_season=1)
    series_9 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=9, num_season=1)
    series_10 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=10, num_season=1)
    series_11 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=11, num_season=1)
    series_12 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=12, num_season=1)
    series_13 = Series(title="Knight Rider", year="1982", genre="Action", num_episode=13, num_season=1)
    series_14 = Series(title="Knight Rider", year="1983", genre="Action", num_episode=14, num_season=1)
    series_15 = Series(title="Knight Rider", year="1983", genre="Action", num_episode=15, num_season=1)
    series_16 = Series(title="Knight Rider", year="1983", genre="Action", num_episode=16, num_season=1)
    series_17 = Series(title="Knight Rider", year="1983", genre="Action", num_episode=17, num_season=1)
    series_18 = Series(title="Knight Rider", year="1983", genre="Action", num_episode=18, num_season=1)
    series_19 = Series(title="Knight Rider", year="1983", genre="Action", num_episode=19, num_season=1)
    series_20 = Series(title="Knight Rider", year="1983", genre="Action", num_episode=20, num_season=1)
    series_21 = Series(title="Knight Rider", year="1983", genre="Action", num_episode=21, num_season=1)
    series_22 = Series(title="Knight Rider", year="1983", genre="Action", num_episode=22, num_season=1)
    series_23 = Series(title="Halo", year="2022", genre="Sci-Fi", num_episode=1, num_season=1)
    series_24 = Series(title="Halo", year="2022", genre="Sci-Fi", num_episode=2, num_season=1)
    series_25 = Series(title="Halo", year="2022", genre="Sci-Fi", num_episode=3, num_season=1)
    series_26 = Series(title="Halo", year="2022", genre="Sci-Fi", num_episode=4, num_season=1)
    series_27 = Series(title="Halo", year="2022", genre="Sci-Fi", num_episode=5, num_season=1)
    series_28 = Series(title="Halo", year="2022", genre="Sci-Fi", num_episode=6, num_season=1)
    series_29 = Series(title="Halo", year="2022", genre="Sci-Fi", num_episode=7, num_season=1)
    series_30 = Series(title="Halo", year="2022", genre="Sci-Fi", num_episode=8, num_season=1)
    series_31 = Series(title="Halo", year="2022", genre="Sci-Fi", num_episode=9, num_season=1)
    series_32 = Series(title="Halo", year="2022", genre="Sci-Fi", num_episode=10, num_season=1)

    lib_mov = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6, movie_7, movie_8, movie_9, movie_10, series_1, series_2, series_3, series_4,
              series_5, series_6, series_7, series_8, series_9, series_10, series_11, series_12, series_13, series_14, series_15, series_16,
              series_17, series_18, series_19, series_20, series_21, series_22, series_23, series_24, series_25, series_26, series_27, series_28,
              series_29, series_30, series_31, series_32]
    
    for i in lib_mov:
        print(i)

    ten_generate_views(lib_mov)

    print("\nNajpopularniejsze filmy i seriale dnia", date.today().strftime("%d.%m.%Y"))

    top = top_titles(lib_mov)
    for i in top:
        print(f'{i}: number of plays: {i.num_play}')

    