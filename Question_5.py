#NAME : HASSAN ADNAN
#UCID: 30217418

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):


    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:  # Validation for input
        return "Radii should be a positive integers"

   # Calculating areas
    pi = 3.14159
    areaOfCircle1 = pi * radiusOfCircle1 * radiusOfCircle1
    areaOfCircle2 = pi * radiusOfCircle2 * radiusOfCircle2

    if areaOfCircle1 < areaOfCircle2:
        smaller = areaOfCircle1
        larger = areaOfCircle2
    else:
        smaller = areaOfCircle2
        larger = areaOfCircle1

    percentage = (smaller / larger) * 100

    return percentage
