from daytflix.DaytFlix import DaytFlix
import argparse


parser = argparse.ArgumentParser()
daytFlix = DaytFlix()

def search():
    parser.add_argument('--q')
    parser.add_argument('--p')
    parser.add_argument('--l')
    args = parser.parse_args()
    
    query = args.q
    page = args.p
    limit = args.l

    if not args.q:
        query = '*'
    if not args.p:
        page = 1
    if not args.l:
        limit = 24

    daytFlix.search(query, page, limit)
