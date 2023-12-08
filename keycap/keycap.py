from build123d import *

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

#the wings that hold the cap down
cap += Pos(0, 0, 0.5*MM) * chamfer(Box(cap_width-2*MM, cap_width+2*MM, 1*MM)
                                   .edges().sort_by(Axis.Z)[-8:-4],
                                   length=1.5*MM)

#cylindrical sculpting of top
cap1 = cap - Pos(0, cap_width, sculpt_center) * Rot(x=90) * extrude(Circle(sculpt_radius), amount=2*cap_width)
cap2 = cap - Pos(0, cap_width, sculpt_center+1.2*MM) * Rot(x=90) * extrude(Circle(sculpt_radius), amount=2*cap_width)

#apply fillets
cap1 = fillet(cap1.edges().sort_by(Axis.Z)[-8:], radius=fillet_rad)
cap2 = fillet(cap2.edges().sort_by(Axis.Z)[-8:], radius=fillet_rad)

#x-shaped cutout for switch
cutout = Rot(z=45) * Pos(0, 0, switch_ht/2) * Box(switch_wd, switch_ln, switch_ht)
cutout += Rot(z=-45) * Pos(0, 0, switch_ht/2) * Box(switch_wd, switch_ln, switch_ht)
cutout = chamfer(cutout.edges().sort_by(Axis.Z)[12:24], length=0.4*MM)

#chamfer for printability of x
cutout += extrude(RegularPolygon(0.80*switch_wd*1.415, side_count=8, rotation=22.5), amount=switch_ht, taper=30)

#presser for nub
cutout -= Pos(0, 0, presser_ht) * extrude(Circle(presser_dia), amount=clearance2, taper=-45)

#test surround
unit = 19*MM
cap_width_plus = cap_width + 0.6*MM
wing_ht_clearance = 1.6 * MM + 3*MM - presser_ht
wing_length_clearance = cap_width_plus+2*MM
wing_width_clearance = cap_width_plus-2*MM
surround_ht = wing_ht_clearance*2
surround_wd = 19*2*MM - cap_width_plus
button_frame_wd = 20 * MM
pcb_hole_wd = 18 * MM
pcb_thick = 1.6 * MM

cap_hole = Pos(0, 0, surround_ht/2) * Box(cap_width_plus, cap_width_plus, surround_ht)
cap_hole += Pos(0, 0, wing_ht_clearance/2) * Box(wing_width_clearance, wing_length_clearance, wing_ht_clearance)
button_frame = Pos(0, 0, surround_ht/2-pcb_thick/2) * Box(button_frame_wd, button_frame_wd, surround_ht+pcb_thick)
pcb_hole = Pos(0, 0, -pcb_thick) * Box(pcb_hole_wd, pcb_hole_wd, pcb_thick*2)

#frame
leftthumb  = Pos(0.0*unit,  0.0*unit, 0) * button_frame
leftthumb += Pos(0.0*unit, -0.5*unit, 0) * button_frame
leftthumb += Pos(1.0*unit,  0.5*unit, 0) * button_frame
leftthumb += Pos(1.0*unit, -0.5*unit, 0) * button_frame
leftthumb += Pos(2.0*unit,  0.0*unit, 0) * button_frame
leftthumb += Pos(2.0*unit, -1.0*unit, 0) * button_frame
#round corners
leftthumb = fillet(leftthumb.edges().sort_by(Axis.Z)[12:20], radius=fillet_rad)
#centered holes for pcb
leftthumb -= Pos(0.0*unit,  0.0*unit, 0) * pcb_hole
leftthumb -= Pos(0.0*unit, -0.5*unit, 0) * pcb_hole
leftthumb -= Pos(1.0*unit,  0.5*unit, 0) * pcb_hole
leftthumb -= Pos(1.0*unit, -0.5*unit, 0) * pcb_hole
leftthumb -= Pos(2.0*unit,  0.0*unit, 0) * pcb_hole
leftthumb -= Pos(2.0*unit, -1.0*unit, 0) * pcb_hole
#clearing the ribs
leftthumb -= Pos(0.1*unit,  0.0*unit, 0) * pcb_hole
leftthumb -= Pos(0.1*unit, -0.5*unit, 0) * pcb_hole
leftthumb -= Pos(1.0*unit,  0.4*unit, 0) * pcb_hole
leftthumb -= Pos(1.1*unit, -0.5*unit, 0) * pcb_hole
leftthumb -= Pos(1.9*unit,  0.0*unit, 0) * pcb_hole
leftthumb -= Pos(2.0*unit, -0.9*unit, 0) * pcb_hole
#slot for the connector protrusion
leftthumb -= Pos(-0.5*unit, (2.5-18.5)/2, -pcb_thick) * Box(unit, 21*MM, pcb_thick*2)
#mirror for the right thumb
rightthumb = mirror(leftthumb, Plane.YZ)


#EDIT THESE TO REMOVE BUTTON HOLES
#holes for left thumb
leftthumb -= Pos(0.0*unit,  0.0*unit, 0) * cap_hole # mod5
leftthumb -= Pos(1.0*unit,  0.5*unit, 0) * cap_hole # mod4
leftthumb -= Pos(1.0*unit, -0.5*unit, 0) * cap_hole # modX
leftthumb -= Pos(2.0*unit,  0.0*unit, 0) * cap_hole # mod3
leftthumb -= Pos(2.0*unit, -1.0*unit, 0) * cap_hole # modY
#holes for right thumb
rightthumb -= Pos(-0.0*unit,  0.0*unit, 0) * cap_hole # c_right
rightthumb -= Pos(-1.0*unit,  0.5*unit, 0) * cap_hole # c_up
rightthumb -= Pos(-1.0*unit, -0.5*unit, 0) * cap_hole # A
rightthumb -= Pos(-2.0*unit,  0.0*unit, 0) * cap_hole # c_left
rightthumb -= Pos(-2.0*unit, -1.0*unit, 0) * cap_hole # c_down

cap1 -= cutout;
cap2 -= cutout;

cap1.export_stl("short_cap.stl")
cap2.export_stl("tall_cap.stl")
leftthumb.export_stl("leftthumb.stl")
rightthumb.export_stl("rightthumb.stl")

