# Jupyter Notebook

## Manipulate Notebooks from the Command Line

See [StackOverflow](https://stackoverflow.com/questions/35545402/how-to-run-an-ipynb-jupyter-notebook-from-terminal).

- Execute notebook and save results

    ```bash
    jupyter nbconvert --execute --to notebook --inplace notebook.ipynb
    ```

- Export notebook to `.py`
    
    ```bash
    jupyter nbconvert --to python notebook.ipynb
    ```

- Export notebook to `.html`

    (Convert without execution)  
    ```bash
    jupyter nbconvert --to html notebook.ipynb
    ```
    
    (Execute before conversion, with no execution time limit)  
    ```bash
    jupyter nbconvert --execute --to html --ExecutePreprocessor.timeout=-1 notebook.ipynb
    ```
    
    (Execute before conversion and set output dir to `./html`)  
    ```bash
    jupyter nbconvert --execute --to html --ExecutePreprocessor.timeout=-1 --output-dir='./html' notebook.ipynb
    ```


## Programmatically Create Jupyter Notebooks (with different parameters)

Specify parameters in the first cell of the source jupyter notebook (`source.ipynb`):

![](img/param-in-notebook.png)

You can then use [nbparameterise](https://github.com/takluyver/nbparameterise) to programmatically replace input values in a notebook before running it.

```{admonition} [set-notebook-params.py](https://github.com/liao961120/pynote/blob/master/scripts/set-notebook-params.py)
:class: dropdown

````python
import os
import nbformat
from nbparameterise import extract_parameters, parameter_values, replace_definitions


# Extract parameters in source notebook
with open("source.ipynb") as f:
	nb = nbformat.read(f, as_version=4)
orig_parameters = extract_parameters(nb)


# Parameters to replace
model_names = [
	'model3-small-search-space4', 'model3-small-search-space5'
]

# Create new notebooks with replaced parameters
for name in model_names:
    print("Running for model:", name)

    # Update the parameters
    params = parameter_values(orig_parameters, model_name=name)
    new_nb = replace_definitions(nb, params, execute=False)

    # Save
    new_nb_fp = f"new_notebook_with_param_{name}.ipynb"
    with open(new_nb_fp, 'w') as f:
        nbformat.write(new_nb, f)
    
    # Execute new notebook
    os.system(f"jupyter nbconvert --execute --ExecutePreprocessor.timeout=-1 --to notebook --inplace {new_nb_fp}")
    # Convert to html
    os.system(f"jupyter nbconvert --output-dir='./html' --to html {new_nb_fp}")
````
```