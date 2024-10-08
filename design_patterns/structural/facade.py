class Patient:
    def create(self, name: str) -> str:
        return f"patient_create_{name}"


class Claim:
    def submit(self, patient: Patient) -> str:
        return "claim_submit"


class InsuranceClaimFacade:
    def submit_claim(self, patient_name: str) -> str:
        patient = Patient()
        patient.create(patient_name)
        claim = Claim()
        return claim.submit(patient)
