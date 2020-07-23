networkx utility


Code snippets (repetitive tasks):
	- logging
	- pathlib
	- readme.py
	- source python script


```python
import pathlib
cur = pathlib.Path('.')

# Generate links to subdirectory
links = []
for fp in cur.rglob('./*.html'):
	if fp.parent.name != 'eval': continue
	link_name = fp.stem.replace("Evaluate_combined_measure_model3-", "Eval-model-")
	link = f"- [{link_name}]({fp})"
	links.append(link)
links.sort()
links_str = '\n'.join(l for l in links)

readme = f"""
## Markdown content

{links_str}
"""

with open('README.md', 'w') as f:
	f.write(readme)
```