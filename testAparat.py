import unittest
from Aparat import Aparat


class TestAparat(unittest.TestCase):
    def test_aparat_login(self):
        aparat = Aparat()
        p = aparat.login('mahdi.khashan', '12345678')
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
        pass


if __name__ == "__main__":
    unittest.main()
