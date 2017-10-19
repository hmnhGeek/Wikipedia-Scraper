import wikipedia as wiki
import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument('keyword', type = str, help = "Search query!!")
parser.add_argument('--loc', type = str, action = 'store', dest = 'l', help = "Saving location!!")
parser.add_argument('-i', action = 'store_true', help = "Download image")

args = parser.parse_args()

if args.l:
    wiki.query(args.keyword, args.l, args.i)
else:
    wiki.query(args.keyword, download_image = args.i)
