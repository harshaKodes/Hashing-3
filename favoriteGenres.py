from collections import defaultdict
from typing import Dict, List

def favoriteGenres(userToSongs: Dict[str, List[str]], genreTosongs: Dict[str, List[str]]) -> Dict[str, List[str]]:
    
    #userToGenres
    result = {}

    #songToGenre
    songToGenre = {}

    for genre, songs in genreTosongs.items():

        for song in songs:
            songToGenre[song] = genre

    #iterate over userToSongs
    for user, songs in userToSongs.items():
        
        #genre frequency dict for a user
        genreFrequency = defaultdict(int)

        freqMax = 0

        #user's songs
        for song in songs:
            genre = songToGenre.get(song)
            #update genre frequnecy and max frequency
            if genre:
                genreFrequency[genre] += 1
                freqMax = max(freqMax, genreFrequency[genre])

        # intiate genre value to be empty list
        result[user] = []

        # add only maximum frequnecy genres to result
        for genre, freq in genreFrequency.items():
            if freq == freqMax:
                result[user].append(genre)
                
    #output
    return result

def main():
    # user to song map
    user_songs = {
        "Harsha": ["Tum ho", "Jannatein kahan", "Nainowale ne", "Fakira", "Ajab si"],
        "Sarat": ["Nainowale", "Fakira", "Mona Gasolina"]
    }

    # genre to song map
    song_genres = { 
        "MohitChauhan": ["Tum ho"],
        "KK": ["Jannatein kahan", "Ajab si"],
        "NeetiMohan": ["Nainowale", "Fakira", "Mona Gasolina"],

    }

    answer = favoriteGenres(user_songs, song_genres)

    for user, genres in answer.items():
        print(f"{user}: {' '.join(genres)}")

if __name__ == "__main__":
    main()

    

            
            



