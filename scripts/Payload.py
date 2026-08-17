import yaml


class Payload:
    def __init__(self):
        pass

    def generate_payloads(self):
        result = []
        with open("./db/payloads.yml", "r") as f:
            payloads = yaml.safe_load(f)
            
        for p in payloads["payloads"]:
            result.append(p)

        return result