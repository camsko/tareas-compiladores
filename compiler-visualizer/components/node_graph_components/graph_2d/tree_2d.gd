class_name Tree2D extends Node2D

@export var x_separation: float = 200
@export var y_separation: float = 150

@export var node_type_colors: Array[NodeTypeColor] = []

@export var default_color: Color = Color.LIGHT_GREEN


var tree_leaf_scene = preload("res://components/node_graph_components/tree_leaf_2d/tree_leaf_2d.tscn")

var root: TreeLeaf2D

var all_leafs: Array[TreeLeaf2D] = []

var show_value: bool = false

var leaf_counter: float = 0

var color_by_type: Dictionary = {}

func _ready():
	for entry in node_type_colors:
		color_by_type[entry.type] = entry.color

func get_color_for(type: String) -> Color:
	return color_by_type.get(type, default_color)

func toggle_labels():
	show_value = not show_value
	for leaf in all_leafs:
		leaf.set_show_value(show_value)

func create_node(type: String, value: String, color: Color):
	var leaf: TreeLeaf2D = tree_leaf_scene.instantiate() as TreeLeaf2D
	leaf.type = type
	leaf.value = value
	leaf.show_value = show_value
	leaf.color = color
	leaf.border_color = Color(color * 0.7, 1)
	leaf.border_radius = 12
	leaf.z_index = 1
	all_leafs.push_back(leaf)
	add_child(leaf)
	return leaf

func generate_tree():
	leaf_counter = 0
	assign_positions(root, 0)
	set_rendering_position()
	create_lines(root)

func assign_positions(leaf: TreeLeaf2D, depth: int):
	if leaf.children.is_empty():
		leaf.logical_position = Vector2(leaf_counter, depth)
		leaf_counter += 1
		return
	for c in leaf.children:
		assign_positions(c, depth + 1)
	var first: float = leaf.children[0].logical_position.x
	var last: float = leaf.children[leaf.children.size() - 1].logical_position.x
	leaf.logical_position = Vector2((first + last) / 2.0, depth)

func set_rendering_position():
	for l in all_leafs:
		l.position = Vector2(l.logical_position.x * x_separation, l.logical_position.y * y_separation)


func connect_leafs(n1: TreeLeaf2D, n2: TreeLeaf2D):
	n1.children.push_back(n2)

func create_lines(leaf: TreeLeaf2D, parent: TreeLeaf2D = null):
	if parent:
		var connection_line: Line2D = Line2D.new()
		connection_line.add_point(leaf.global_position)
		connection_line.add_point(parent.global_position)
		connection_line.width = 5
		connection_line.antialiased = true
		var gradient := Gradient.new()
		gradient.set_color(0, leaf.color)
		gradient.set_color(1, parent.color)
		connection_line.gradient = gradient
		add_child(connection_line)
	for c in leaf.children:
		create_lines(c, leaf)

func load_json_nodes(data: Dictionary):
	clear_tree()
	root = build_leaf(data)
	generate_tree()

func build_leaf(data: Dictionary) -> TreeLeaf2D:
	var value_text: String = ""
	if data.get("value") != null:
		value_text = str(data["value"])
	var leaf: TreeLeaf2D = create_node(data.get("type", ""), value_text, get_color_for(data.get("type", "")))
	for child in data.get("children", []):
		connect_leafs(leaf, build_leaf(child))
	return leaf

func clear_tree():
	for child in get_children():
		child.queue_free()
	all_leafs.clear()
	root = null
