from fastapi import FastAPI , Path ,HTTPException


app = FastAPI()


@app.get("/")



@app.get('/about')
def about():
    return {'message':"This is the seconf api "}

def 

@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., description ='Id of the patient',example = 'P100343')):
    # loading all data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient Not found")
            HTTPException()
    
