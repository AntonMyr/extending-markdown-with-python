markdown_fp = open("step_2.md", "r")

# Needed for later
idea_list = []
idea_counter = 0

inside_tag = False
for line in markdown_fp:
    start_tag = "<i" in line
    end_tag = "i>" in line
    outside_tag = not inside_tag

    if start_tag and outside_tag:
        # Start tag
        tag_start_index = line.index("<i") + len("<i")
        print("tag_start_index: ", tag_start_index)
        print("Line starting from index: ", line[tag_start_index:])
        print("Original line: ", line[0:])

    if end_tag and inside_tag:
        # End tag
        continue

    if inside_tag:
        # Extract
        continue