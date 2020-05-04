import argparse
import base64

import pandas as pd
import requests

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--server-url')
    parser.add_argument('--server-port')
    parser.add_argument('--image-url')
    args = parser.parse_args()
    response_content = requests.get(args.image_url).content
    image_contents = base64.encodebytes(response_content)
    model_input = pd.DataFrame(data={'image_bytes': [image_contents]}).to_json(orient="split")
    response = requests.post(url='{host}:{port}/invocations'.format(host=args.server_url, port=args.server_port),
                             data=model_input,
                             headers={"Content-Type": "application/json; format=pandas-split"})

    print(response)
