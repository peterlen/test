
import arcpy
import sys

fc = r"C:\ZMain\programming\GISData\Polys.gdb\antarctic"

def main():
    
    array = arcpy.Array()

    latStart = -57
    array.add(arcpy.Point(-180.0, latStart))  # Starting coordinate

    # Sets the bottom part (flat) of the extent
    for i in range(-180, 180, 1):
        array.add(arcpy.Point(i, -89.9))

    # Sets the upper part with varying latitudes
    ls = latStart

    # innerChange (45 degree ring and down):
    # Template shows a lat of latStart at 180 & -180 long.  The boundary
    # is flat until about longitude 135 / -135 and 45 / -45 where it meets
    # the ~45 latitude mark.  That is roughly 45 degrees longitude for roughly
    # 12 degrees latitude.  As we move each degree of longitude for those
    # 45 degrees, we must increase or decrease the latitude by roughly .266
    # degrees.
    # 12 / 45 = ~.266666666
    #
    # outerChange1 (45 degree ring to corner):
    # Corner is roughly at 125 / -125 longitude and 35 / -35 latitude which
    # is roughly 10 degrees in both lat and long from the innerChange area.
    # This means a 1 degree plus / minus
    #
    # outerChange2 (corner to corner vertically)
    # Corner is roughly at 125 / -125 longitude and 35 / -35 latitude. The
    # 90 / -90 longitude on template is roughly at 44 / -44 latidue.  This is
    # a 35 degree longitude change for a 9 degree latitude change.
    # 9 / 35 = ~.257
    
    innerChange = .266
    outerChange2 = .257
    outerChange1 = 1
    for i in range(180, -180, -1):
        lat = -45

        # Handles Top and Bottom sides of template extent
        if i <= 180 and i >= 135:
            ls = ls + innerChange
            lat = ls
            
        elif i <= 45 and i >= 0:
            if i == 45: ls = -45  # Set accordingly
            ls = ls - innerChange
            lat = ls

        elif i <= 0 and i >= -45:
            if i == 0: ls = -57  # Set accordingly
            ls = ls + innerChange
            lat = ls
            
        elif i <= -135:
            if i == -135: ls = -45  # Set accordingly
            ls = ls - innerChange
            lat = ls

        # Handles Right side of template extent
        elif i <= 134 and i >= 125:
            if i == 134: ls = -45  # Set accordingly
            ls = ls + outerChange1
            lat = ls

        elif i <= 124 and i >= 90:
            if i == 124: ls = -35  # Set accordingly
            ls = ls - outerChange2
            lat = ls

        elif i <= 89  and i >= 55:
            if i == 89: ls = -44  # Set accordingly
            ls = ls + outerChange2
            lat = ls

        elif i <= 54  and i >= 46:
            if i == 54: ls = -35 # Set accordingly
            ls = ls - outerChange1
            lat = ls

        # Handles Left side of template extent
        elif i <= -125 and i >= -134:
            if i == -125: ls = -35  # Set accordingly
            ls = ls - outerChange1
            lat = ls

        elif i <= -90 and i >= -124:
            if i == -90: ls = -44  # Set accordingly
            ls = ls + outerChange2
            lat = ls

        elif i <= -55  and i >= -89:
            if i == -55: ls = -35  # Set accordingly
            ls = ls - outerChange2
            lat = ls

        elif i <= -46  and i >= -54:
            if i == -46: ls = -45 # Set accordingly
            ls = ls + outerChange1
            lat = ls

            
        array.add(arcpy.Point(i, lat))    
    
    poly = arcpy.Polygon(array)

    icur = arcpy.InsertCursor(fc)
    row = icur.newRow()
    row.shape = poly
    icur.insertRow(row)

    del row
    del icur

    print "DONE"

def deleteit():
    icur = arcpy.UpdateCursor(fc)
    for row in icur:
        icur.deleteRow(row)
    del row
    del icur
    
    print "Deleted"

try:
    if len(sys.argv) == 2:
        deleteit()
    else:
        main()
except Exception as err:
    print "ERROR: " + str(err)
