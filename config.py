from asteroid import Asteroid

# Asteroid settings
horizontal_postion_start = 400
vertical_postion_start = 500 
horizontal_start_speed_per_frame = 0 # asteroid speed
vertical_speed_per_frame = -8 # negative means upward momentum
asteroid_radius = 25 # size of asteroid * 2 for total diameter

asteroid = Asteroid(horizontal_postion_start, vertical_postion_start, horizontal_start_speed_per_frame, vertical_speed_per_frame, asteroid_radius, image=None) # arguments for Asteroid Class Init

# Levels
levels = {
"level_one" : 2,
"level_two" : 3
}