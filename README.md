# polls-api
api for poll system


administration
http://localhost:8000/admin

#for user


get active polls
http://localhost:8000/api/v1.0/polls/

get user answer
http://localhost:8000/api/v1.0/answers/[user_id]/

post a reply of user
http://localhost:8000/api/v1.0/reply/

Method POST

{
"poll":[poll_id],

"question":[question_id],

"variant":[variant_choice],

"user_id":[user_id or default]
}
