class tag_checker:
    def __init__(self):
        self.tags = {}
    
    def add_tag(self, name, start_t, end_t):
        self.tags[name] = {
            "start_t": start_t,
            "end_t": end_t,
            "tag_counter": 0,
            "tag_list": [],
            "inside_tag": False,
        }

    def run(self, line):
        for tag_name, tag in self.tags.items():
            start_t = tag["start_t"]
            end_t = tag["end_t"]
            tag_counter = tag["tag_counter"]
            tag_list = tag["tag_list"]
            inside_tag = tag["inside_tag"]

            start_tag = start_t in line
            end_tag = end_t in line
            outside_tag = not inside_tag

            if start_tag and outside_tag:
                #start_line = line
                tag_start_index = line.index(start_t) + len(start_t)
                line = line[tag_start_index:]
                #splitted = start_line.split(q_start, 1)
                #questions.append(splitted[1]) if len(splitted[-1]) > 1 else questions.append(splitted[0])
                #line = questions[q_counter]
                tag_list.append("")
                inside_tag = True

            if end_tag and inside_tag:
                end_tag_index = line.index(end_t)
                # this means that the line only contains the q_end tag
                if end_tag_index == -1:
                    line = ""
                else:
                    line = line[:end_tag_index]

                tag_list[tag_counter] += line
                tag_counter += 1
                inside_tag = False

                tag["tag_counter"] = tag_counter
                tag["tag_list"] = tag_list
                tag["inside_tag"] = inside_tag

                continue
            
            if inside_tag:
                tag_list[tag_counter] += line

            tag["tag_counter"] = tag_counter
            tag["tag_list"] = tag_list
            tag["inside_tag"] = inside_tag
        
    def get_tag_list(self, tag_name):
        return self.tags[tag_name]["tag_list"]
            