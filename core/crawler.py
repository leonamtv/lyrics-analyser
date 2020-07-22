from core.agents import agents
from core.util import clean_string

from bs4 import BeautifulSoup
from tqdm import tqdm

import pandas as pd

import requests
import random
import os

def parse_page ( artist ) :
    
    requester = requests.session()
    requester.headers.update({ 'user-agent' : random.choice(agents)})
    
    try:
        request = requester.get( artist.link )
    except requests.exceptions.ChunkedEncodingError:
        print('Error while requesting page')
    
    soup = BeautifulSoup( request.content, 'html.parser' )
    
    table_of_contents = soup.findAll('div', { 'class' : 'layout_d' })
    
    requester.close()

    if len(table_of_contents) > 0:
        music_links = table_of_contents[0].select('div[data-name]')
        if not os.path.isdir ( './dump/csv' ):
            print('not an dir')
            os.makedirs ( './dump/csv' )
        header = ''
        file_path = './dump/csv/' + artist.name.replace(' ', '-').lower() + '.csv'
        if not os.path.isfile ( file_path ):
            header = 'Nome;Link\n'
        lyrics_file = open(file_path, 'a')
        lyrics_file.write(header)
        for item in tqdm(music_links):
            links = item.findAll('a')
            nome  = links[0].text.strip('lyrics').strip('lyric')
            link  = links[0]['href']
            lyrics_file.write(nome + ";" + link + "\n")
        lyrics_file.close()
        return file_path

def parse_csv ( artist, path ):
    
    file_path = path

    if not '.csv' in path:
        if not os.path.isfile ( path + '.csv' ):
            raise Exception('Arquivo não existe')
        else :
            file_path += '.csv'
    else :
        if not os.path.isfile ( path ):
            raise Exception('Arquivo não existe')

    links = pd.read_csv(file_path, sep=';')

    artist_lyrics_path = './dump/lyrics/' + artist.name.capitalize().replace(' ', '')

    if not os.path.isdir ( artist_lyrics_path ) :
        os.makedirs ( artist_lyrics_path )

    print('Baixando letras...')

    for _, row in tqdm(links.iterrows()):

        lyric_file_name = os.path.join( artist_lyrics_path, clean_string(row['Nome']).replace(' ', '') + '.txt' )

        if os.path.isfile ( lyric_file_name ):
            continue

        requester = requests.session()
        requester.headers.update({ 'user-agent' : random.choice(agents)})

        try:
            request = requester.get( row['Link'] )
        except requests.exceptions.ChunkedEncodingError:
            print('Error while requesting page')
        
        soup = BeautifulSoup( request.content, 'html.parser' )
        lyrics = soup.findAll('div', { 'class' : 'contentbox' })

        if len(lyrics) > 0 :

            lyric = lyrics[0].text
            lyric_file = open( lyric_file_name, 'w' )
            lyric_file.write(lyric)
            lyric_file.close()
        
        requester.close()

    return artist_lyrics_path

    


    