import json
import requests

from typing import Callable, Dict

from pyDaRUS.metadatablocks.citation import Author, IdentifierScheme


def validate_author(author: Author, allow_edit: bool = False):
    """Validates whether the name of an author is consistent with the given identifier scheme.

    Args:
        author (Author): Compound object that includes all informations of an author
        allow_edit (bool, optional): Whether or not proposed edits should be applied. Defaults to False.
    """

    # Initialize report
    report = {}

    if not author.name:
        return False, {"loc": "Author", "message": "Author missing name"}

    # Get the identifier scheme
    if author.identifier_scheme:
        # Validate identifier
        identifier_scheme = IdentifierScheme(author.identifier_scheme)
        scheme_valid_fun = scheme_factory(identifier_scheme)

        author_valid, sub_report = scheme_valid_fun(author)

        report["name"] = sub_report

        return author_valid, report

    else:
        # Search author via ORCID
        author_valid, report = _retrieve_by_name_from_orcid(author.name)

        return author_valid, report


def scheme_factory(scheme: IdentifierScheme) -> Callable:
    """Returns a validation function to the corresponding identifier scheme

    Args:
        scheme (IdentifierScheme): Enumeration part of the identifier scheme

    Returns:
        Callable: Corresponding validation scheme.
    """

    scheme_mapping = {IdentifierScheme.orcid: _validate_orcid}

    return scheme_mapping[scheme]


def _validate_orcid(author: Author):
    """Takes an orcid ID and checks consistency to the authors informations"""

    # Get data of corresponding ORCID ID
    url = f"https://pub.orcid.org/v3.0/expanded-search/?q={author.identifier}"
    response = requests.get(url, headers={"Accept": "application/vnd.orcid+json"})

    if response.status_code == 200:
        results = response.json()["expanded-result"]

        # Iterate over all results and retrieve the one with the corresponding ORCID
        for result in results:
            if result.get("orcid-id") == author.identifier:
                name_valid, name_report = _check_names(author, result)
                return name_valid, name_report

    else:
        raise requests.HTTPError(
            f"Bad request: {response.status_code} {response.reason}"
        )


def _check_names(author: Author, orcid_entry: Dict):
    """Checks if the names from an author match to the ORCID entry"""

    # Split both names and create a set of words
    orcid_name = " ".join([orcid_entry["given-names"], orcid_entry["family-names"]])
    orcid_names = set(orcid_name.split(" "))

    ds_name = set(author.name.split(" "))

    diff = set(list(orcid_names - ds_name) + list(ds_name - orcid_names))

    if diff:
        is_valid = False
        report = {
            "message": f"Author name for ORCID entry ('{author.identifier}', '{orcid_name}') matches with Dataverse ('{author.name}') expect for the following name/s: {diff}",
            "proposed-changes": {"name": orcid_name},
        }

    else:
        is_valid = True
        report = None

    return is_valid, report


def _retrieve_by_name_from_orcid(name: str):
    """Retrieves an ORCID ID from a givebn name.

    Args:
        name (str): Author name of teh Dataverse dataset
    """

    def score_name(target: str, query: str):
        """Matches a name and returns a percent identity"""

        target_set = set(target.split(" "))
        query_set = set(query.split(" "))

        diff = sum([1 for name in query_set if name in target_set])

        return diff / len(target_set)

    # Set up and perform HTTP request
    url = f"https://pub.orcid.org/v3.0/expanded-search/?q={name}"
    response = requests.get(url, headers={"Accept": "application/vnd.orcid+json"})
    results = response.json()["expanded-result"]

    # Score all occuring result entries
    matches = []
    for result in results:
        orcid_name = " ".join([str(result["given-names"]), str(result["family-names"])])
        orcid_id = result["orcid-id"]

        score = score_name(name, orcid_name)
        matches.append((orcid_name, orcid_id, score))

    # Sort everything and add all top entries with same score
    matches = sorted(matches, key=lambda x: x[-1], reverse=True)
    best_score = matches[0][-1]

    proposals = [
        {
            "name": name,
            "identifier": orcid_id,
            "identifier_scheme": IdentifierScheme.orcid.value,
        }
        for name, orcid_id, score in matches
        if score == best_score
    ]

    return False, {
        "message": f"Author '{name}' is missing an identifier. The name has been used to retrieve from ORCID and is attached in 'porposed-changes'.",
        "proposed-changes": proposals,
    }
