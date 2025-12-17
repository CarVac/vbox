from build123d import *
from math import sqrt

clearance = 0.4 * MM
clearance2 = 2 * clearance
switch_wd = (4.8 * MM) + clearance2
switch_ln = (7.04 * 2 * MM) + clearance2
switch_ht = 2.4 * MM + clearance

presser_dia = 1.5 * MM
presser_ht = switch_ht - clearance

cap_width = 15.5 * MM
cap_big_thick = 10 * MM
min_thick = 2 * MM

sculpt_radius = 35 * MM
sculpt_center = switch_ht+min_thick+sculpt_radius

fillet_rad = 1 * MM

#the base size of the cap
cap = Pos(0, 0, cap_big_thick/2) * Box(cap_width, cap_width, cap_big_thick)


#cylindrical sculpting of top
cap1 = cap - Pos(0, cap_width, sculpt_center) * Rot(x=90) * extrude(Circle(sculpt_radius), amount=2*cap_width)
cap2 = cap - Pos(0, cap_width, sculpt_center+1.2*MM) * Rot(x=90) * extrude(Circle(sculpt_radius), amount=2*cap_width)

#apply fillets
cap1 = fillet(cap1.edges().sort_by(Axis.Z)[-8:], radius=fillet_rad)
cap2 = fillet(cap2.edges().sort_by(Axis.Z)[-8:], radius=fillet_rad)

#the wings that hold the cap down
wings = Pos(0, 0, 0.5*MM) * chamfer(Box(cap_width, cap_width+2*MM, 1*MM)
                                   .edges().sort_by(Axis.Z)[-8:-4],
                                   length=.6*MM)

cap1 += wings
cap2 += wings

#x-shaped cutout for switch
cutout = Rot(z=45) * Pos(0, 0, switch_ht/2) * Box(switch_wd, switch_ln, switch_ht)
cutout += Rot(z=-45) * Pos(0, 0, switch_ht/2) * Box(switch_wd, switch_ln, switch_ht)
cutout = chamfer(cutout.edges().sort_by(Axis.Z)[12:24], length=0.4*MM)

#chamfer for printability of x
cutout += extrude(RegularPolygon(0.80*switch_wd*1.415, side_count=8, rotation=22.5), amount=switch_ht, taper=30)

#presser for nub
cutout -= Pos(0, 0, presser_ht - 0.1*MM) * extrude(Circle(presser_dia), amount=clearance2, taper=-45)

#shave off the top and bottom of the print to reduce its width to 15.4 and to improve printability
cutout += Pos(cap_width/2, 0, 0) * Box(0.1*MM, cap_width*2, cap_big_thick*2)
cutout += Pos(-cap_width/2, 0, 0) * Box(0.1*MM, cap_width*2, cap_big_thick*2)

cap1 -= cutout;
cap2 -= cutout;

#test surround
unit = 19*MM
cap_width_plus = cap_width + 0.6*MM
wing_ht_clearance = 1.6 * MM + 3*MM - presser_ht
wing_length_clearance = cap_width_plus+2*MM
wing_width_clearance = cap_width_plus+1*MM#-2*MM
surround_ht = wing_ht_clearance*2
surround_wd = 19*2*MM - cap_width_plus
button_frame_wd = 20 * MM
pcb_hole_wd = 18 * MM
pcb_thick = 1.6 * MM

cap_hole = Pos(0, 0, surround_ht/2) * Box(cap_width_plus, cap_width_plus, surround_ht)
cap_hole += Pos(0, 0, wing_ht_clearance/2) * Box(wing_width_clearance, wing_length_clearance, wing_ht_clearance)
button_frame = Pos(0, 0, surround_ht/2-pcb_thick/2) * Box(button_frame_wd, button_frame_wd, surround_ht+pcb_thick)
pcb_hole = Pos(0, 0, -pcb_thick) * Box(pcb_hole_wd+.2, pcb_hole_wd, pcb_thick*2)
#                                                   ^ make the hole a bit wider so that the press fit is only vertical
dogbone_rad = 0.4 * MM
dogbone_off = dogbone_rad / sqrt(2)
pcb_hole_topright = pcb_hole + Pos(pcb_hole_wd*.5+.1 - dogbone_off, pcb_hole_wd*.5 - dogbone_off, -pcb_thick) * Cylinder(dogbone_rad+0.1, pcb_thick*2)
pcb_dogbone_topright = fillet(pcb_hole_topright.edges().sort_by(Axis.Z)[5:10], 4*MM)
pcb_dogbone_topleft = mirror(pcb_dogbone_topright, Plane.YZ)
pcb_dogbone_botright = mirror(pcb_dogbone_topright, Plane.XZ)
pcb_dogbone_botleft = mirror(pcb_dogbone_topleft, Plane.XZ)

#frame for thumbs
leftthumb  = Pos(0.0*unit,  0.0*unit, 0) * button_frame
leftthumb += Pos(0.0*unit, -0.5*unit, 0) * button_frame #extra fill
leftthumb += Pos(1.0*unit,  0.5*unit, 0) * button_frame
leftthumb += Pos(1.0*unit, -0.5*unit, 0) * button_frame
leftthumb += Pos(2.0*unit,  0.0*unit, 0) * button_frame
leftthumb += Pos(2.0*unit, -1.0*unit, 0) * button_frame
#round corners
leftthumb = fillet(leftthumb.edges().sort_by(Axis.Z)[12:20], radius=fillet_rad)
#centered holes for pcb
leftthumbpcb =  Pos(0.0*unit,  0.0*unit, 0) * (pcb_hole + pcb_dogbone_topleft)
leftthumbpcb += Pos(0.0*unit, -0.5*unit, 0) * pcb_hole
leftthumbpcb += Pos(1.0*unit,  0.5*unit, 0) * (pcb_hole + pcb_dogbone_topleft + pcb_dogbone_topright)
leftthumbpcb += Pos(1.0*unit, -0.5*unit, 0) * pcb_hole
leftthumbpcb += Pos(2.0*unit,  0.0*unit, 0) * (pcb_hole + pcb_dogbone_topright)
leftthumbpcb += Pos(2.0*unit, -1.0*unit, 0) * (pcb_hole + pcb_dogbone_botleft + pcb_dogbone_botright)
#clearing the ribs
leftthumbpcb += Pos(0.1*unit,  0.0*unit, 0) * pcb_hole
leftthumbpcb += Pos(0.1*unit, -0.5*unit, 0) * pcb_hole
leftthumbpcb += Pos(1.0*unit,  0.4*unit, 0) * pcb_hole
leftthumbpcb += Pos(1.1*unit, -0.5*unit, 0) * pcb_hole
leftthumbpcb += Pos(1.9*unit,  0.0*unit, 0) * pcb_hole
leftthumbpcb += Pos(2.0*unit, -0.9*unit, 0) * pcb_hole
#slot for the connector protrusion
leftthumbpcb += Pos(-0.5*unit, (2.75-18.5)/2*MM, -pcb_thick) * Box(unit, (2.75+18.5)*MM, pcb_thick*2)
#fillet the inside corners
leftthumbpcb = fillet(leftthumbpcb.edges().filter_by(Axis.Z), radius=1.5*MM)

leftthumb -= leftthumbpcb
#mirror for the right thumb
rightthumb = mirror(leftthumb, Plane.YZ)

#frame for fingers
leftfinger  = Pos(0.0*unit,      -1.0*unit, 0) * button_frame
leftfinger += Pos(0.0*unit,      -2.0*unit, 0) * button_frame
leftfinger += Pos(1.0*unit,       0.0*unit, 0) * button_frame
leftfinger += Pos(1.0*unit,      -1.0*unit, 0) * button_frame
leftfinger += Pos(2.0*unit,           6*MM, 0) * button_frame
leftfinger += Pos(2.0*unit,         -13*MM, 0) * button_frame
leftfinger += Pos(3.0*unit,       0.0*unit, 0) * button_frame
leftfinger += Pos(3.0*unit,      -1.0*unit, 0) * button_frame
leftfinger += Pos(3.5*unit,       0.0*unit, 0) * button_frame #extra fill
leftfinger += Pos(4.0*unit+4*MM,  0.0*unit, 0) * button_frame
#round corners
leftfinger = fillet(leftfinger.edges().sort_by(Axis.Z)[18:36], radius=fillet_rad)
#centered holes for pcb
leftfingerpcb =  Pos(0.0*unit,      -1.0*unit, 0) * (pcb_hole + pcb_dogbone_topleft)
leftfingerpcb += Pos(0.0*unit,      -2.0*unit, 0) * (pcb_hole + pcb_dogbone_botleft + pcb_dogbone_botright)
leftfingerpcb += Pos(1.0*unit,       0.0*unit, 0) * (pcb_hole + pcb_dogbone_topleft)
leftfingerpcb += Pos(1.0*unit,      -1.0*unit, 0) * (pcb_hole + pcb_dogbone_botright)
leftfingerpcb += Pos(2.0*unit,           6*MM, 0) * (pcb_hole + pcb_dogbone_topleft + pcb_dogbone_topright)
leftfingerpcb += Pos(2.0*unit,         -13*MM, 0) * pcb_hole
leftfingerpcb += Pos(3.0*unit,       0.0*unit, 0) * pcb_hole
leftfingerpcb += Pos(3.0*unit,      -1.0*unit, 0) * (pcb_hole + pcb_dogbone_botleft + pcb_dogbone_botright)
leftfingerpcb += Pos(3.5*unit,       0.0*unit, 0) * pcb_hole
leftfingerpcb += Pos(4.0*unit+4*MM,  0.0*unit, 0) * (pcb_hole + pcb_dogbone_topright + pcb_dogbone_botright)
#clearing the ribs
leftfingerpcb += Pos(0.1*unit,      -1.0*unit, 0) * pcb_hole
leftfingerpcb += Pos(0.0*unit,      -1.9*unit, 0) * pcb_hole
leftfingerpcb += Pos(1.0*unit,       0.0*unit, 0) * pcb_hole
leftfingerpcb += Pos(1.0*unit,      -0.1*unit, 0) * pcb_hole
leftfingerpcb += Pos(1.1*unit,       0.0*unit, 0) * pcb_hole
leftfingerpcb += Pos(1.1*unit,         -13*MM, 0) * pcb_hole
leftfingerpcb += Pos(2.0*unit,       0.0*unit, 0) * pcb_hole
leftfingerpcb += Pos(2.1*unit,       0.0*unit, 0) * pcb_hole
leftfingerpcb += Pos(2.1*unit,         -13*MM, 0) * pcb_hole
leftfingerpcb += Pos(3.0*unit,       0.0*unit, 0) * pcb_hole
leftfingerpcb += Pos(3.0*unit,      -0.1*unit, 0) * pcb_hole
leftfingerpcb += Pos(3.0*unit,      -1.0*unit, 0) * pcb_hole
#slot for the connector protrusion
leftfingerpcb += Pos(-0.5*unit, -19*MM + (6.5-22.5)/2*MM, -pcb_thick) * Box(unit, (6.5+22.5)*MM, pcb_thick*2)
#fillet the inside corners
leftfingerpcb = fillet(leftfingerpcb.edges().filter_by(Axis.Z), radius=1.5*MM)

leftfinger -= leftfingerpcb
#mirror for the right fingers
rightfinger = mirror(leftfinger, Plane.YZ)


#EDIT THESE TO REMOVE BUTTON HOLES
#holes for left thumb
#leftthumb -= Pos(0.0*unit,  0.0*unit, 0) * cap_hole #         (optional) mod5
#leftthumb -= Pos(1.0*unit,  0.5*unit, 0) * cap_hole #         (optional) mod4
leftthumb -= Pos(1.0*unit, -0.5*unit, 0) * cap_hole # modX
#leftthumb -= Pos(2.0*unit,  0.0*unit, 0) * cap_hole #         (optional) mod3
leftthumb -= Pos(2.0*unit, -1.0*unit, 0) * cap_hole # modY
#holes for right thumb
rightthumb -= Pos(-0.0*unit,  0.0*unit, 0) * cap_hole # c_right
rightthumb -= Pos(-1.0*unit,  0.5*unit, 0) * cap_hole # c_up
rightthumb -= Pos(-1.0*unit, -0.5*unit, 0) * cap_hole # A
rightthumb -= Pos(-2.0*unit,  0.0*unit, 0) * cap_hole # c_left
rightthumb -= Pos(-2.0*unit, -1.0*unit, 0) * cap_hole # c_down
#holes for left fingers
#leftfinger -= Pos(0.0*unit     , -1.0*unit, 0) * cap_hole #       (optional) upper pinky
leftfinger -= Pos(0.0*unit     , -2.0*unit, 0) * cap_hole # L
#leftfinger -= Pos(1.0*unit     ,  0.0*unit, 0) * cap_hole #       (optional) upper ring
leftfinger -= Pos(1.0*unit     , -1.0*unit, 0) * cap_hole # left
leftfinger -= Pos(2.0*unit     ,      6*MM, 0) * cap_hole #       (optional) up2
leftfinger -= Pos(2.0*unit     ,    -13*MM, 0) * cap_hole # down
#leftfinger -= Pos(3.0*unit     ,  0.0*unit, 0) * cap_hole #       (optional) upper index
leftfinger -= Pos(3.0*unit     , -1.0*unit, 0) * cap_hole # right
leftfinger -= Pos(4.0*unit+4*MM,  0.0*unit, 0) * cap_hole # start
#holes for left fingers
rightfinger -= Pos(-0.0*unit     , -1.0*unit, 0) * cap_hole # midshield
rightfinger -= Pos(-0.0*unit     , -2.0*unit, 0) * cap_hole # up
rightfinger -= Pos(-1.0*unit     ,  0.0*unit, 0) * cap_hole # lightshield
rightfinger -= Pos(-1.0*unit     , -1.0*unit, 0) * cap_hole # Z
rightfinger -= Pos(-2.0*unit     ,      6*MM, 0) * cap_hole # Y
rightfinger -= Pos(-2.0*unit     ,    -13*MM, 0) * cap_hole # X
rightfinger -= Pos(-3.0*unit     ,  0.0*unit, 0) * cap_hole # R
rightfinger -= Pos(-3.0*unit     , -1.0*unit, 0) * cap_hole # B
#rightfinger -= Pos(-4.0*unit-4*MM,  0.0*unit, 0) * cap_hole #        (optional) start2

cap1.export_step("short_cap.step")
cap2.export_step("tall_cap.step")
leftthumb.export_step("leftthumb.step")
rightthumb.export_step("rightthumb.step")
leftfinger.export_step("leftfinger.step")
rightfinger.export_step("rightfinger.step")

