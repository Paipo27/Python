def BuscarMin(i, j, k):
    if i < j and i < k:
        return i
    elif j < i and j < k:
        return j
    else:
        return k
    
    
def Swap(a, b):
  return b, a
