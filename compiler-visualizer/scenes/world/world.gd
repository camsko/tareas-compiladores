extends Node2D

@export var background_color: Color

@onready var tree_2d = $Tree2D

var compile_dialog: FileDialog
var compiled_menu: PopupMenu
var compiled_files: PackedStringArray = []

func _ready():
	RenderingServer.set_default_clear_color(background_color)
	build_ui()

func build_ui():
	var layer := CanvasLayer.new()
	add_child(layer)

	var buttons := VBoxContainer.new()
	buttons.position = Vector2(20, 20)
	layer.add_child(buttons)

	var compile_button := Button.new()
	compile_button.text = "Compilar archivo"
	compile_button.pressed.connect(open_compile_dialog)
	buttons.add_child(compile_button)

	var visualize_button := Button.new()
	visualize_button.text = "Visualizar compilado"
	visualize_button.pressed.connect(open_compiled_menu)
	buttons.add_child(visualize_button)

	var labels_button := Button.new()
	labels_button.text = "Type / Value"
	labels_button.pressed.connect(tree_2d.toggle_labels)
	buttons.add_child(labels_button)

	compile_dialog = FileDialog.new()
	compile_dialog.file_mode = FileDialog.FILE_MODE_OPEN_FILE
	compile_dialog.access = FileDialog.ACCESS_FILESYSTEM
	compile_dialog.use_native_dialog = true
	compile_dialog.filters = PackedStringArray(["*.py ; Python"])
	compile_dialog.file_selected.connect(on_source_selected)
	layer.add_child(compile_dialog)

	compiled_menu = PopupMenu.new()
	compiled_menu.id_pressed.connect(on_compiled_selected)
	layer.add_child(compiled_menu)

func open_compile_dialog():
	compile_dialog.current_dir = Compiler.python_dir.path_join("tests")
	compile_dialog.popup_centered_ratio(0.6)

func on_source_selected(path: String):
	var file_name := path.get_file().get_basename()
	Compiler.compile_file(file_name)

func open_compiled_menu():
	compiled_files = Compiler.list_compiled()
	compiled_menu.clear()
	for i in range(compiled_files.size()):
		compiled_menu.add_item(compiled_files[i], i)
	compiled_menu.position = Vector2i(20, 80)
	compiled_menu.reset_size()
	compiled_menu.popup()

func on_compiled_selected(id: int):
	var data := Compiler.load_compiled(compiled_files[id])
	if not data.is_empty():
		tree_2d.load_json_nodes(data)
