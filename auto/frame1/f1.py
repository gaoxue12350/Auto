import yaml

with open("f1.yaml") as f:
    # data=yaml.load(f,Loader=yaml.FullLoader)
    data=yaml.safe_load(f)
    print(data)