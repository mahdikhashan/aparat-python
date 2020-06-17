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
- [ ] Upload Video
- [ ] Download Video

## How to login

```python
from aparat import Aparat


aparat = Aparat()
user = aparat.login('username', 'password')
```




## References:
[1] https://en.wikipedia.org/wiki/Aparat
