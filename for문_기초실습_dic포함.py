#for문 실습예제

users = {'Hans':'active','Eleonore':'inactive','홍길동':'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status



