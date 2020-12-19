# 请求地址

以下请求均为POST方式请求数据

| 作用     | 请求地址                                 | 请求数据 | 请求数据含义 | 返回数据                        | 返回数据含义                          |
| -------- | ----------------------------------------- | :------------------------------ | -------------------------------------- | -------- | -------- |
| 用户登录 | http://106.13.236.185:5000/api/login_user | username<br />password | 用户名<br />密码 |  success<br />failed             | 登录成功<br />用户名或密码错误         |
| 用户注册 | http://106.13.236.185:5000/api/regit_user | username<br />password | 用户名<br />密码 |success<br />failed<br />repeat | 注册成功<br />注册失败<br />用户名重复   |
| 管理员登录 | http://106.13.236.185:5000/api/login_admin | username<br />password | 用户名<br />密码 | success<br />failed             | 登录成功<br />用户名或密码错误          |
| 管理员注册 | http://106.13.236.185:5000/api/regit_admin | username<br />password | 用户名<br />密码 | success<br />failed<br />repeat | 注册成功<br />注册失败<br />用户名重复  |
| 开发者登录 | http://106.13.236.185:5000/api/login_developer | username<br />password | 用户名<br />密码 |success<br />failed             | 登录成功<br />用户名或密码错误         |
| 开发者注册 | http://106.13.236.185:5000/api/regit_developer| username<br />password | 用户名<br />密码 | success<br />failed<br />repeat | 注册成功<br />注册失败<br />用户名重复 |

## 用户

| 作用             | 请求地址                                            | 请求数据                                                     | 请求数据含义                                                 | 返回数据                                                     | 返回数据含义           |
| ---------------- | --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------- |
| 用户查询个人信息 | http://106.13.236.185:5000/api/user/query_userinfo  | username                                                     | 用户名                                                       | { "birthday": "", "exper": "", "intro": "", "phone": "", "sex": "\u7537", "uid": 1, "uname": "dmar", "unick": "" } | 包含个人信息的json数据 |
| 用户修改个人信息 | http://106.13.236.185:5000/api/user/update_userinfo | uname<br />unick<br />sex<br />phone<br />birthday<br />intro<br />exper | 用户名<br />昵称<br />性别<br />手机号<br />生日<br />个人简介<br />经验值 | success<br />failed                                          | 修改成功<br />修改失败 |

## 游戏

| 作用                                       | 请求地址                                          | 请求数据                                                     | 请求数据含义                                                 | 返回数据                                                     | 返回数据含义                           |
| ------------------------------------------ | ------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------- |
| 查询所有已发布游戏<br />（平台主界面显示） | http://106.13.236.185:5000/api/game/query_all_pub | 无                                                           | 无                                                           | [ { "filename": "http://127.0.0.1:5000/static/2048.py", "gid": 1, "gname": "2048", "image": "http://127.0.0.1:5000/static/2048.png", "name": "2048", "note": null, "star": 0, "version": "1.0" }, { "filename": "http://127.0.0.1:5000/static/tanchi", "gid": 2, "gname": "\u8d2a\u5403\u86c7\u5927\u4f5c\u6218", "image": "http://127.0.0.1:5000/static/tanchi.png", "name": "tanchi", "note": null, "star": 0, "version": "1.0" } ] | 包含游戏信息的json数据                 |
| 新增游戏<br />（仅测试数据使用）           | http://106.13.236.185:5000/api/game/add_game      | gname<br />name<br />filename<br />image<br />note<br />version<br />star<br />status | 游戏名<br />逻辑名<br />文件名<br />图片名<br />简介<br />版本<br />星级<br />审核状态 | success<br />repeat<br />failed                              | 新增成功<br />逻辑名重复<br />新增失败 |

