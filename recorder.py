

class Recorder:
  def __init__(self):
    self.offsets = []

  def record(offset, cur_diag, cur_step):
    self.offsets.append(offset)
    print offset
