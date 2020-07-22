import pandas as pd
import tensorflow as tf

import requests
import random
import pickle
import os

from core.agents import agents
from core.util import clean_string, to_ignore

from tqdm import tqdm
from bs4 import BeautifulSoup
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

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
        success = False

        while not success:
            try:
                request = requester.get( row['Link'])
                success = True
            except requests.exceptions.ChunkedEncodingError:
                print('Error while requesting page')
                continue                
            except requests.exceptions.ConnectionError:
                print('Connection error')
                requester = requests.session()
                requester.headers.update({ 'user-agent' : random.choice(agents)})
        
        soup = BeautifulSoup( request.content, 'html.parser' )
        lyrics = soup.findAll('div', { 'class' : 'contentbox' })

        if len(lyrics) > 0 :

            lyric = lyrics[0].text
            lyric_file = open( lyric_file_name, 'w' )
            lyric_file.write(lyric)
            lyric_file.close()
        
        requester.close()

    return artist_lyrics_path

def tokenize_lyrics ( artist, path ):

    tokenizer_dump_path = './dump/tokenizer/' + artist.name.capitalize().replace(' ', '')
    tokenizer_path = './dump/tokenizer/' + artist.name.capitalize().replace(' ', '') + '/tokenizer.pickle'

    if os.path.isfile(tokenizer_path):
        with open(tokenizer_path, 'rb') as handle:
            tokenizer = pickle.load(handle)
    else:
        tokenizer = Tokenizer(num_words=100)

    for file_path in os.listdir(path):
        file_content = open( os.path.join( path, file_path ), 'r').read()
        tokenizer.fit_on_texts([ file_content ])
    
    words = tokenizer.word_index

    if not os.path.isdir( tokenizer_dump_path ):
        os.makedirs ( tokenizer_dump_path )

    if not os.path.isfile(tokenizer_path):
        with open(tokenizer_path, 'wb') as handle:
            pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)    

    dump_text = ''

    for word in words:
        if word not in to_ignore:
            dump_text += word + '\n'

    output_file_name = './output/' + artist.name.capitalize().replace(' ', '') + '.txt'

    if not os.path.isfile ( output_file_name ):
        with open(output_file_name, 'w') as output_file:
            output_file.write(dump_text)
        print('File written')

    return output_file_name



    