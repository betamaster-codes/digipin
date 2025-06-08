"""
DIGIPIN Decoder
---------------
This module decodes a 10-character alphanumeric DIGIPIN code back into a
bounding box (min/max latitude and longitude) and center coordinate.

Developed under the DIGIPIN initiative by the Department of Posts, Govt. of India.
"""

def decode_digipin(digipin):
    """
    Decodes a 10-character DIGIPIN code into a bounding box and center coordinates.

    Args:
        digipin (str): The DIGIPIN code (e.g., "3LC-L67-647F")

    Returns:
        dict: A dictionary with bounding box and center lat/lon
    """
    digipin = digipin.replace('-', '').upper()
    
    if len(digipin) != 10:
        return {"error": "Invalid DIGIPIN length. Expected 10 characters."}

    # DIGIPIN Labelling Grid
    L = [
        ['F', 'C', '9', '8'],
        ['J', '3', '2', '7'],
        ['K', '4', '5', '6'],
        ['L', 'M', 'P', 'T']
    ]

    MinLat, MaxLat = 2.5, 38.5
    MinLon, MaxLon = 63.5, 99.5
    LatDivBy, LonDivBy = 4, 4

    for symbol in digipin:
        try:
            row, column = next(
                (i, j) for i, row_ in enumerate(L) for j, val in enumerate(row_) if val == symbol
            )
        except StopIteration:
            return {"error": f"Invalid DIGIPIN symbol: '{symbol}'"}

        LatDivDeg = (MaxLat - MinLat) / LatDivBy
        LonDivDeg = (MaxLon - MinLon) / LonDivBy

        # Update bounding box
        MaxLat = MaxLat - row * LatDivDeg
        MinLat = MaxLat - LatDivDeg
        MinLon = MinLon + column * LonDivDeg
        MaxLon = MinLon + LonDivDeg

    # Compute center of bounding box
    center_lat = (MinLat + MaxLat) / 2
    center_lon = (MinLon + MaxLon) / 2

    return {
        "bounding_box": {
            "min_lat": MinLat, "max_lat": MaxLat,
            "min_lon": MinLon, "max_lon": MaxLon
        },
        "center": {
            "latitude": center_lat,
            "longitude": center_lon
        }
    }


# Example usage (uncomment for testing):
# if __name__ == "__main__":
#     result = decode_digipin("3LC-L67-647F")
#     print(result)
