from core.crawler import parse_page, parse_csv, tokenize_lyrics
from core.artist import Artist
from core.analyser import plot_pie_chart 

artist = Artist('Pink Floyd', 'https://www.letssingit.com/pink-floyd-kj2mq/lyrics')
# parse_page(artist)
# parse_csv(artist, './dump/csv/pink-floyd.csv')
# path_to_dumped_output = tokenize_lyrics(artist, './dump/lyrics/Pinkfloyd')
path_to_dumped_output = './output/Pinkfloyd.txt'
plot_pie_chart(path_to_dumped_output, 50)