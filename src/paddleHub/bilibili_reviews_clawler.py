import argparse
import requests as rs
import random
import time
from tqdm import tqdm

# bilibili_reviews_crawler
parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, help='bilibili video url')
parser.add_argument('--output_file', type=str, default='./reviews.txt', help='reviews output file')
args = parser.parse_args()


video_api_base = 'http://api.bilibili.com/x/web-interface/view?bvid={}'
reviews_api_base = 'https://api.bilibili.com/x/v2/reply?callback=jQueryjsonp=jsonp&pn={}&type=1&oid={}&sort=0'
sub_reviews_api_base = 'https://api.bilibili.com/x/v2/reply/reply?callback=jQueryjsonp=jsonp&pn={}&type=1&oid={}&ps=10&root={}'
def fetch_reviews(url: str, output_file: str):
    # get old id from bvid
    bvid = url.split('/')[-1]
    r = rs.get(video_api_base.format(bvid)).json()
    aid = r['data']['aid']

    # get reivews info
    r = rs.get(reviews_api_base.format(1, aid)).json()
    rcount = int(r['data']['page']['count'])
    page_size = int(r['data']['page']['size'])

    # fetch reivews
    n_reviews = 0
    with open(output_file, 'w') as f:
        for i in tqdm(range(1, (rcount-1)//page_size+2)):
            time.sleep(random.random())
            r = rs.get(reviews_api_base.format(i, aid)).json()
            replies = r['data']['replies']

            # print(f'page {i}, start to fetch content...')
            for j, reply in enumerate(replies):
                #print(f'*****************{j+1}*****************')
                #print(reply['content']['message'])
                f.write(repr(reply['content']['message']).replace("'", "") + '\n')

                rpid, sub_rcount, sub_page_size = reply['rpid'], int(reply['rcount']), 10
                n_reviews += 1+sub_rcount

                if sub_rcount == 0:  # no sub replies
                    continue

                for k in range(1, (sub_rcount-1)//sub_page_size+2):
                    sub_r = rs.get(sub_reviews_api_base.format(k, aid, rpid)).json()
                    sub_replies = sub_r['data']['replies']
                    for sub_reply in sub_replies:
                        #print('\t' + sub_reply['content']['message'])
                        f.write(repr(sub_reply['content']['message']).replace("'", "") + '\n')

    print(f'total reviews count: {n_reviews}')


if __name__ == "__main__":
    fetch_reviews(args.url, args.output_file)