xa = int(input("please enter the coordinates of the segment XA :"))
ya = int(input("please enter the coordinates of the segment YA :"))
xb = int(input("please enter the coordinates of the segment XB :"))
yb = int(input("please enter the coordinates of the segment YB :"))
xc = int(input("please enter the coordinates of the segments XC :"))
yc = int(input("please enter the coordinates of the segment YC :"))


def distance(xa, ya, xb, yb, xc, yc):
    segment_ab = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
    segment_bc = ((xc - xb) ** 2 + (yc - yb) ** 2) ** 0.5
    segment_ac = ((xc - xa) ** 2 + (yc - ya) ** 2) ** 0.5
    if segment_ab < segment_bc and segment_ab < segment_ac:
        return "segment_ab"
    elif segment_bc < segment_ac:
        return segment_bc
    else:
        return segment_ac


print("the shortest segment is: ", distance(xa, ya, xb, yb, xc, yc))
