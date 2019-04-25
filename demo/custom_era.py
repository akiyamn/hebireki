from src import *
from datetime import *

if __name__ == "__main__":

    ''' create a new instance of the Era class. (None as an end date means it is ongoing) '''
    new_era = Era("新時代", "New Era", datetime(2020, 1, 1), None)

    ''' Set the current latest era to end when the new era starts. '''
    Wareki.eras[0].end = new_era.start

    ''' Add the new era to the top (0th position) in the list of eras in the Wareki class. '''
    Wareki.eras.insert(0, new_era)

    # Sample output
    print("Way before: " + str(Wareki(datetime(2000, 1, 1))))
    print("Before: " + str(Wareki(datetime(2019, 12, 31))))
    print("On first day: " + str(Wareki(datetime(2020, 1, 1))))
    print("After: " + str(Wareki(datetime(2030, 1, 1))))
