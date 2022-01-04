from fastapi import FastAPI

from pyDaRUS.metadatablocks.citation import Citation
from pyDaRUS.metadatablocks.enzymeML import EnzymeMl
from pyDaRUS.metadatablocks.engMeta import EngMeta
from pyDaRUS.metadatablocks.codeMeta import CodeMeta
from pyDaRUS.metadatablocks.archive import Archive
from pyDaRUS.metadatablocks.process import Process
from pyDaRUS.metadatablocks.privacy import Privacy

app = FastAPI(title="pyDaRUS", version="1.0", redoc_url="/")
@app.post(
    "/create/citation",
    summary="Create Citation block",
    description="Creates a Dataverse compatible JSON file for the Citation schema",
    tags=["Metadatablocks"]
)
async def create_citation(citation: Citation):
    return citation.dataverse_dict()

@app.post(
    "/create/enzymeml",
    summary="Create EnzymeMl block",
    description="Creates a Dataverse compatible JSON file for the EnzymeMl schema",
    tags=["Metadatablocks"]
)
async def create_enzymeml(enzymeml: EnzymeMl):
    return enzymeml.dataverse_dict()

@app.post(
    "/create/engmeta",
    summary="Create EngMeta block",
    description="Creates a Dataverse compatible JSON file for the EngMeta schema",
    tags=["Metadatablocks"]
)
async def create_engmeta(engmeta: EngMeta):
    return engmeta.dataverse_dict()

@app.post(
    "/create/codemeta",
    summary="Create CodeMeta block",
    description="Creates a Dataverse compatible JSON file for the CodeMeta schema",
    tags=["Metadatablocks"]
)
async def create_codemeta(codemeta: CodeMeta):
    return codemeta.dataverse_dict()

@app.post(
    "/create/archive",
    summary="Create Archive block",
    description="Creates a Dataverse compatible JSON file for the Archive schema",
    tags=["Metadatablocks"]
)
async def create_archive(archive: Archive):
    return archive.dataverse_dict()

@app.post(
    "/create/process",
    summary="Create Process block",
    description="Creates a Dataverse compatible JSON file for the Process schema",
    tags=["Metadatablocks"]
)
async def create_process(process: Process):
    return process.dataverse_dict()

@app.post(
    "/create/privacy",
    summary="Create Privacy block",
    description="Creates a Dataverse compatible JSON file for the Privacy schema",
    tags=["Metadatablocks"]
)
async def create_privacy(privacy: Privacy):
    return privacy.dataverse_dict()