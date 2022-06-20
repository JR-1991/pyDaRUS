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

    # Get the identifier scheme
    if author.identifier_scheme:
        identifier_scheme = IdentifierScheme(author.identifier_scheme)
        scheme_valid_fun = scheme_factory(identifier_scheme)

        author_valid, report = scheme_valid_fun(author)

        return author_valid, report

    else:
        # Search for an author on ORCID
        return "None", {}


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
    orcid_names = set(
        orcid_entry["given-names"].split(" ") + orcid_entry["family-names"].split(" ")
    )

    ds_name = set(author.name.split(" "))

    diff = set(list(orcid_names - ds_name) + list(ds_name - orcid_names))

    if diff:
        is_valid = False
        report = {
            "loc": f"Author/{author.name}",
            "message": f"Author name for ORCID entry {author.identifier} {author.name} matches expect for the following name/s: {diff}",
            "proposed-change": " ".join(
                [orcid_entry["given-names"], orcid_entry["family-names"]]
            ),
        }

    else:
        is_valid = True
        report = None

    return is_valid, report


if __name__ == "__main__":
    author = Author(
        name="Jan Range",
        identifier_scheme=IdentifierScheme.orcid,
        identifier="0000-0001-6478-1051",
        affiliation="SimTech",
    )

    author_valid, report = validate_author(author)

    print(author_valid)
    print(json.dumps(report, indent=2))
