from math import sin, pi, radians
import scene, ui

    

class SinWave(scene.ShapeNode):
  def __init__(self, p_parent, p_size):
    super().__init__()
    p_parent.add_child(self)
    self.path = ui.Path()
    hz = 180
    sec = p_size[0]
    div = sec / hz
    self.path.move_to(0, p_size[1]/2)
    for i in range(hz):
      y = sin(radians(2*pi*i))*hz
      self.path.line_to(div*i, y+p_size[1]/2)
    self.stroke_color = 'blue'
    self.fill_color = (0,0,0,0)
    
  def debug(self, t_print):
    txt = scene.LabelNode(parent=self)
    txt.text = str(t_print)
    txt.font = ('Source Code Pro', 24)
    txt.color = 0
    return txt
    
    
class BackGround(scene.ShapeNode):
  def __init__(self, p_parent, p_size):
    super().__init__()
    p_parent.add_child(self)
    r = min(p_size[0], p_size[1])
    self.path = ui.Path.rect(0,0,r,r)
    self.fill_color = 'dimgray'
    

class MainNode(scene.Node):
  def __init__(self, p_parent):
    super().__init__()
    p_parent.add_child(self)
    self.p_size = p_parent.size
    self.position = self.p_size/2
    bg = BackGround(self, self.p_size)
    sin_wave = SinWave(bg, bg.size)
    
    
class MyScene(scene.Scene):
  def setup(self):
    main = MainNode(self)
    guide = GuideNode(self)

  def update(self):
    pass


class GuideNode(scene.Node):
  def __init__(self, p_parent):
    super().__init__()
    guide_color = 'red'
    p_x = p_parent.size[0]
    p_y = p_parent.size[1]
    line = scene.ShapeNode(parent=self)
    line.path = ui.Path()
    line.path.move_to(0, p_y/2)
    line.path.line_to(p_x, p_y/2)
    line.path.move_to(p_x/2, 0)
    line.path.line_to(p_x/2, p_y)
    line.stroke_color = guide_color
    x_oval = scene.ShapeNode(parent=self)
    x_o = min(p_x, p_y)
    x_oval.path = ui.Path.oval(0,0,x_o/2,x_o/2)
    x_oval.fill_color = (0,0,0,0)
    x_oval.stroke_color = guide_color
    self.alpha = .25
    self.position = p_parent.size/2
    p_parent.add_child(self)


main = MyScene()
scene.run(main,
          orientation=1,
          frame_interval=2,
          show_fps=True)

