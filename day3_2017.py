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
  
print(solve(s))
