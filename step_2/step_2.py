markdown_fp = open("step_2.md", "r")

# Needed for later
idea_list = []
idea_counter = 0

start_t = "<i"
end_t = "i>"

inside_tag = False
for line in markdown_fp:
    start_tag = start_t in line
    end_tag = end_t in line
    outside_tag = not inside_tag

    if start_tag and outside_tag:
        # Start tag
        tag_start_index = line.index(start_t) + len(end_t)
        line = line[tag_start_index:]
        
        # This is where we'll store the idea
        idea_list.append("")
        
        inside_tag = True

    if end_tag and inside_tag:
        # End tag
        end_tag_index = line.index(end_t)

        line = line[:end_tag_index]

        idea_list[idea_counter] += line
        idea_counter += 1
        inside_tag = False

    if inside_tag:
        # Extract
        idea_list[idea_counter] += line

markdown_fp.close()

output_fp = open("output.md", "w")

output_fp.write("# Collection of ideas\n")

for i, idea in enumerate(idea_list):
		output_fp.write("## Idea %d\n" % (i))
		output_fp.write(idea + "\n")

output_fp.close()
