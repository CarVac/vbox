from build123d import *
from math import sqrt


#test surround
unit = 19*MM
height = 5*MM
hole_width = 14*MM
clearance_width = 15*MM
plate_thick = 1.4*MM

cap_hole  = Pos(0, 0, height/2) * Box(hole_width, hole_width, height)
cap_hole += Pos(0, 0, height/2-plate_thick/2) * Box(clearance_width, clearance_width, height-plate_thick)
button_frame = Pos(0, 0, height/2) * Box(unit, unit, height)

#frame for thumbs
leftthumb  = Pos(0.0*unit,  0.0*unit, 0) * button_frame
leftthumb += Pos(0.0*unit, -0.5*unit, 0) * button_frame #extra fill
leftthumb += Pos(1.0*unit,  0.5*unit, 0) * button_frame
leftthumb += Pos(1.0*unit, -0.5*unit, 0) * button_frame
leftthumb += Pos(2.0*unit,  0.0*unit, 0) * button_frame
leftthumb += Pos(2.0*unit, -1.0*unit, 0) * button_frame

#mirror for the right thumb
rightthumb = mirror(leftthumb, Plane.YZ)

#frame for fingers
#leftfinger  = Pos(0.0*unit,         -14*MM, 0) * button_frame
leftfinger  = Pos(0.0*unit,         -33*MM, 0) * button_frame
#leftfinger += Pos(1.0*unit,       0.0*unit, 0) * button_frame
leftfinger += Pos(1.0*unit,      -1.0*unit, 0) * button_frame
leftfinger += Pos(2.0*unit,           4*MM, 0) * button_frame
leftfinger += Pos(2.0*unit,         -15*MM, 0) * button_frame
leftfinger += Pos(3.0*unit,       0.0*unit, 0) * button_frame
leftfinger += Pos(3.0*unit,      -1.0*unit, 0) * button_frame
leftfinger += Pos(3.5*unit,       0.0*unit, 0) * button_frame #extra fill
leftfinger += Pos(4.0*unit+4*MM,  0.0*unit, 0) * button_frame

mrightfinger  = Pos(0.0*unit,         -14*MM, 0) * button_frame
mrightfinger += Pos(0.0*unit,         -33*MM, 0) * button_frame
mrightfinger += Pos(1.0*unit,       0.0*unit, 0) * button_frame
mrightfinger += Pos(1.0*unit,      -1.0*unit, 0) * button_frame
mrightfinger += Pos(2.0*unit,           4*MM, 0) * button_frame
mrightfinger += Pos(2.0*unit,         -15*MM, 0) * button_frame
mrightfinger += Pos(3.0*unit,       0.0*unit, 0) * button_frame
mrightfinger += Pos(3.0*unit,      -1.0*unit, 0) * button_frame

#mirror for the right fingers
rightfinger = mirror(mrightfinger, Plane.YZ)


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
leftfinger -= Pos(0.0*unit     ,    -33*MM, 0) * cap_hole # L
leftfinger -= Pos(1.0*unit     , -1.0*unit, 0) * cap_hole # left
#leftfinger -= Pos(2.0*unit     ,      4*MM, 0) * cap_hole #       (optional) up2
leftfinger -= Pos(2.0*unit     ,    -15*MM, 0) * cap_hole # down
leftfinger -= Pos(3.0*unit     , -1.0*unit, 0) * cap_hole # right
leftfinger -= Pos(4.0*unit+4*MM,  0.0*unit, 0) * cap_hole # start
#holes for left fingers
rightfinger -= Pos(-0.0*unit     ,    -14*MM, 0) * cap_hole # midshield
rightfinger -= Pos(-0.0*unit     ,    -33*MM, 0) * cap_hole # up
rightfinger -= Pos(-1.0*unit     ,  0.0*unit, 0) * cap_hole # lightshield
rightfinger -= Pos(-1.0*unit     , -1.0*unit, 0) * cap_hole # Z
rightfinger -= Pos(-2.0*unit     ,      4*MM, 0) * cap_hole # Y
rightfinger -= Pos(-2.0*unit     ,    -15*MM, 0) * cap_hole # X
rightfinger -= Pos(-3.0*unit     ,  0.0*unit, 0) * cap_hole # R
rightfinger -= Pos(-3.0*unit     , -1.0*unit, 0) * cap_hole # B

leftthumb.export_step("mx_thumb_left.step")
rightthumb.export_step("mx_thumb_right.step")
leftfinger.export_step("mx_finger_left.step")
rightfinger.export_step("mx_finger_right.step")

