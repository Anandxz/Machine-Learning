from pydantic import BaseModel
from typing import Optional , List,Dict,Annotated,Feild

field_name: Optional[str] = None
 

class Patient(BaseModel):
    
    name : Annotated[str, Feild(max_lenght=50,title="Name of the patient")]
    age : int
    weight : float
    married : Optional[bool]=None

    

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("INserted")

patient_info = {"name":"Anand","age": 30,'weight':23.3,'married':True,}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)