class_name CameraController extends Camera2D

@export var zoom_step: float = 0.1
@export var min_zoom: float = 0.2
@export var max_zoom: float = 5.0

@export var pan_speed: float = 800.0
@export var keyboard_zoom_step: float = 0.03

var dragging: bool = false

func _process(delta):
	var direction: Vector2 = Vector2.ZERO
	if Input.is_key_pressed(KEY_A):
		direction.x -= 1
	if Input.is_key_pressed(KEY_D):
		direction.x += 1
	if Input.is_key_pressed(KEY_W):
		direction.y -= 1
	if Input.is_key_pressed(KEY_S):
		direction.y += 1
	position += direction * pan_speed * delta / zoom
	if Input.is_key_pressed(KEY_E):
		set_zoom_level(zoom.x + keyboard_zoom_step)
	if Input.is_key_pressed(KEY_Q):
		set_zoom_level(zoom.x - keyboard_zoom_step)

func _unhandled_input(event):
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_MIDDLE:
			dragging = event.pressed
		elif event.button_index == MOUSE_BUTTON_WHEEL_UP:
			set_zoom_level(zoom.x + zoom_step)
		elif event.button_index == MOUSE_BUTTON_WHEEL_DOWN:
			set_zoom_level(zoom.x - zoom_step)
	elif event is InputEventMouseMotion and dragging:
		position -= event.relative / zoom

func set_zoom_level(value: float):
	var level: float = clamp(value, min_zoom, max_zoom)
	zoom = Vector2(level, level)
