#!/usr/bin/env python3

from user import User
from post import Post

app_user_one = User("test@user.com", "Test User", "pwd", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("test@user2.com", "Test User2", "pwd", "DevOps Engineer")
app_user_two.get_user_info()

new_post = Post("On a secret mission today", app_user_two.name)
new_post.get_post_info()
