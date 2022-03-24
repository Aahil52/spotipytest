import os
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def toggle_playback(is_playing, device_id=None):
    match is_playing:
        case False:
            sp.start_playback(device_id=device_id)
        case True:
            sp.pause_playback(device_id=device_id)

def cycle_repeat(repeat_state, device_id=None):
    match repeat_state:
        case 'off':
            sp.repeat('context', device_id=device_id)
        case 'context':
            sp.repeat('track', device_id=device_id)
        case 'track':
            sp.repeat('off', device_id=device_id)

CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = 'https://localhost/player'
SCOPE = 'user-read-playback-state,user-modify-playback-state'
DEVICE_ID = '0bb4d726656ae60024e260e346f6dedf33f2348d'

while True:
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))

        while True:
            curr_plbk = sp.current_playback(market='US')
            if curr_plbk == None:
                # Assume these values
                curr_plbk = {'is_playing': False, 'repeat_state': 'off', 'shuffle_state': False}
            
            usercmd = input('))) ')

            match usercmd:
                case 'toggle':
                    toggle_playback(curr_plbk['is_playing'], device_id=DEVICE_ID)
                case 'next':
                    sp.next_track(device_id=DEVICE_ID)
                case 'previous':
                    sp.previous_track(device_id=DEVICE_ID)
                case 'shuffle':
                    sp.shuffle(not curr_plbk['shuffle_state'], device_id=DEVICE_ID)
                case 'repeat':
                    cycle_repeat(curr_plbk['repeat_state'], device_id=DEVICE_ID)
                case 'track':
                    uri = 'spotify:track:' + input('ID: ')
                    sp.add_to_queue(uri, device_id=DEVICE_ID)
                case 'album':
                    context_uri = 'spotify:album:' + input('ID: ')
                    sp.start_playback(device_id=DEVICE_ID, context_uri=context_uri)
                case 'playlist':
                    context_uri = 'spotify:playlist:' + input('ID: ')
                    sp.start_playback(device_id=DEVICE_ID, context_uri=context_uri)    
                case 'current':
                    pprint(curr_plbk)
    except Exception as e:
        print(e)
        pass