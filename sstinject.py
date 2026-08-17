import argparse
from scripts.URL import URL
from scripts.Payload import Payload
from scripts.Parser import Parser


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

    payload = "SsTiinjectionSsTi"

    urls = URL()

    # Remove duplicates
    if file:
        url = urls.remove_duplicates(file)

    # Generate payloads
    payload = Payload()
    payloads = payload.generate_payloads()

    # Parser
    parsed_urls = []
    for parser_url in url:
        parser = Parser(parser_url)
        for p in payloads:
            parsed_urls_params = parser.parser_params(p)
            if parsed_urls_params and parsed_urls_params not in parsed_urls:
                parsed_urls.append(parsed_urls_params)

if __name__ == "__main__":
    main()