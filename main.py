import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Credenciales de tu aplicación
client_id = 'd88377feaef54b45acb0d1d8941efcf2'
client_secret = '2e771745945c4ba4828a1dd357f40f93'
redirect_uri = 'http://localhost:8888/callback'

# Alcance de los permisos
scope = 'user-library-read'

# Autenticación y obtención del token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

results = sp.search(q='album:Abbey Road artist:The Beatles', type='album')
albums = results['albums']['items']

for album in albums:
    print(album['name'],album['release_date'])

#results = sp.search(q='Imagine Dragons', limit=10)
#for idx, item in enumerate(results['tracks']['items']):
#    print(f"{idx + 1}. {item['name']} – {item['artists'][0]['name']}")


# Ejemplo de uso: Obtener y mostrar las canciones guardadas del usuario
#results = sp.current_user_saved_tracks()
#for idx, item in enumerate(results['items']):
#   track = item['track']
#    print(f"{idx + 1}. {track['artists'][0]['name']} – {track['name']}")
