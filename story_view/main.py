import requests, re, json, time


class stories:
    def __init__(self, cookies, user):
        self.cookies = {'cookie': cookies}
        self.user = user
        self.profile()


    def profile(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Alt-Used': 'www.instagram.com',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Priority': 'u=0, i',
            }

            response = requests.get('https://www.instagram.com/%s/'%(self.user), cookies=self.cookies, headers=headers)

            if response.status_code == 200:
                self.version_id = re.search('"versioningID":"(.*?)"', response.text).group(1)
                self.csrf_token = re.search('"csrf_token":"(.*?)"', response.text).group(1)
                self.app_id = re.search('"APP_ID":"(.*?)"', response.text).group(1)
                self.lsd = re.search('"LSD",\[\],{"token":"(.*?)"', response.text).group(1)
                self.actor_id = re.search('"actorID":"(.*?)"', response.text).group(1)
                self.spin_r = re.search('"__spin_r":(.*?),', response.text).group(1)
                self.spin_t = re.search('"__spin_t":(.*?),', response.text).group(1)
                self.fb_dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', response.text).group(1)
                self.jazoest = re.search('jazoest=(.*?)"', response.text).group(1)
                self.hsi = re.search('"hsi":"(.*?)"', response.text).group(1)
                self.ccg = re.search('"connectionClass":"(.*?)"', response.text).group(1)
                self.haste_session = re.search('"haste_session":"(.*?)"', response.text).group(1)
                self.uid = re.search('"props":{"id":"(.*?)"', response.text).group(1)

                self.stories_info()

            else:
                print('Error get data')


        except Exception as e:
            raise e


    def stories_info(self):
        try:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-Friendly-Name': 'PolarisStoriesV3ReelPageStandaloneDirectQuery',
                'X-BLOKS-VERSION-ID': self.version_id,
                'X-CSRFToken': self.csrf_token,
                'X-IG-App-ID': self.app_id,
                'X-FB-LSD': self.lsd,
                'X-ASBD-ID': '129477',
                'Origin': 'https://www.instagram.com',
                'Alt-Used': 'www.instagram.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.instagram.com/%s/'%(self.user),
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Priority': 'u=0'
            }

            self.data = {
                'av': self.actor_id,
                '__d': 'www',
                '__user': '0',
                '__a': '1',
                '__req': 'u',
                '__hs': self.haste_session,
                'dpr': '1',
                '__ccg': self.ccg,
                '__rev': self.spin_r,
                '__s': '',
                '__hsi': self.hsi,
                '__dyn': '',
                '__csr': '',
                '__comet_req': '7',
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'lsd': self.lsd,
                '__spin_r': self.spin_r,
                '__spin_b': 'trunk',
                '__spin_t': self.spin_t,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisStoriesV3ReelPageStandaloneDirectQuery',
                'variables': '{"reel_ids_arr":["%s"]}'%(self.uid),
                'server_timestamps': 'true',
                'doc_id': '8118053404899604',
            }

            response = requests.post('https://www.instagram.com/graphql/query', cookies=self.cookies, headers=self.headers, data=self.data).json()

            if response['status'] == 'ok':
                media = response['data']['xdt_api__v1__feed__reels_media']['reels_media']
                if len(media) != 0:
                    items = media[0]['items']
                    for item in items:
                        if item['carousel_media'] == None:
                            caption = item['caption']['text'] if item['caption'] != None else 'None'
                            image = item['image_versions2']['candidates'][0]['url']
                            video = item['video_versions'][0]['url'] if item['video_versions'] != None else 'None'
                            story_id = item['id']
                            time_sent = item['taken_at']

                            # data = {'caption': caption, 'image': image, 'video': video}
                            
                            self.view_story(story_id, time_sent)

                        else:
                            print('Stories carousel_media')

                else:
                    print('stories not found')

        except Exception as e:
            raise e


    def view_story(self, story_id, time_sent):
        try:
            media_id, uid = story_id.split('_')
            data = self.data
            data.update({
                'fb_api_req_friendly_name': 'PolarisStoriesV3SeenDirectMutation',
                'variables': '{"reelId":"%s","reelMediaId":"%s","reelMediaOwnerId":"%s","reelMediaTakenAt":%s,"viewSeenAt":%s}'%(uid,media_id,uid,time_sent,self.spin_t),
                'doc_id': '7652261868163375'
            })

            response = requests.post('https://www.instagram.com/graphql/query', cookies=self.cookies, headers=self.headers, data=data).json()

            if response['status'] == 'ok':
                if 'errors' in response.__str__():
                    print('Error: %s\n'%(response['errors'][0]['message']))

                else:
                    print('Succes view story')
                    print('User: %s'%(self.user))
                    print('story_id: %s\n'%(story_id))
                    time.sleep(3)

        except Exception as e:
            raise e



cookies = open('data/cookies.txt','r').read()

stories(cookies, 'hnfaaahlwn_')