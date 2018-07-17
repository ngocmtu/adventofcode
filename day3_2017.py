s = 347991
def solve(s):
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

d={(0,0):1}

# TODO
# up left, right down, down right all need 4 inputs instead of just three

def calc_next(x,y,i,direction):
  next_cord = (x,y)
  print('next cord '+str(next_cord))
  print('i '+str(i))
  
  if x == 1 and y == 0:
    d[next_cord] = 1
  elif direction == 'left_up':
    d[next_cord] = d[(next_cord[0],next_cord[1]-1)] + d[(next_cord[0]-1,next_cord[1])] + d[(next_cord[0]-1,next_cord[1]-1)] if i>0 else d[(next_cord[0]-1,next_cord[1]-1)] + d[(next_cord[0]-1,next_cord[1])]
  elif direction == 'up_left':
    d[next_cord] = d[(next_cord[0]-1,next_cord[1]-1)] + d[(next_cord[0],next_cord[1]-1)] + d[(next_cord[0],next_cord[1]-1)] if i>0 else d[(next_cord[0]-1,next_cord[1]-1)] + d[(next_cord[0],next_cord[1]-1)]
  elif direction == 'right_down':
    d[next_cord] = d[(next_cord[0]-1,next_cord[1]-1)] + d[(next_cord[0]-1,next_cord[1])] + d[(next_cord[0]-1,next_cord[1]+1)] if i>0 else d[(next_cord[0]-1,next_cord[1]-1)] + d[(next_cord[0]-1,next_cord[1])]
  elif direction == 'down_right':
    d[next_cord] = d[(next_cord[0]-1,next_cord[1]-1)] + d[(next_cord[0],next_cord[1]-1)] + d[(next_cord[0]+1,next_cord[1]-1)] if i>0 else d[(next_cord[0],next_cord[1]-1)] + d[(next_cord[0]+1,next_cord[1]-1)]
  elif direction == 'corner':
    d[next_cord] = d[(next_cord[0]-1,next_cord[1]+1)] + d[(next_cord[0],next_cord[1]+1)] + d[(next_cord[0]-1,next_cord[1])]
  print(str(d))
  print('next_cord after conditional '+str(next_cord))
  if d[next_cord] > s:
    return d[next_cord]
  else:
    return None

def solve_2(s):
  answer_not_found = True
  base_cord_x = 0
  base_cord_y = 0
  length=1
  while answer_not_found:
    length += 2
    # going up left side
    base_cord_x += 1
    for i in range(length-2):
      base_cord_y += i
      print('base y '+str(base_cord_y))
      print('i step '+str(i))
      result = calc_next(base_cord_x,base_cord_y,i,'left_up')
      if not result is None:
        answer_not_found = False
        return result
    
    # going left up side
    base_cord_y += 1
    for i in range(length-1):
      base_cord_x -= i
      calc_next(base_cord_x,base_cord_y,i,'up_left')
      if not result is None:
        answer_not_found = False
        return result
    
    # going down right side
    base_cord_x -= 1
    for i in range(length-1):
      base_cord_y -= i
      calc_next(base_cord_x,base_cord_y,i,'right_down')
      if not result is None:
        answer_not_found = False
        return result
        
    # going right down side
    base_cord_y -=1
    for i in range(length-1):
      base_cord_x += i
      calc_next(base_cord_x,base_cord_y,i,'down_right')
      if not result is None:
        answer_not_found = False
        return result
        
    # bottom right corner needs separate calculation
    base_cord_x += 1
    calc_next(base_cord_x,base_cord_y,0,'corner')
    if not result is None:
      answer_not_found = False
      return result
  
print(solve(s))
