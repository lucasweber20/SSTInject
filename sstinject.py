import argparse
import concurrent.futures
from scripts.URL import URL
from scripts.SSTI import SSTI
from scripts.Parser import Parser
from scripts.Requests import Requests


parser = argparse.ArgumentParser()

args = parser.add_argument("-u", "--url", help='Specify url, example: -u https://example.com/?param=value', nargs="+", type=str)
args = parser.add_argument("-l", "--list", help="Specify file with urls, example: -l urls.txt", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 2", default=1, type=int)
args = parser.add_argument("-o", "--output", help="Specify output file, example: -o outputs.txt", type=str)

args = parser.parse_args()

def main():
    url = args.url
    file = args.list
    thread = args.thread
    output = args.output

    urls = URL()

    # Remove duplicates
    if file:
        url = urls.remove_duplicates(file)

    # Generate payloads
    payload = SSTI()
    payloads = payload.generate_payloads()
  
    # Parser
    parsed_urls = []
    for parser_url in url:
        parser = Parser(parser_url)
        for p in payloads:
            payload_str = f"SsTi{p}SsTi"
            parsed_urls_params = parser.parser_params(payload_str)
            if parsed_urls_params and parsed_urls_params not in parsed_urls:
                parsed_urls.append(parsed_urls_params)

    # Requests
    req = Requests()
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as executor:
        futures = [executor.submit(req.requests, url) for url in parsed_urls]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                pass

if __name__ == "__main__":
    main()