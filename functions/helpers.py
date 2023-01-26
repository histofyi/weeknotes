def slugify(string:str) -> str:
    """
    This function creates a slug version of a specified word or phrase
    
    Args:
        string (str): the string to be slugified

    Returns
        str - the slugified version of the string
    """
    slug_char = '_'
    to_replace = [' ','-','.',',','[',']','{','}','(',')','/','\\','*',':']
    for replace_me in to_replace:
        if replace_me in string:
            string = string.replace(replace_me, slug_char)
    return string.lower()

