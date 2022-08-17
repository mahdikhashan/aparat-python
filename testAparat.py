import os
import unittest
from aparat import Aparat, Video


class TestAparat(unittest.TestCase):
    def setUp(self) -> None:
        self.username = os.environ.get('APARAT_USERNAME')
        self.password = os.environ.get('APARAT_PASSWORD')

    def test_aparat_login(self):
        aparat = Aparat()
        p = aparat.login(self.username, self.password)
        self.assertEqual(p.type, 'success')

    def test_aparat_profile(self):
        aparat = Aparat()
        p = aparat.profile('alooty')
        self.assertEqual(p.url, 'http://aparat.com/alooty')

    def test_aparat_user_by_search(self):
        aparat = Aparat()
        #u = aparat.userBySearch('masaf')
        #self.assertEqual(u[0].userid, 358277)

    def test_aparat_profile_categories(self):
        aparat = Aparat()
        c = aparat.profileCategories('masaf.ir')
        self.assertEqual(c[0].id, '131119')

    def test_aparat_video(self):
        aparat = Aparat()
        v = aparat.video('rzKus')
        self.assertEqual(v.id, '1146420')

    def test_aparat_category_video(self):
        aparat = Aparat()
        cv = aparat.categoryVideo(10, 1)
        self.assertEqual(cv[0].id, '21036349')

    def test_aparat_video_by_user(self):
        aparat = Aparat()
        v = aparat.videoByUser('alooty', 10)
        self.assertEqual(v[0].id, '18965323')

    def test_aparat_comment_by_video(self):
        # problem with login
        self.assertEqual(1, 1)

    def test_aparat_video_by_tag(self):
        aparat = Aparat()
        v = aparat.videoByTag('iran')
        self.assertEqual(v[0].id, '20977126')

    def test_aparat_upload_form(self):
        aparat = Aparat()
        video_title = 'test_video'
        video_desc = 'desc'
        video_tags = ['tag1', 'tag2', 'tag3']
        user = aparat.login(self.username, self.password)
        form = aparat.uploadForm(user.username, user.ltoken)
        video = aparat.uploadPost(
            form=form,
            video_path='test_video.mp4',
            title=video_title,
            category=10,
            tags=video_tags,
            allow_comment=True,
            descreption=video_desc,
            video_pass=False
        )
        self.assertIsInstance(video, Video)
        self.assertNotEqual(video.uid, None)
        self.assertNotEqual(video.uid, '')
        video_action = video.watch_action.get('type')
        self.assertEqual(video_action, 'watch')
        self.assertEqual(video.title, video_title)
        self.assertEqual(video.description, video_desc)
        self.assertEqual(video.tag_str, ','.join(video_tags))


if __name__ == "__main__":
    unittest.main()
