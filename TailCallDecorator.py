name_to_func = {}
def tailcall(f):
  name_to_func[f.__name__] = f
  def g(*args):
    func = f
    while True:
      result = func(*args)
      if type(result) is tuple:
        (first, *new_args) = result
        if type(first) is str and len(first) > 1:
          if first[0] == "@":
            func = name_to_func[first[1:]]
            args = new_args
          else:
            return result
        else:
          return result
      else:
        return result
  return g
