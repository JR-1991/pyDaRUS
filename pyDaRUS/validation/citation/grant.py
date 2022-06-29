from operator import truediv
import json
from urllib.error import HTTPError
import requests
from Levenshtein import distance
import re
from typing import Callable

from pyDaRUS.metadatablocks.citation import GrantInformation

def validate_grantInformation(grant: GrantInformation, allow_edit: bool = False):
    """ Validates grantInformation
        Args:
            grant (GrantInformation): compound object that includes all grant information of a dataset with subfields grant_agency and grant_number
            allow_edit (bool, optional): Whether or not proposed edits should be applied. Defaults to False.
    """
    is_valid, report = _grantInfo_isEmpty(grant)

    if not is_valid:
        return is_valid, report

    spelling_valid, spelling_report = _grantAgency_checkSpelling(grant.grant_agency)

    is_valid = is_valid and spelling_valid

    if not is_valid:
        return is_valid, spelling_report

    check_number = funder_factory(grant.grant_agency)

    if check_number is not None:
        number_valid, number_report = check_number(grant)

        if not number_valid:
            return number_valid, number_report

    return is_valid, report

def _grantInfo_isEmpty(grant: GrantInformation):
    """ Checks, if grant information is (partly) not provided
        Args:
            grant (GrantInformation): compound object that includes all grant information of a dataset with subfields grant_agency and grant_number
    """
    if not grant.grant_agency:
        is_valid = False
        if not grant.grant_number:
            report = {
                "loc": f"GrantInformation",
                "message": f"No grant information provided. Correct?",
                "proposed-change": None
            }
        else:
            report = {
                "loc": f"GrantInformation/{grant.grant_number}",
                "message": f"Grant number {grant.grant_number} without grant agency.",
                "proposed-change": None
            }
    else:
        if not grant.grant_number:
            is_valid = False
            report = {
                "loc": f"GrantInformation/{grant.grant_agency}",
                "message": f"Grant agency {grant.grant_agency} without grant number.",
                "proposed-change": None
            }
        else:
            is_valid = True
            report = None

    return is_valid, report

def _grantAgency_checkSpelling(grantAgency: str):
    """ Checks, if grantAgency is known and spelled as expected """
    valid_agencies = ["DFG", "BMBF", "European Commission", "MWK"]

    if grantAgency in valid_agencies:
        is_valid = True
        report = None
    else:
        replace_agency = {
            "Deutsche Forschungsgemeinschaft": "DFG", 
            "EU": "European Commission", 
            "EC": "European Commission", 
            "Europa": "European Commission",
            "Ministerium für Wissenschaft und Kunst": "MWK",
            "Bundesministerium für Bildung und Forschung": "BMBF"}
        if grantAgency in replace_agency:
            is_valid = False
            report = {
                "loc": f"GrantInformation/{grantAgency}",
                "message": f"Grant Agency {grantAgency} not in recommended notation.",
                "proposed-change": replace_agency[grantAgency]
            }

        for agency in valid_agencies:
            lev = distance(agency, grantAgency)
            if 0 < lev < 3:
                is_valid = False
                report = {
                    "loc": f"GrantInformation/{grantAgency}",
                    "message": f"Typo in grant agency {grantAgency}.",
                    "proposed-change": agency
                }


    return is_valid, report

def _validateOpenAIRE(grant: GrantInformation):
    """ checks grant number of EU projects """

    if grant.grant_agency == "European Commission":
        pattern = re.match("info:eu-repo/grantAgreement/(.*)/(.*)/(.*)", grant.grant_number)
        print("pattern:", pattern)
        if pattern:
            funder = pattern.group()[0]
            program = pattern.group()[1]
            number = pattern.group()[2]
            try:
                info = _getProjectInfos_OpenAire(number)
            except HTTPError as e:
                report = {
                    "loc": f"GrantInformation/{grant.grant_number}",
                    "message": f"Not able to check {grant.grant_number}: {e}",
                    "proposed-change": None
                }
                return False, report
            if info is not None and info["funder"] == funder and info["program"] == program:
                is_valid = True
                report = None
            else:
                is_valid = False
                report = {
                    "loc": f"GrantInformation/{grant.grant_number}",
                    "message": f"Grant number {grant.grant_number} is not valid or not in the right format for EU projects.",
                    "proposed-change": f"info:eu-repo/grantAgreement/{info['funder']}/{info['program']}/{info['projectid']}"
                }

        else:
            is_valid = False
            number = grant.grant_number
            info = _getProjectInfos_OpenAire(number)
            if info["projectid"] != "":
                report = {
                    "loc": f"GrantInformation/{grant.grant_number}",
                    "message": f"Grant number {grant.grant_number} is not in the right format for EU projects.",
                    "proposed-change": f"info:eu-repo/grantAgreement/{info['funder']}/{info['program']}/{info['projectid']}"
                }
            else:
                report = {
                    "loc": f"GrantInformation/{grant.grant_number}",
                    "message": f"Grant number {grant.grant_number} is not a valid EU project id."
                }
        return is_valid, report
    else:
        return True, None

def funder_factory(grantAgency: str) -> Callable:
    """
        returns function to check the grantNumber of a funder

        Args:
        grantAgency (str): Name of the grant agency

    Returns:
        Callable: Corresponding validation function.
    """
    funder_mapping = {
        "European Commission" : _validateOpenAIRE
    }

    return funder_mapping[grantAgency]


def _getProjectInfos_OpenAire(projectid:str):
    info = {}
    info["funder"] = ""
    info["program"] = ""
    info["projectid"] = ""

    url = f"http://api.openaire.eu/search/projects?format=json&grantID={projectid}"
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()["response"]["results"]
        # print(json.dumps(result, indent=2))
        results = []
        if result and "result" in result:
            results = result.get("result")
            print("result vorhanden")
        # Iterate over all results and retrieve the one with the corresponding project
        for result in results:
            project = result.get("metadata").get("oaf:entity").get("oaf:project")
            # print(json.dumps(project, indent=2))
            if project.get("code").get("$") == projectid:
                print("richtige projectid")
                info["projectid"] = projectid
                fundinginfo = project.get("fundingtree")
                # print(json.dumps(fundinginfo, indent=2))
                if fundinginfo:
                    info["funder"] = fundinginfo.get("funder").get("shortname").get("$")
                    info["program"] = fundinginfo.get("funding_level_1").get("parent").get("funding_level_0").get("name").get("$")

    else:
        raise requests.HTTPError(
            f"Bad request: {response.status_code} {response.reason}"
        )
    return info

if __name__ == "__main__":
    grant = GrantInformation(
        grant_agency="European Commission",
        grant_number="640741"
    )

    grant_valid, report = validate_grantInformation(grant)
    print(grant_valid)
    print(json.dumps(report, indent=2))
