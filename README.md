<h1 align="center">
  PyDaRUS
</h1>
<p align="center">PyDaRUS is the Python library used to programatically interact with the Dataverse installation DaRUS. It offers the creation and upload of datasets as well as download and editing of existing entries. In addition, it offers the export to and import from JSON/XML/YAML/HDF5. </p>


## 🚀 Getting Started

Get started with PyDaRUS by running the following command 

```
# Using PyPI
python -m pip install pyDaRUS
```

Or build by source
```
git clone https://github.com/JR-1991/pyDaRUS.git
cd pyDaRUS
python3 setup.py install
```

### 🚨 __Important note__

Currently the dependency __pyDataverse__ is not updated to work with the new Dataverse version **5.9** and will thus fail when data is uploaded. For this, use the fork provided that fixes the problem. In order to install, follow these instructions

```
pip install git+https://github.com/JR-1991/pyDataverse.git@0fcfcd3fbc6bf1aec869899f715a51dca25e91be
```

### ⚙️ Dependencies

* easyDataverse
* fastapi
* uvicorn
* pydantic
* jinja2
* pyDataverse
* pandas
* pyaml
* deepdish
* h5py

## 🐍 Example program

The following example will demonstrate how to use pyDaRUS. Essentially, the workflow can be summarized as follows:

1. Initialize the ```Dataset``` container.
2. Choose the metadatablocks to which you'd like to write and initialize these.
3. Enter your data to the metadatablock's fields. Use the ```add_XYZ```-methods to add compound/objects.
4. Add the metadatablocks to the ```Dataset``` object and upload it to DaRUS.

Please note, that the interface ```easyDataverse``` will infer the ```DATAVERSE_URL``` as well as ```DATAVERSE_API_TOKEN``` from your environment variables. Thus, please make sure these are available at runtim.

### Creating and uploading a dataset to Dataverse

```python
from pyDaRUS import Citation, Process, Dataset
from pyDaRUS.metadatablocks.citation import SubjectEnum, IdentifierScheme
```

```python
# Initialize Dataset
dataset = Dataset()

# Initialize metadatablocks you like to use
citation = Citation()
process = Process()
```


```python
# Fill in citation relevant fields
citation.title = "Some Title"
citation.subject = [SubjectEnum.chemistry]

# Use add function to append compound objects without
# having to import the corresponding class
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
# If given add files and directories
dataset.add_directory("Examples/dataset_upload/")
```


```python
# Finally, upload the dataset to dataverse
# URL and API_TOKEN will be inferred from the env
p_id = dataset.upload(dataverse_name="playground")
```

## Download and edit a dataset from Dataverse


```python
# Retrieve a dataset from Dataverse by using the given DOI/PID
dataset = Dataset.from_dataverse_doi(p_id, filedir="Examples/dataset_download/")

# Change a file
with open("Examples/dataset_download/test_file.txt", "w") as f:
    f.write("Has changed")
    
# Add new files
dataset.add_file(dv_path="nu_file.txt", local_path="Examples/dataset_download/nu_file.txt")

# Edit the dataset
dataset.process.add_method_parameters(name="Param3", symbol="p3", unit="kg", value=100.0)
dataset.citation.add_author(name="Max Mustermann", affiliation="SimTech")
```


```python
# Now to update the dataset on Dataverse use 'dataset.update'.
# Unfortunately you have to provide your contact again
# since DaRUS wont include mails when fetchin an entry

dataset.update(contact_name="Jan Range", contact_mail="jan.range@simtech.uni-stuttgart.de")
```


## Export dataset as YAML template and re-initialize

In addition to scripting, PyDaRUS offers the opportunity to initialize a dataset via a specific YAML file (JSON, XML and HDF5 will follow). Some application may require metadata that stays constent in the course of creation. Thus, such a YAML file can be used as a template to reduce overhead. In this exmaple, the file is generated using the ```yaml```-method found in the ```Dataset``` object.

```python
with open("MyDataset.yaml", "w") as file_handle:
    file_handle.write(dataset.yaml())
```
Now that the YAML file has been exported, it can be edited or extended to you desire. Finally, the ```Dataset``` object can be re-initialized using the ```from_yaml```-classmethod, which parses the YAML content to the appropriate metadatablock objects. From this point, modifications can be made similar to the previous example.

```python
dataset = Dataset.from_yaml(path = "./MyDataset.yaml")
```

## 🚑 Help

Help will arrive soon ...

## 👫 Authors

Jan Range - University Of Stuttgart

## 📄 License

This project is licensed under the MIT License - see the LICENSE.md file for details

## ☑️ Acknowledgments

Will be written soon ...
