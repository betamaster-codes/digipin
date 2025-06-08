"""
DIGIPIN Encoder
---------------
This module encodes latitude and longitude into a 10-character alphanumeric
DIGIPIN code based on the Indian National Address Grid specification.

Developed under the DIGIPIN initiative by the Department of Posts, Govt. of India.
"""

def get_digipin(lat, lon):
    """
    Encodes latitude and longitude into a DIGIPIN (Digital Postal Index Number).

    Args:
        lat (float): Latitude in decimal degrees
        lon (float): Longitude in decimal degrees

    Returns:
        str: A 10-character alphanumeric DIGIPIN, or an error message
    """

    # DIGIPIN Labelling Grid
    L = [
        ['F', 'C', '9', '8'],
        ['J', '3', '2', '7'],
        ['K', '4', '5', '6'],
        ['L', 'M', 'P', 'T']
    ]

    # Bounding box covering India
    MinLat, MaxLat = 2.5, 38.5
    MinLon, MaxLon = 63.5, 99.5
    LatDivBy, LonDivBy = 4, 4

    if not (MinLat <= lat <= MaxLat):
        return 'Latitude Out of range'
    if not (MinLon <= lon <= MaxLon):
        return 'Longitude Out of range'

    vDIGIPIN = ''

    for Lvl in range(1, 11):
        LatDivDeg = (MaxLat - MinLat) / LatDivBy
        LonDivDeg = (MaxLon - MinLon) / LonDivBy

        # Find row
        row = 0
        NextLvlMaxLat = MaxLat
        NextLvlMinLat = MaxLat - LatDivDeg
        for x in range(LatDivBy):
            if NextLvlMinLat <= lat < NextLvlMaxLat:
                row = x
                break
            else:
                NextLvlMaxLat = NextLvlMinLat
                NextLvlMinLat = NextLvlMaxLat - LatDivDeg

        # Find column
        column = 0
        NextLvlMinLon = MinLon
        NextLvlMaxLon = MinLon + LonDivDeg
        for x in range(LonDivBy):
            if NextLvlMinLon <= lon < NextLvlMaxLon:
                column = x
                break
            elif (NextLvlMinLon + LonDivDeg) < MaxLon:
                NextLvlMinLon = NextLvlMaxLon
                NextLvlMaxLon = NextLvlMinLon + LonDivDeg
            else:
                column = x

        # Append symbol
        symbol = L[row][column]
        vDIGIPIN += symbol

        if Lvl == 3 or Lvl == 6:
            vDIGIPIN += '-'

        # Update bounding box for next level
        MinLat, MaxLat = NextLvlMinLat, NextLvlMaxLat
        MinLon, MaxLon = NextLvlMinLon, NextLvlMaxLon

    return vDIGIPIN

# Example usage (uncomment for testing):
# if __name__ == "__main__":
#     lat = 22.2433683
#     lon = 73.2019148
#     print(get_digipin(lat, lon))  # Expected: "3LC-L67-647F"
