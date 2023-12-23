from bs4 import BeautifulSoup

from app.utils.v1.split_list_into_chunks import split_list_into_chunks

def get_substitutions_from_soup(soup: BeautifulSoup):
    try:
        substitutions = []
        substitutions = substitutions + [item.get_text().strip() for item in soup.find_all("td", class_="UngeradeZelleTabelleVertretungen")]
        substitutions = substitutions + [item.get_text().strip() for item in soup.find_all("td", class_="ZelleGeradeTabelleVertretungen")]
        substitutionsList = list(split_list_into_chunks(substitutions, 7))
        substitutionsListDict = []
        for item in substitutionsList:
            substitutionsListDict.append(
                {
                    "course": item[0],
                    "hour": item[1],
                    "substitute_teacher": item[2],
                    "subject": item[3],
                    "room": item[4],
                    "replaced_teacher": item[6],
                }
            )
        return substitutionsListDict
    except AttributeError:
        return []
