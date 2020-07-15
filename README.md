
http://127.0.0.1:8000/
Allows a get request and list out a single point for the API

http://127.0.0.1:8000/api/questions/
Allows searches based on category , question, users, first name , last name or email
GET request fetches all active question for regular users but fetches both active and inactive questions if user is staff

http://127.0.0.1:8000/api/questions/<int:pk>
PATCH, PUT, DELETE request allows only owner of question to edit question
GET request allows all users view details of the question

http://127.0.0.1:8000/api/answers/
GET request gives a list of questions that have answers (ordered by most recently answered )
POST request gives authenticated users permission to answer any question, question id must be supplied to determine question being answered.

http://127.0.0.1:8000/api/answers/<int:pk>
GET request allows any user view more extensive details about question answered. 
PUT, PATCH , DELETE are only permissible to owner of answer. 
