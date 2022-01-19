import os

from easyDataverse import Dataset
from pyDaRUS.metadatablocks import Citation
from pyDaRUS.metadatablocks import EnzymeMl
from pyDaRUS.metadatablocks import EngMeta
from pyDaRUS.metadatablocks import CodeMeta
from pyDaRUS.metadatablocks import Archive
from pyDaRUS.metadatablocks import Process
from pyDaRUS.metadatablocks import Privacy

# Add the lib_name to the operating systems env
os.environ["EASYDATAVERSE_LIB_NAME"] = "pyDaRUS"