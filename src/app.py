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