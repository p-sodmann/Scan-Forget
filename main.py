import datetime
from win32com.client import Dispatch
from rich import print
import typer
import pytesseract
from PIL import Image
import json
import os


debug_mode = False

class TesseractWrapper():
    def __init__(self) -> None:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    def __call__(self, image) -> str:
        return pytesseract.image_to_string(image, lang="deu")

class ScanService():
    def __init__(self) -> None:
        wia = Dispatch("WIA.CommonDialog")
        dev = wia.ShowSelectDevice()

        self.scanner = dev.Items[0]
        self.scanner.ItemID


        self.WIA_IMG_FORMAT_PNG = "{B96B3CAF-0728-11D3-9D7B-0000F81EF32E}"

        # switch to feeder
        if not debug_mode:
            dev.Properties("Document Handling Select").Value = 1

    def __call__(self):
        return self.scanner.Transfer(self.WIA_IMG_FORMAT_PNG)


class Scan():
    def __init__(self, id=-1, title="") -> None:
        # set date to today
        self.id = id
        self.title = title

        self.date = datetime.date.today()

        self.keywords = []
        self.text = ""
        self.owner = ""
        self.page = 0

        self.image_path = f"images/{self.id:06d}_{self.sanitize_title()}.png"

    def sanitize_title(self):
        replaces = [" ", ":", ";", ",", ".", "!", "?", "\"", "'", "\\", "/", "|", "*", "&", "^", "%", "$", "#", "@", "~", "`", "(", ")", "[", "]", "{", "}", "=", "+", "-", "_", ">", "<"]
        title = self.title
        for replace in replaces:
            title = title.replace(replace, "_")
        return title

    def toJSON(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date.isoformat(),
            "keywords": self.keywords,
            "text": self.text,
            "owner": self.owner,
            "image_path": self.image_path,
            "page": self.page
        }

    def from_json(self, dictionary):
        # load from a json dictionary
        self.id = dictionary["id"]
        self.title = dictionary["title"]
        self.date = datetime.datetime.strptime(dictionary["date"], "%Y-%m-%d").date()
        self.keywords = dictionary["keywords"]
        self.text = dictionary["text"]
        self.owner = dictionary["owner"]
        self.image_path = dictionary["image_path"]
        self.page = dictionary["page"]
        
        return self


class DataBase():
    def __init__(self):
        self.data = []

    def get_next_id(self):
        return len(self.data)

    def save(self):
        serialization_copy = [d.toJSON() for d in self.data]
        with open("database.json", "w", encoding='utf-8') as f:
            json.dump(serialization_copy, f, indent=4, ensure_ascii=False)

    def load(self):
        if not os.path.exists("database.json"):
            return None

        with open("database.json", "r", encoding='utf-8') as f:
            unserialization_copy = json.load(f)
            for d in unserialization_copy:
                self.data.append(Scan().from_json(d))

def main(user: str):
    previous = False
    title = input("Title: ")
    page = 0

    while title != "q":
        if previous:
            if next_title == "q":  
                return None
            elif next_title != "":
                title = next_title
                page = 0
            else:
                page += 1

        scanner = ScanService()

        # scan
        image = scanner()

        scan = Scan(db.get_next_id(), title)
        scan.user = user
        scan.page = page

        image.SaveFile(scan.image_path)

        # reload with pillow
        image = Image.open(scan.image_path)

        # ocr
        tesseract = TesseractWrapper()
        scan.text = tesseract(image)

        db.data.append(scan)
        db.save()

        next_title = input("Title: ")
        previous = True

if __name__ == "__main__":
    db = DataBase()
    db.load()
    typer.run(main)
