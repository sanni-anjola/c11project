import pathlib
import yaml


file_path = pathlib.Path("./config.yaml").resolve()
text = {'name': 'Boyo', 'age': 18, 'children': ["Odogwu", "Dorcas"]}
with file_path.open(mode="w") as f:
    yaml.dump(text, f, sort_keys=False)

with file_path.open(mode='r', encoding='utf-8') as file:
    text_again = yaml.load(file, Loader=yaml.Loader)

print(text_again)
