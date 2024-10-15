"""
Facade pattern is usually used when we are given an existing third-party API and we want to simplify it or adapt to our
needs in some way. Here (below), we have an external insurance API, which has 2 operations: creating a patient (Patient) and 
filing a new claim for that patient (Claim).
We think it's more convenient to create a facade (InsuranceClaimFacade) that combines these 2 operations into one.
"""


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
