from build123d import *

clearance = 0.2 * MM
clearance2 = 2 * clearance
switch_wd = (4.8 * MM) + clearance2
switch_ln = (7.04 * 2 * MM) + clearance2
switch_ht = 3 * MM + clearance

presser_dia = 1.5 * MM
presser_ht = switch_ht - clearance

cap_width = 15.5 * MM
cap_big_thick = 10 * MM
min_thick = 1.2 * MM

sculpt_radius = 25 * MM
sculpt_center = switch_ht+min_thick+sculpt_radius

fillet_rad = 1 * MM

#the base size of the cap
cap = Pos(0, 0, cap_big_thick/2) * Box(cap_width, cap_width, cap_big_thick)

#the wings that hold the cap down
cap += Pos(0, 0, 0.5*MM) * chamfer(Box(cap_width-2*MM, cap_width+2*MM, 1*MM)
                                   .edges().sort_by(Axis.Z)[-8:-4],
                                   length=1.5*MM)

#cylindrical sculpting of top
cap1 = cap - Pos(0, cap_width, sculpt_center) * Rot(x=90) * extrude(Circle(sculpt_radius), amount=2*cap_width)
cap2 = cap - Pos(0, cap_width, sculpt_center+min_thick) * Rot(x=90) * extrude(Circle(sculpt_radius), amount=2*cap_width)

#apply fillets
cap1 = fillet(cap1.edges().sort_by(Axis.Z)[-8:], radius=fillet_rad)
cap2 = fillet(cap2.edges().sort_by(Axis.Z)[-8:], radius=fillet_rad)

#x-shaped cutout for switch
cutout = Rot(z=45) * Pos(0, 0, switch_ht/2) * Box(switch_wd, switch_ln, switch_ht)
cutout += Rot(z=-45) * Pos(0, 0, switch_ht/2) * Box(switch_wd, switch_ln, switch_ht)
cutout = chamfer(cutout.edges().sort_by(Axis.Z)[12:24], length=0.4*MM)

#chamfer for printability of x
cutout += extrude(RegularPolygon(0.86*switch_wd*1.415, side_count=8, rotation=22.5), amount=switch_ht, taper=30)

#presser for nub
cutout -= Pos(0, 0, presser_ht) * extrude(Circle(presser_dia), amount=clearance2, taper=-45)

cap1 -= cutout;
cap2 -= cutout;

cap1.export_stl("short_cap.stl")
cap2.export_stl("tall_cap.stl")
