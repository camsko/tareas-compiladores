class_name TreeLeaf2D extends RigidBody2D

@export var type: String
@export var value: String
@export var color: Color
@export var border_width: int = 5
@export var border_color: Color
@export var border_radius: float

@onready var label = $Label

var logical_position: Vector2

var children: Array[TreeLeaf2D] = []

var show_value: bool = false
var hovering: bool = false

func _ready():
	input_pickable = true
	mouse_entered.connect(on_mouse_entered)
	mouse_exited.connect(on_mouse_exited)
	label.add_theme_color_override("font_color", Color(color * 0.5, 1))
	refresh_label()

func refresh_label():
	var primary: String = value if show_value else type
	var secondary: String = type if show_value else value
	if hovering and secondary != "":
		label.text = secondary.replace("Node", "")
	else:
		label.text = primary.replace("Node", "")

func set_show_value(enabled: bool):
	show_value = enabled
	refresh_label()

func on_mouse_entered():
	hovering = true
	refresh_label()

func on_mouse_exited():
	hovering = false
	refresh_label()

func _process(delta):
	queue_redraw()
	
func _draw():
	var sb := StyleBoxFlat.new()
	sb.bg_color = color
	sb.set_corner_radius_all(border_radius)
	sb.anti_aliasing = true
	sb.draw(get_canvas_item(), Rect2(-60, -30, 120, 60))
