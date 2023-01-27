from typing import Dict

import os
import json

from functions.parsing import parse_post
from functions.helpers import build_year_month

def build_index_handler() -> Dict:
    """
    This function indexes all of the posts in the content/posts folder and indexes them into a dictionary and writes them to disk
    
    Returns:
        Dict - the dictionary of posts and the indices/facets
    """
    index = {
        'ordering':{
            'weeks_asc':[],
            'weeks_desc':[]
        },
        'facets': {
            'years':{},
            'weeks':{},
            'months':{},
            'tags':{},
        },
        'posts':{}
    }
    post_directory = 'content/posts'
    posts = [filename for filename in os.listdir(post_directory) if not '.DS_Store' in filename]
    for filename in posts:
        with open(f'{post_directory}/{filename}') as post_file:
            raw_post = post_file.read()
            post = parse_post(raw_post)

        slug = post['metadata']['slug']
        year = int(post['metadata']['year'])
        month = int(post['metadata']['month'])
        month_index = build_year_month(year, month)
        week = int(post['metadata']['week'])
        index['posts'][slug] = post
        if year not in index['facets']['years']:
            index['facets']['years'][year] = []
        index['facets']['years'][year].append(slug)
        if month_index not in index['facets']['months']:
            index['facets']['months'][month_index] = []
        index['facets']['months'][month_index].append(slug)
        index['facets']['weeks'][week] = slug
        for tag in post['metadata']['tags']:
            if tag not in index['facets']['tags']:
                index['facets']['tags'][tag] = []
            index['facets']['tags'][tag].append(slug)

    weeks = sorted([key for key in index['facets']['weeks']])

    index['ordering']['weeks_asc'] = [index['facets']['weeks'][week] for week in weeks]
    index['ordering']['weeks_desc'] = [index['facets']['weeks'][week] for week in reversed(weeks)]

    with open('content/index.json', 'w') as index_file:
        json.dump(index, index_file)
    return index