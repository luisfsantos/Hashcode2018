def read_input(filepath):
    input_read = {}
    with open(filepath, 'r') as file:
        # first line with the V E R C X
        curr_line = file.readline()
        line_dict = curr_line.split()
        input_read["V"] = int(line_dict[0]) #number of videos
        input_read["E"] = int(line_dict[1]) #number of endpoints
        input_read["R"] = int(line_dict[2]) #number of request descritions
        input_read["C"] = int(line_dict[3]) #number of cache servers
        input_read["X"] = int(line_dict[4]) #capacity in mb of server

    return input_read