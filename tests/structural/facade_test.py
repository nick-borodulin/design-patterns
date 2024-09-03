from design_patterns.structural.facade import InsuranceClaimFacade

def test_insurance_claim_facade() -> None:
    facade = InsuranceClaimFacade()
    assert facade.submit_claim("John Doe") == "claim_submit"