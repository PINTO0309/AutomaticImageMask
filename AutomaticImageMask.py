from base64 import b64encode
import json
import requests
import argparse
import cv2

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Google Cloud Vision Api')
    parser.add_argument('api_key', help='api path')
    parser.add_argument('image', help='image path')
    parser.add_argument('mask_word', help='Character to be masked')
    args = parser.parse_args()

    img_requests = []
    with open(args.image, 'rb') as f:
        ctxt = b64encode(f.read()).decode()
        img_requests.append({
                'image': {'content': ctxt},
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 10
                }]
        })

    response = requests.post(ENDPOINT_URL,
                             data=json.dumps({"requests": img_requests}).encode(),
                             params={'key': args.api_key},
                             headers={'Content-Type': 'application/json'})

    out = cv2.imread(args.image)
    height, width = out.shape[:2]
    json_dict = response.json()['responses']

    for x in json_dict:
        for y in x:
            if y == 'textAnnotations':
                for z in x[y]:

                    x1 = 0
                    y1 = 0
                    x2 = 0
                    y2 = 0

                    try:
                        x1 = z['boundingPoly']['vertices'][0]['x']
                    except:
                        pass
                    try:
                        y1 = z['boundingPoly']['vertices'][0]['y']
                    except:
                        pass
                    try:
                        x2 = z['boundingPoly']['vertices'][2]['x']
                    except:
                        pass
                    try:
                        y2 = z['boundingPoly']['vertices'][2]['y']
                    except:
                        pass

                    description = z['description'].replace('\n','')
                    rectposition = ((x1, y1), (x2, y2))

                    print(description, '\t\t', rectposition)

                    if args.mask_word in description:
                        if ((x2 - x1) * (y2 - y1)) <= ((width * height) * 0.1):
                            cv2.rectangle(out, rectposition[0], rectposition[1], (0, 0, 255), 2)
                            cv2.rectangle(out, rectposition[0], rectposition[1], (0, 0, 0), -1)
                    else:
                        pass

    cv2.imshow('masked', out)
    cv2.imwrite('masked.png', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


