# PyDaRUS

PyDaRUS is the Python library used to programatically interact with the Dataverse installation DaRUS. It offers the creation and upload of datasets as well as download and editing of existing entries. In addition, PyDaRUS offers the export to and import from JSON/XML/YAML. 

## Description

Will be written soon ...

## Getting Started

### Dependencies

* easyDataverse
* fastapi
* uvicorn
* pydantic
* jinja2
* pyDataverse
* pandas
* pyaml

### Installing

In order to install pyDaRUS either use the python package manager pip

```python3 -m pip install pyDaRUS```

or build it from source 

```
git clone https://github.com/JR-1991/pyDaRUS.git
cd pyDaRUS
python3 setup.py install
```

### Executing program

The following example will demonstrate how to use pyDaRUS. Essentially, the workflow can be summarize as follows:

1. Initialize the ```Dataset``` container.
2. Choose the metadatablocks to which you'd like to write and initialize these.
3. Enter your data to the metadatablock's fields. Use the ```add_XYZ```-methods to add compound/objects.
4. Add the metadatablocks to the ```Dataset``` object and upload it to DaRUS.

Please note, that the interface ```easyDataverse``` will infer the ```DATAVERSE_URL``` as well as ```DATAVERSE_API_TOKEN``` from your environment variables. Thus, please make sure these are available at runtim.


## Creating and uploading a dataset to Dataverse

```python
from pyDaRUS import Citation, Process, Dataset
from pyDaRUS.metadatablocks.citation import SubjectEnum, IdentifierScheme
```


```python
# Initialize Dataset and metadatablocks
dataset = Dataset()

# Initialize metadatablocks you like to use
citation = Citation()
process = Process()
```


```python
# Fill in citation relevant fields (TODO: Make sure these are required)
citation.title = "Some Title"
citation.subject = [SubjectEnum.chemistry]

citation.add_description(text="Some description", date="1991")
citation.add_author(name="Jan Range", affiliation="SimTech")
citation.add_contact(name="Jan Range", email="jan.range@simtech.uni-stuttgart.de")
```


```python
# Fill in process relevant fields
process.add_processing_methods(name="Some Process", parameters="Param1, Param2")
process.add_method_parameters(name="Param1", value=10)
process.add_method_parameters(name="Param2", textual_value="Textual")
```


```python
# Add each metadatablock to the dataset
dataset.add_metadatablock(citation)
dataset.add_metadatablock(process)
```


```python
# Finally, upload the dataset to dataverse
# URL and API_TOKEN will be inferred from the env
p_id = dataset.upload(dataverse_name="my_dataverse", filenames=["pyDaRUS"])
```

    Dataset with pid 'doi:10.18419/darus-2447' created.


## Download, edit and update a dataset from Dataverse


```python
# Retrieve a dataset from Dataverse by using the given DOI/PID
dataset = Dataset.from_dataverse_doi(p_id)

# Edit the dataset
dataset.process.add_method_parameters(name="Param3", symbol="p3", unit="kg", value=100.0)
dataset.citation.add_author(name="Max Mustermann", affiliation="SimTech")
```

```python
# In order to update the dataset on Dataverse use the dataset.update method
# Unfortunately you have to provide your contact again
# since DaRUS wont include mails when fetchin an entry

dataset.update(contact_name="Jan Range", contact_mail="jan.range@simtech.uni-stuttgart.de")
```


## Help

Help will arrive soon ...

## Authors

Contributors names and contact info

Jan Range

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Will be written soon ...