# module specific business logic (will be use for endpoints)
import regex as re

# from ...load_models import models
from ....core.logging import logger

stopWords = [
    "Editor",
    "Publisher",
    "Penerbit",
    "Penyunting",
    "Penulis",
    "Author",
    "Hak Cipta",
    "Reporter",
    "Tags",
    "Redaktur",
    "Copyright",
    "Follow",
    "Source",
    "Cek Berita",
    "Koran",
    "Bagikan",
    "\|",
    "Sumber",
    ",",
    "-",
    ":",
    "\)",
    "#",
    "[0-9]"
]
stopWords = f"(?:(?!{'|'.join(stopWords)}).)"

class PontianakService:
    def __init__(self) -> None:
        pass

    def get_author(self, text):
        try:
            keys = {"parentheses": None, "penulis": None, "editor": None, "pewarta": None}

            for key in keys:
                if key == "parentheses":
                    tempend = re.findall("(?i)(?<=(?<! Co| Tbk)\.\s*[\[(])[^0-9].*?(?=[\])])", text)
                    if tempend == []:
                        # Try again
                        tempend = re.findall("(?<=\()[^()]*?(?=\)[ .]*$)", text)

                    if tempend != []:
                        tempend = [x.strip() for x in tempend]
                    
                    tempend = list(set(tempend))
                    if len(tempend) == 1:
                        tempend = tempend[0]

                    logger.info(tempend)

                    if tempend == []:
                        tempend = None

                    keys["parentheses"] = tempend
                elif key == "penulis":
                    tempauthor = re.finditer(f"(?i)(?<=(Penulis|Author|Oleh|Laporan)\s*:)\s*{stopWords}*", text)
                    if tempauthor != []:
                        tempauthor = [x.group().strip() for x in tempauthor]

                    tempauthor = list(set(tempauthor))
                    if tempauthor == []:
                        tempauthor = None
                    elif len(tempauthor) == 1:
                        tempauthor = tempauthor[0]

                    keys["penulis"] = tempauthor
                elif key == "editor":
                    tempeditor = re.finditer(f"(?i)(?<=(Editor|Penyunting|Redaktur)\s*:)\s*{stopWords}*", text)
                    if tempeditor != []:
                        tempeditor = [x.group().strip() for x in tempeditor]

                    tempeditor = list(set(tempeditor))
                    if tempeditor == []:
                        tempeditor = None
                    elif len(tempeditor) == 1:
                        tempeditor = tempeditor[0]

                    keys["editor"] = tempeditor
                elif key == "pewarta":
                    temppewarta = re.findall(f"(?i)(?<=Pewarta\s*:)\s*{stopWords}*", text)
                    if temppewarta != []:
                        temppewarta = [x.strip() for x in temppewarta]

                    temppewarta = list(set(temppewarta))
                    if len(temppewarta) == 1:
                        temppewarta = temppewarta[0]

                    keys["pewarta"] = temppewarta

            for key in keys:
                if keys[key] is not None and len(keys[key]) == 0:
                    keys[key] = None

            result = {
                    'result': {
                        # 'text': text,
                        'author': keys
                    }, 
                    'status': 1
                }

            logger.info(f"API return success. Result: {result}")
            return result
        except Exception as e:
            logger.info(f'Error while request: {e}. Text: {text}')
            return {'result': {
                        # 'text': text, 
                        'author': None
                        }, 
                    'status': 0, 
                    'error-message': f'Error while request: {e}.'
                    }