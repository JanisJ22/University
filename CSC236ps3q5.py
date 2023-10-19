# define variables as "x_i", where i is a natural number
# define operators as either '∧' or '∨'
# define p as a formula, it can either one of:
#   - a variable ('x_i'), where i is a natural number
#   - a tuple of 2 elements ('¬', q), where q is a formula. This stands for ¬(p)
#   - a tuple of 3 elements (q_1, <operator>, q_2), where q_1 and q_2 are formulas
# define size(p) as the number of '¬', variables, and operators in p, where p is a formula
# by this definition os size, from the definition of p above, we have:
#   - size('x_i') = 1
#   - size(p) = 1 + size(q)
#   - size(p) = size(q_1) + 1 + size(q_2)
def T(p):
  # returns a tuple, with all negation only on variables
  if isinstance(p, str):
    # p is a variable, this is a base case where size(p) = 1
    return (p,)

  if p[0] == '¬':
    # p is a tuple of two elements and p[1] is a formula or variable

    if (isinstance(p[1], str)):
      # p[1] is a variable
      return (f"¬{p[1]}",)

    # p[1] is a formula, but not a variable
    # note that since size(p[1]) = size(p[1][0]) + 1 (operator) + size(p[1][2]), both recursive calls are
    #   made for smaller "size" (i.e. size(p[1][0] < size(p[1]) and size(p[1][2] < size(p[1])))
    firstFormula = T(('¬',) + (p[1][0],))
    secondFormula = T(('¬',) + (p[1][2],))
    if p[1][1] == '∧':
      return (firstFormula, '∨', secondFormula)
    elif p[1][1] == '∨':
      return (firstFormula, '∧', secondFormula)

  # p is a tuple of 3 elements where p[0] is a formula, p[1] is either '∧' or '∨', and p[2] is a formula
  # note that since size(p) = size(p[0]) + 1 (operator) + size(p[2]), both recursive calls are
  #   made for smaller "size" (i.e. size(p[0]) < size(p) and size(p[2]) < size(p))
  if p[1] ==  '∧':
    return (T(p[0]), '∧' ,T(p[2]))
  if p[1] == '∨':
    return (T(p[0]), '∨', T(p[2]))

# note: only works for small tuple depth due to error tuple index out of range for depth > 3
print(T(('¬', 'x_2')))
print(T(('¬', ('x_1', '∧', 'x_2' ))))
print(T(('¬', ('x_1', '∧', ('x_2', '∨', 'x_3')))))
# print(T(('¬', ('x_3', '∨', ('x_2', '∧', ('¬', 'x_7')))))) # not working, tuple index out of range
