# Aparat Python API
![Aparat Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Aparat_English_Square.png/250px-Aparat_English_Square.png)

[Aparat](http://www.aparat.com/) (Persian: آپارات‎, Âpârât) is an Iranian video sharing service (source: wikipedia [1])

## Features

- [x] Login
- [x] Profile
- [x] Search
- [x] Profile Categories
- [x] Video
- [x] Video Categories
- [x] Video By User
- [x] Comment By Video
- [x] Video By Tag
- [x] Upload Video
- [ ] Download Video

## How to login

```python
from aparat import Aparat


aparat = Aparat()

user = aparat.login('username', 'password')
```


## How to upload a video

```python
from aparat import Aparat


aparat = Aparat()

user = aparat.login(username, password)
form = aparat.uploadForm(user.username, user.ltoken)

video = aparat.uploadPost(
    form=form,
    video_path='video.mp4',
    title='title',
    category=10,
    tags=['tag1', 'tag2', 'tag3'],
    allow_comment=True,
    descreption='desc',
    video_pass=False
)
```


## References:
[1] https://en.wikipedia.org/wiki/Aparat
