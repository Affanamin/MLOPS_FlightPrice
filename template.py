import os

dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    os.path.join("data","Transformed01"),
    os.path.join("data","Transformed02"),
    os.path.join("data","Transformed03"),
    os.path.join("data","Transformed04"),
    os.path.join("data","Transformed05"),
    os.path.join("data","Transformed06"),
    os.path.join("data","Transformed07"),
    os.path.join("data","Transformed08"),
    "notebooks",
    "saved_models",
    "src",
    "report"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass

file = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")]

for file_ in file:
    with open(file_,"w") as f:
        pass