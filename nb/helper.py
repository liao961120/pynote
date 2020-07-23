from myst_nb import glue
from IPython.display import display, Markdown

def full_url(rel_path_to_nb, repo='https://github.com/liao961120/pynote'):
    return f"{repo}/{rel_path_to_nb}"

# Not working now #
def embed_py(path, id_=None):
    content = read_text(path, pre_sty='```python\n', post_sty='\n```')
    if id_ is None:
        glue(str(path), content)
    else:
        glue(id_, content)


def read_text(path, pre_sty, post_sty):

    with open(path) as fh:
        content = pre_sty + fh.read().strip() + post_sty
        
    return content