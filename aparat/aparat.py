"""Aparat Video Platform

   author: Mahdi Khashan
   data: 1399/02/13
"""

import os
import json
import hashlib
import urllib3
import certifi
import requests


class Base(object):
    """Base Object"""

    def __init__(self, dic):
        """init"""
        self.dic = dic
        for key in dic.keys():
            setattr(self, key, dic[key])


class CommentList(object):
    """ Aparat CommentList Model
        TODO:
    """

    def __init__(self, dic):
        self.dic = dic
        for key in dic.keys():
            setattr(self, key, dic[key])


class Category(object):
    """ Aparat Categories Model
        TODO:
    """

    def __init__(self, dic):
        self.dic = dic
        for key in dic.keys():
            setattr(self, key, dic[key])


class Channel(object):
    """ Aparat User Model
        TODO:
    """

    def __init__(self, dic):
        self.dic = dic
        for key in dic.keys():
            setattr(self, key, dic[key])


class ChannelInfo(object):
    """ Aparat User Info Model
        TODO:
    """

    def __init__(self):
        pass


class Video(object):
    """ Aparat Video Model
        TODO:
    """

    def __init__(self, dic):
        self.dic = dic
        for key in dic.keys():
            setattr(self, key, dic[key])


class VideoList(Base):
    """ Aparat Video List Model
        TODO:
    """

    def __init__(self, dic):
        super().__init__(dic)


class Profile(Base):
    """
    Profile Object

    :param id: user id -> (int)
    :param username: user username -> (string)
    :param name: user name -> (string)
    :param pic: does user have profile pic or not -> (string)
    :param ltokem: token when user need login e.x: video uploading -> (string)
    :param banned: whether usesr is banned or not -> (string)
    :param email: user email -> (string)
    :param mobile_number: user mobile number -> (string)
    :param movile_valid: validated user mobile number -> (string)
    :param pic_s: small sized user profile pic -> (url)
    :param pic_m: medium sized user profile pic -> (url)
    :param pic_b: big sized user profile pic -> (url)
    """

    def __init__(self, dic):
        super().__init__(dic)


class Form(Base):
    """
    Form Action Object

    :param formAction: data to post should be to this address -> (url)
    :param directuploadAction: no information -> (url)
    :param frm-id: form id -> (int)
    """

    def __init__(self, dic):
        super().__init__(dic)


class Aparat(object):
    """ Aparat Api Model
        TODO:
    """

    def __init__(self):
        pass

    def __sh1_mdf5__(self, value):
        mdf5 = hashlib.md5()
        sha1 = hashlib.sha1()
        mdf5.update(value.encode('utf-8'))
        sha1.update(mdf5.hexdigest().encode('utf-8'))
        hashedValue = sha1.hexdigest()
        return hashedValue

    def login(self, luser, lpass):
        hashedpass = self.__sh1_mdf5__(lpass)
        r = requests.get(
            'https://www.aparat.com/etc/api/login/luser/{}/lpass/{}'.format(luser, hashedpass))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['login']
            profile = Profile(dic)
            return profile
        else:
            return None

    def profile(self, username):
        r = requests.get(
            'https://www.aparat.com/etc/api/profile/username/{}'.format(username))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['profile']
            channel = Channel(dic)
            return channel
        else:
            return None

    def userBySearch(self, text, perpage=10):
        r = requests.get(
            'https://www.aparat.com/etc/api/userBySearch/text/{}/perpage/{}'.format(text, perpage))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['userbysearch']
            channels = []
            for channel in dic:
                c = Channel(channel)
                channels.append(c)
            return channels
        else:
            return None

    def profileCategories(self, username):
        r = requests.get(
            'https://www.aparat.com/etc/api/profilecategories/username/{}'.format(username))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['profilecategories']
            categories = []
            for category in dic:
                c = Category(category)
                categories.append(c)
            return categories
        else:
            return None

    def video(self, videohash):
        r = requests.get(
            ' https://www.aparat.com/etc/api/video/videohash/{}'.format(videohash))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['video']
            video = Video(dic)
            return video
        else:
            return None

    def categoryVideo(self, perpage=10, cat=1):
        r = requests.get(
            'https://www.aparat.com/etc/api/categoryVideos/cat/{}/perpage/{}'.format(cat, perpage))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['categoryvideos']
            catVideos = []
            for catVideo in dic:
                cv = VideoList(catVideo)
                catVideos.append(cv)
            return catVideos
        else:
            return None

    def videoByUser(self, username, perpage=10):
        r = requests.get(
            'https://www.aparat.com/etc/api/videoByUser/username/{}/perpage/{}'.format(username, perpage))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['videobyuser']
            videos = []
            for video in dic:
                v = VideoList(video)
                videos.append(v)
            return videos
        else:
            return None

    def commentByVideos(self, videohash, perpage=10):
        r = requests.get(
            'https://www.aparat.com/etc/api/commentByVideos/videohash/{}/perpage/{}'.format(videohash, perpage))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['videobyuser']
            comments = []
            for comment in dic:
                c = CommentList(comment)
                comments.append(c)
            return comments
        else:
            return None

    def videoBySearch(self, text, perpage=10):
        r = requests.get(
            'https://www.aparat.com/etc/api/videoBySearch/text/{}/perpage/{}'.format(text, perpage))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['videobysearch']
            videos = []
            for video in dic:
                v = VideoList(video)
                videos.append(v)
            return videos
        else:
            return None

    def videoByTag(self, text):
        r = requests.get(
            'https://www.aparat.com/etc/api/videobytag/text/{}'.format(text))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['videobytag']
            videos = []
            for video in dic:
                v = VideoList(video)
                videos.append(v)
            return videos
        else:
            return None

    def uploadForm(self, luser, ltoken):
        r = requests.get(
            'https://www.aparat.com/etc/api/uploadform/luser/{}/ltoken/{}'.format(luser, ltoken))
        if r.status_code == 200:
            data = json.loads(r.text)
            dic = data['uploadform']
            frm_id = dic['frm-id']
            dic['frm_id'] = frm_id
            del dic['frm-id']
            form = Form(dic)
            return form
        else:
            return None

    def uploadPost(
            self, 
            video_path: str, 
            title: str, 
            category: int, 
            form: Form, 
            tags: 'list[str]' = None,
            allow_comment: bool = None, 
            descreption: str = None, 
            video_pass: bool = None
        ):

        url = form.formAction
        with open(video_path, 'rb') as f:
            video_data = f.read()

        data = {
            'frm-id': form.frm_id,
            'data[title]': title,
            'data[category]': category
        }

        if tags:
            data['data[tags]'] = ','.join(tags)
        if allow_comment is not None:
            data['data[comment]'] = allow_comment
        if descreption is not None:
            data['data[descr]'] = descreption
        if video_pass is not None:
            data['data[video_pass]'] = video_pass

        urllib_http = urllib3.PoolManager(ca_certs=certifi.where())
        resp = urllib_http.request("POST", url, fields={
            "video": (video_path, video_data),
            **data
        })

        if resp.status != 200:
            raise Exception("Upload failed")

        try:
            response_data = json.loads(resp.data.decode('utf-8'))
        except Exception as ex:
            raise Exception("Upload failed")

        videohash = response_data['uploadpost']['uid']
        return self.video(videohash)
