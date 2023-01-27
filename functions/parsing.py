from typing import Dict

import markdown
import toml

from functions.helpers import slugify

def parse_post(post:str) -> Dict:
    """
    This function takes a post, parses the TOML formatted metadata and marks up the Markdown format post
    
    Args:
        post (str) - the string representation of the file

    Returns:
        dict - the markdown version of the post
    """
    split_chars = '==='
    processed_post = {
        'metadata':{},
        'content':''
    }
    if split_chars in post:
        components = post.split(split_chars)
        processed_post['metadata'] = toml.loads(components[0])
        if ',' in processed_post['metadata']['tags']:
            tags = processed_post['metadata']['tags'].split(',')
        else:
            tags = [processed_post['metadata']['tags']]
        title = processed_post['metadata']['title']
        week = processed_post['metadata']['week']
        slug_text = f'Week {week}:{title}'
        processed_post['metadata']['slug'] = slugify(slug_text)
        processed_post['metadata']['tags'] = [slugify(tag.strip()) for tag in tags]
        
        processed_post['content'] = markdown.markdown(components[1])
    else:
        print ('ERROR')
    return processed_post
