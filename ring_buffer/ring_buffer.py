class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.storage[self.current] == None:
      self.storage[self.current] = item
      if self.current == self.capacity - 1:
        self.current = 0
      else:
        self.current += 1

    else:
      if self.current == self.capacity:
        self.current = 0
      self.storage[self.current] = item
      if self.current == self.capacity - 1:
        self.current = 0
      else:
        self.current += 1

  def get(self):
    return [x for x in self.storage if x != None]