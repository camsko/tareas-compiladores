extends Node

var python_executable: String = "python"

var python_dir: String
var python_main: String
var compiled_dir: String

func _ready():
	var project_dir := ProjectSettings.globalize_path("res://").trim_suffix("/")
	python_dir = project_dir.path_join("proyecto_2")
	python_main = python_dir.path_join("Main.py")
	compiled_dir = python_dir.path_join("compiled")

func compile_file(file_name: String) -> int:
	var output: Array = []
	var exit_code := OS.execute(python_executable, [python_main, file_name], output, true)
	return exit_code

func list_compiled() -> PackedStringArray:
	var names: PackedStringArray = []
	var dir := DirAccess.open(compiled_dir)
	if dir == null:
		return names
	for file_name in dir.get_files():
		if file_name.ends_with(".json"):
			names.push_back(file_name)
	return names

func load_compiled(json_name: String) -> Dictionary:
	var path := compiled_dir.path_join(json_name)
	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		return {}
	var data = JSON.parse_string(file.get_as_text())
	if typeof(data) != TYPE_DICTIONARY:
		return {}
	return data
