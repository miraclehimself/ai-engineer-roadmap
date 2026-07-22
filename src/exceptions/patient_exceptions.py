class PatientNotFoundException(Exception):
    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        super().__init__(f"Patient '{patient_id}' was not found")