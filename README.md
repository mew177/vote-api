# vote-api

This is an api server based on RESTful framework serving poll service.

Assumptions:
1. Every user is free to vote agree or disagree with an email provided.
2. Every email should only be provided once.

Functionalities:
1. Vote : vote for an opinion for wuhan virus.
	i. send a http POST request with agree = [true/false], email
	ii. e.g. { "agree": true, "email": "example@gmail.com"}
	iii. if "status" = "OK", successfully voted

2. View Result : show result of the poll.
	i. send a GET request or a default visiting
	ii. return counts of disagree / agree

* both api are aggregated in url:'voting/'

Others:
1. This server is set to have limited requests rate of 60 req/mins.
2. Error will be return if quantity of the requests meets.
