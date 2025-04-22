import yaml
import json

with open("languages.yml") as stream:
    data = yaml.safe_load(stream)

filenames = {}

extensions = {}

formats = []

for lang_name, lang_data in data.items():
    short_item_data = {
        "lang": lang_name,
        "color": lang_data.get("color", "#FF0000"),
        "type": lang_data["type"]
    }
    if lang_data.get("filenames"):
        for filename in lang_data.get("filenames"):
            filenames[filename] = short_item_data
    if lang_data.get("extensions"):
        for extension in lang_data.get("extensions"):
            extensions[extension] = short_item_data
    
    long_item_data = short_item_data.copy()
    long_item_data["extensions"] = lang_data.get("extensions", [])
    long_item_data["filenames"] = lang_data.get("filenames", [])

    formats.append(short_item_data)

with open("filenames.json", "w") as jf:
    json.dump(filenames, jf, indent=4)

with open("extensions.json", "w") as jf:
    json.dump(extensions, jf, indent=4)

with open("formats.json", "w") as jf:
    json.dump(formats, jf, indent=4)
