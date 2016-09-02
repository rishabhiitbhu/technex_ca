# Api Documentation
## Registration Api

Url: http://localhost:8000/register

Method: POST

Json object Expected : 			//(all fields required)
								{
									"email" : emailOfUser,
									"first_name" : firstName,
									"last_name" : lastName,
									"password" : password,
									"college" : collegeName,
									"year" : year(1,2,3,4,5)
									"mobile_number" : mobileNumber
								 }

Json Response for Successful registration:
								{
								 	"status" : "Profile created successfully"
								}
								 
Json Response for Error in Registration(validation Erorr):
								{
									"status" : "Registration in error",
									"field_name": errorInField //field_name is same as above expected
								}
								 	
Json Response for Invalid Request(requests other than post):
								{
									"Error" : True,
									"status" : "invalid request,Post request Please!"
								}

## Login Api
Url: http://localhost:8000/login

Method: POST

Json object Expected:			{
									"email" : email,
									"password" : password
								}

Json Response for successful Login: 
								{
									"status" : "logged in"
								}

Json Response for wrong Username/password:
								{
									"Error" : True,
									"status" : "Invalid Credentials!"
								}

Json Response for invalid form submission(empty username/password and other validation errors):
								{
									"Error" : True,
									"status" : "Please Fill the form correctly!"
								}					
