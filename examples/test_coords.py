from digipin_encoder import get_digipin

def test_known_location():
    code = get_digipin(28.6139, 77.2090)
    assert code == "39J-438-TJC7", f"Unexpected DIGIPIN: {code}"

test_known_location()
