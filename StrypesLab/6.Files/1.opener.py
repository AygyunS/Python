with open('input_file1.txt', 'r') as f_in:
    lines = f_in.readlines()
    sorted_lines = sorted(lines)
    with open('output_file1.txt', 'w') as f_out:
        f_out.writelines(sorted_lines)

# f_in.close()
# f_out.close()

