import os

from dotenv import load_dotenv
import requests

from fastapi import FastAPI
from models import Course, Assignments

load_dotenv()
app = FastAPI()
access_token = os.getenv("ACCESS_TOKEN")
base_url = "https://dixietech.instructure.com/api/v1"
headers: dict[str, str] = {"Authorization": f"Bearer {access_token}"}
response = requests.get(url=f"{base_url}/courses", headers=headers)
r_json = response.json()
print()



@app.get("/courses")
async def get_courses() -> list[Course]:
    response = requests.get(url=f"{base_url}/courses", headers=headers)
    r_json = response.json()

    courses: list[Course] = []
    for course_json in r_json:
        course = Course(id=course_json["id"], name=course_json["name"])
        courses.append(course)
    return courses

@app.get("/courses/{course_id}/assignments")
async def get_assignments(course_id: int) -> list[Assignments]:
    
    c = f"{base_url}/courses/{course_id}/assignments?per_page=100"
    a = requests.get(url=c, headers=headers).json()
    assignmets: list[Assignments] = []
    for a_json in a:
        assignment = Assignments(id=a_json["id"], name=a_json["name"])
        assignmets.append(assignment)
    return assignmets 

@app.post("/courses/{course_id}/assignments/{assignment_id}/submit")
async def create_assignemnt(course_id: int, assignment_id: int , submission: str):
    
    
    c = f"{base_url}/courses/{course_id}/assignments/{assignment_id}/submissions"
    d = {"submission[submission_type]": "online_url", "submission[url]": submission}
    
    a = requests.post(url=c, headers=headers, data=d)
    return a.status_code

    
    