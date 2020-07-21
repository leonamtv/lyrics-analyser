from core.crawler import parse_page, parse_csv
from core.artist import Artist

# artist = Artist('Pink Floyd', 'https://www.letssingit.com/pink-floyd-kj2mq/lyrics')
# parse_page(artist)
parse_csv('./dump/csv/pink-floyd.csv')