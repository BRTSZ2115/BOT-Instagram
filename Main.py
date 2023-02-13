from instagrapi import Client

#dane logowaina
username = ""
password = ""

#logowanie
client = Client()
client.login(username, password)

#funkcja lajkowania po hashtagu
def hashatag_like(hashtag, liczba):
         medias = client.hashtag_medias_recent(hashtag, liczba)
         for i, media in enumerate(medias):
             client.media_like(media.id)
             print(f"Polajkowany post nr {i + 1} z hashtagu")


#funkcja followowania obserwujacych konkretnego profilu
def user_followers_like(profil, liczba):
    profil_id = client.user_id_from_username(profil)
    medias = client.search_followers(profil_id, liczba)
    for i, media in enumerate(medias):
        nazwa = media.username
        user_id = client.user_id_from_username(nazwa)
        client.user_follow(user_id)
        print(f"followujesz profil {nazwa}")

#funkcja komentowania po hashtagu

#funkcja komentowania najnowszego postu obserwujacych konkretnego profilu





