# UDrop Backend

## MySQL

### 数据导入

dump.sql

### 数据库连接配置

创建`connection/mysqlConfig.json`，内容：
```
{
  "host": "YOUR HOST IP",
  "user": "YOUR USER NAME",
  "password": "YOUR PASSWORD",
  "database":"YOUR DATABASE"
}
```

## Redis

需要启动本地Redis，启动参数为默认参数，即6379端口，无密码。

### windows启动

```
cd D:\Program Files\Redis
redis-server.exe redis.windows.conf
```

## Flask

### 启动

```
uwsgi --http-socket :5001 --wsgi-file app.py --callable app &
```

### 接口

#### 1.1 add_new_user

/user/register

- POST
- form: \[name: String, password: String]
- return:
  - user_id: Integer
  - added: Integer: 0, new user added; 1, not added (exist)

#### 1.2 check_existed_user

/user/name

- GET
- param: \[name: String]
- return:
  - "Exist", "Not exist", "Failed"

#### 1.3 get_user_info

/user/basic_info

- GET
- param: \[user_id: Int]
- return: (user_name: String, user_motto: String, learned_days: Int)

#### 1.4 change_user_info

/user/basic_info

- POST
- param: \[user_id: Int, name: String, user_motto: String]
- return: 
  - "Failed", "Success"

#### 1.5 login

/user/login

- POST
- form: \[name: String, password: String]
- return:
  - success: Integer 1 or 0
  - userId: Integer

#### 2.1 get_schedule

/study/schedule

- GET
- param: (user_id: Int)
- return: (new_list: JSONArray, review_list: JSONArray)
  - new_list: 今日所有需要新学的课文，每个课文信息中包含是否已背诵
  - review_list: 今日所有需要复习的课文，每个课文信息中包含是否已背诵

#### 2.2 set_new_schedule

/study/new_schedule

- POST

- param: (user_id: Int, new_schedule: JSONArray) 这里的JSONArray就是你前面返回的古诗列表格式，不用管它是个什么词
- return: (resultCode: Int)
  - 0: failure
  - 1: success

#### 2.3 set_review_schedule

/study/review_schedule

- POST

- param: (user_id: Int, review_schedule: JSONArray)
- return: (resultCode: Int)
  - 0: failure
  - 1: success

#### 3.1 get_text_detail

/passage/detail

- GET

- param: (title: String)
- return: (title: String, author: String, author_info: String, content: String)

#### 3.2 search_text

/poems/search

- GET
- param: (key: String)
- return: (result_list: JSONArray) 诗名或作者与关键词匹配

#### 3.3 random_poems

/poems/random

- GET
- param: (number: Int) 随机返回的数量
- return: (result_list: JSONArray)

#### 4.1 get_collection

/user/collection

- GET

- param: (user_id: Int)
- return: (collection_list: JSONArray)

#### 4.2 remove_collection

/user/collection

- DELETE

- param: (user_id: Int, title: String)
- return:
  - "Failed", "Removed", "No Change"

#### 4.3 add_collection

/user/collection

- POST

- param: (user_id: Int, title: String)
- return:
  - "Failed", "Added", "No Change"

#### 4.4 check_single_collection

/user/check_collection

- GET
- param: (user_id: Int, title: String)
- return:
  - "Failed", "Yes", "No"

#### 5.1 reply

/response

- POST
- param: (user_id: Int, text: String) 用户id和用户语音转成的文本
- return:
  - response: String，需要转成语音的回复
  - is_finished: Bool，true - 会话结束，false - 尚未结束继续进行

