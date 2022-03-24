import os
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = 'https://localhost/player'
SCOPE = 'user-read-playback-state,user-modify-playback-state'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))

res = sp.current_playback(market='US')
pprint(res)
if res == None:
     # Assume these values
    res = {'is_playing': False, 'repeat_state': 'off', 'shuffle_state': False}
    pprint(res)