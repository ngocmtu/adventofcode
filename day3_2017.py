s = 347991

# Part 1
# Bottom right corner is the square of the outer length of the memory grid
# If s is smaller than bottom right corner, s is on the layer of the grid with that length
# the shortest route from outer layer to center is distance between the middle point of side and center
# shortest route from s to middle point is distance between s and middle point
def solve_part1(s):
  length = 1
  while length**2 <s:
    length+=2
  halfway_to_1 = (length-1)/2
  
  max_val = length**2
  top_left_corner = (length-2)**2 + length-1
  halfway_point = 0
  
  if s < top_left_corner:
    halfway_point = top_left_corner - ((length-1)/2)
  else:
    while s < max_val:
      max_val = max_val - (length -1)
    halfway_point = (max_val*2 + length - 1)/2
    
  s_to_halfway = s-halfway_point
  return halfway_to_1 + s_to_halfway if s_to_halfway > 0 else halfway_to_1 + s_to_halfway*(-1)


# Part 2
# The code below builds out the spiral memory using a dictionary with coordinates as keys and values as, well, values
d={(0,0):1}

def calc_next(x,y):
  next_cord = (x,y)
  
  # cord of surrounding values
  # if there's a surrounding value, add that the value of the position in examination
  surroundings = [(x,y+1),(x+1,y),(x-1,y),(x,y-1),(x+1,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1)]
  existing_cords = d.keys()
  d[next_cord] = sum([d[each] if each in existing_cords else 0 for each in surroundings])
  return d[next_cord] if d[next_cord] > s else None

def solve_2(s):
  base_x = 0
  base_y = 0
  length=0
  while True:
    length += 1
    # going up left side
    base_x += 1
    for i in range(length):
      result = calc_next(base_x,base_y)
      if not result is None: return result
      base_y += 1
    
    length+=1
    # going left up side
    for i in range(length):
      result = calc_next(base_x,base_y)
      if not result is None: return result
      base_x -= 1
    
    # going down right side
    for i in range(length):
      result = calc_next(base_x,base_y)
      if not result is None: return result
      base_y -= 1
        
    # going right down side
    for i in range(length):
      result = calc_next(base_x,base_y)
      if not result is None: return result
      base_x += 1
        
    # bottom right corner needs separate calculation
    result = calc_next(base_x,base_y)
    if not result is None: return result
      
print(solve_part1(s))
print(solve_part2(s))
