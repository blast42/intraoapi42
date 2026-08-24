import jinja2
import json
from pathlib import Path

def generate_templates_files(template_dir: Path):
	data_path = template_dir / "data.json"
	template_path = template_dir / "template.j2"

	with open(data_path) as f:
		data = json.load(f)

	with open(template_path, "r") as template_file:
		template = template_file.read()

	jinja_env = jinja2.Environment(
		loader=jinja2.BaseLoader(),
		trim_blocks=True,
		lstrip_blocks=True
	)
	rendered_template = jinja_env.from_string(template).render(data=data)

	output_path = project_root / data.get("file_output", "output.yaml").lstrip("/")
	output_path.parent.mkdir(parents=True, exist_ok=True)
	with open(output_path, "w") as f:
		f.write(rendered_template)

	print(f"Generated {output_path} from {template_dir}")


def find_template_dirs(paths_directory: Path):
	"""Find every directory anywhere under paths_directory that contains
	both a template.j2 and a data.json file."""
	template_dirs = []
	for template_j2 in paths_directory.rglob("template.j2"):
		candidate_dir = template_j2.parent
		if (candidate_dir / "data.json").is_file():
			template_dirs.append(candidate_dir)
	return template_dirs


def main() -> None:
	global project_root
	project_root = Path(__file__).resolve().parent.parent
	paths_directory = project_root / "specs/paths"

	if not paths_directory.is_dir():
		raise FileNotFoundError(
			f"Missing directory: {paths_directory}"
		)

	template_dirs = find_template_dirs(paths_directory)

	if not template_dirs:
		print(f"No template.j2 / data.json pairs found under {paths_directory}")
		return

	for template_dir in template_dirs:
		generate_templates_files(template_dir)


if __name__ == "__main__":
	main()