import os
import nbformat
from nbparameterise import extract_parameters, parameter_values, replace_definitions


# Extract parameters in source notebook
with open("source.ipynb") as f:
	nb = nbformat.read(f, as_version=4)
orig_parameters = extract_parameters(nb)


# Parameters to replace
model_names = [
	'model3-small-search-space3', 'model3-small-search-space4'
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
