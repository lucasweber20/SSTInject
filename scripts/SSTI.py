import yaml
import re


class SSTI:
    def __init__(self):
        pass

    def generate_payloads(self):
        result = []
        with open("./db/payloads.yml", "r") as f:
            payloads = yaml.safe_load(f)
            
        for p in payloads["payloads"]:
            result.append(p)

        return result

    def check_ssti(self, body, url):
        result = []
        matches = re.findall(r"SsTi.*SsTi", body)
        for match in matches:
            if "49" in match:
                result.append(url)
        return result