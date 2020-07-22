from core.crawler import parse_page, parse_csv, tokenize_lyrics
from core.artist import Artist

artist = Artist('Pink Floyd', 'https://www.letssingit.com/pink-floyd-kj2mq/lyrics')
# parse_page(artist)
# parse_csv(artist, './dump/csv/pink-floyd.csv')
tokenize_lyrics(artist, './dump/lyrics/Pinkfloyd')