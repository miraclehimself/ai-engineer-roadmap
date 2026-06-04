from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
	return  {
		"message":  "AI Engineering Workspace Running"
		}
		
@app.get("/health")
def health():
	return {
		"status": "healthy",
		"service": "ai-engineer-roadmap"
	}
	
@app.get("/about")
def about():
	return {
		"owner": "Abiola Miracle Aderiye",
		"goal": "Build production AI Systems"
	}
	
@app.get("/greet")
def greet(name: str):
	return {
		"message": f"Hello {name}, your API is working"
	}
	
@app.get ("/profile")
def profile(name: str, role: str):
	return {
		"name": name,
		"role": role,
		"message": f"{name} is training as {role}"
	}
	
@app.get("/sum")
def calculate(a: int, b: int):
	total = a + b
	
	return {
		"first_number": a,
		"second_number": b,
		"total": total
	}
	
@app.get("/multiply")
def multiply(a:int,b:int):
	answer = a* b
	
	return{
	"a":a,
	"b":b,
	"result":answer
	}
	
@app.get("/age-check")
def age_check(name: str, age: int):
	
	if age < 18:
		return {
			"status": "blocked" ,
			"message": f"{name} is under 18"
		}
		
	return {
		"status": "approved" ,
		"message": f"{name} may continue"
	}
	
@app.get ("/patient-record")
def patient_record(
	name: str,
	nhs_number: str
) :

	if len(nhs_number) != 10:
		return {
			"status" : "failed",
			"reason" : "invalid NHS Number"
		}
		
	return{
		"status" :  "success",
		"patient" : name,
		"nhs_number" : nhs_number
	}