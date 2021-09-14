markdown_fp = open("step_1.md", "r")

for line in markdown_fp:
	if "<i" in line:
		print("Includes a starting tag: ", line)
	if "i>" in line:
		print("Includes an end tag: ", line)
