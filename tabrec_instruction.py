import random
from bs4 import BeautifulSoup
import json

# TSD
# JSON格式输出指令，few-shot方式让GPT-4生成
TSD_JSON_instruction_list = [
    'Output the final answer in the JSON format {"row_number": "m", "column_number": "n"}. For instance, if the table has 5 rows and 4 columns, the answer would be {"row_number": "5", "column_number": "4"}',
    'The JSON format {"row_number": "m", "column_number": "n"} should be utilized to display the ultimate result.',
    'Output the final answer as JSON in the format {"row_number": "m", "column_number": "n"}.',
    'Show your final answer in the JSON format {"row_number": "m", "column_number": "n"}.',
    'Provide the final answer in the JSON structure, using the format {"row_number": "m", "column_number": "n"}.',
    'The final result should be presented in the JSON format of {"row_number": "m", "column_number": "n"}.',
    'Your final answer should be in the JSON structure, formatted as {"row_number": "m", "column_number": "n"}.',
    'Format your final answer as a JSON, using the structure {"row_number": "m", "column_number": "n"}.',
    'Present the final answer in a JSON format {"row_number": "m", "column_number": "n"} such as {"row_number": "2", "column_number": "3"}.',
    'Return the result as JSON in the format {"row_number": "m", "column_number": "n"}, e.g., {"row_number": "12", "column_number": "7"}.',
]


# 指令模板，few-shot方式让GPT-4生成
def build_table_size_detection_input(row_num, col_num):
    JSON_INSTRUCTION = random.sample(TSD_JSON_instruction_list, 1)[0]
    input_template_list = [
        f"This image shows a table. Tell me the row number and column number of this table. {JSON_INSTRUCTION}",
        f"How many rows and columns does this table have? {JSON_INSTRUCTION}",
        f"This image displays a table. Could you provide me with the row number and column number corresponding to this table? {JSON_INSTRUCTION}",
        f"For the table shown in this image, can you tell me the row and column numbers of this table? {JSON_INSTRUCTION}",
        f"This image depicts a table. How many rows and columns does this table have? {JSON_INSTRUCTION}",
        f"How many rows and columns does the given table have? {JSON_INSTRUCTION}",
        f"Please identify the row and column numbers of the table displayed in this image. {JSON_INSTRUCTION}",
        f"This is a table picture. Can you figure out the row and column numbers for this particular table? {JSON_INSTRUCTION}",
        f"Tell me the row and column numbers of the shown table. {JSON_INSTRUCTION}",
        f"This image presents a table, and I'd like to know its row and column numbers. {JSON_INSTRUCTION}",
        f"Provide me with the row number and column number for the table shown in this image. {JSON_INSTRUCTION}",
        f"I'd like to know the total number of rows and columns in the provided table. {JSON_INSTRUCTION}",
        f"Please determine the total count of rows and columns in the provided table, respectively. {JSON_INSTRUCTION}",
        f"Could you calculate the row number and column number in this table? {JSON_INSTRUCTION}",
        f"What is the count of rows and columns in the given table? {JSON_INSTRUCTION}",
        f"How many rows and columns does this table contain? {JSON_INSTRUCTION}",
        f"Please ascertain the quantity of rows and columns within the provided table. {JSON_INSTRUCTION}",
        f"Tell me how many rows and columns exist in the given table. {JSON_INSTRUCTION}",
        f"For the shown table, how many rows and columns are there? {JSON_INSTRUCTION}",
        f"Could you count the number of rows and columns in this table? {JSON_INSTRUCTION}",
        f"I need to know the count of rows and columns in this specific table. {JSON_INSTRUCTION}",
        f"Regarding the table displayed, can you identify how many rows and columns it has? {JSON_INSTRUCTION}",
    ]
    json_answer = f'{{"row_number": "{row_num}", "column_number": "{col_num}"}}'
    output_template_list = [
        f"This table has {row_num} rows and {col_num} columns. Thus, the final answer is {json_answer}.",
        f"There are {row_num} rows and {col_num} columns in the table. So, the final answer is {json_answer}."
    ]

    final_input = random.sample(input_template_list, 1)[0]
    final_output = random.sample(output_template_list, 1)[0]
    return final_input, final_output


# TCE
TCE_JSON_instruction_list_multi = [
    'Represent each cell value in the JSON format {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}. For instance, {"row_id":"5", "column_id":"4", "cell_value":"missouri 4"}.',
    'Output each cell content as JSON in the format {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}.',
    'Show the cell value in the JSON format {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}.',
    'Provide the value of all target cells in the JSON structure, using the format {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}.',
    'The value of every target cell should be presented in the JSON format of {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}, e.g., {"row_id":"10", "column_id":"3", "cell_value":"District"}.',
    'Format each cell value as a JSON, using the structure {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}.',
    'Return each cell value as JSON in the format {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}.',
]

TCE_JSON_instruction_list_single = [
    'Represent the cell value in the JSON format {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}. For instance, {"row_id":"5", "column_id":"4", "cell_value":"missouri 4"}.',
    'Output the target cell content as JSON in the format {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}.',
    'Show the cell value in the JSON format {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}.',
    'Provide the value of target cell in the JSON structure, using the format {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}.',
    'The target cell value should be presented in the JSON format of {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}, e.g., {"row_id":"10", "column_id":"3", "cell_value":"District"}.',
    'Format the cell value as a JSON, using the structure {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}.',
    'Return the cell value as JSON in the format {"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}.',
]


# 指令模板
def build_cell_lookup_input_and_output(target_cell_location_list, cell_value_list):
    # 分别设计2种单元格位置的表示方式
    repr_type = random.sample([1, 2], 1)[0]

    if repr_type == 1:
        digit_num_to_order_num = {1: '1st', 2: '2nd', 3: '3rd'}
        cell_location_str_list_1 = []
        target_cell_str_list_1 = []
        sep_char = random.sample(['', ','], 1)[0]
        for (row_id, col_id), target_cell in zip(target_cell_location_list, cell_value_list):
            row_id_str = digit_num_to_order_num.get(row_id, f"{row_id}th")
            col_id_str = digit_num_to_order_num.get(col_id, f"{col_id}th")

            location_str = f"the {row_id_str} row and the {col_id_str} column" + sep_char
            cell_location_str_list_1.append(location_str)
            location_str_clean = location_str.strip(',')
            target_cell_str = f'{{"row_id":"{row_id}", "column_id":"{col_id}", "cell_value":"{target_cell}"}}'
            target_cell_str_list_1.append(target_cell_str)
        cell_location_repr = '\n'.join(cell_location_str_list_1)
        target_cell_repr = '\n'.join(target_cell_str_list_1)

    else:
        cell_location_str_list_2 = []
        target_cell_str_list_2 = []
        sep_char = random.sample(['', ','], 1)[0]
        for (row_id, col_id), target_cell in zip(target_cell_location_list, cell_value_list):
            location_str = f"row {row_id} and column {col_id}" + sep_char
            cell_location_str_list_2.append(location_str)
            location_str_clean = location_str.strip(',')
            target_cell_str = f'{{"row_id":"{row_id}", "column_id":"{col_id}", "cell_value":"{target_cell}"}}'
            target_cell_str_list_2.append(target_cell_str)
        cell_location_repr = '\n'.join(cell_location_str_list_2)
        target_cell_repr = '\n'.join(target_cell_str_list_2)

    JSON_INSTRUCTION = random.sample(TCE_JSON_instruction_list_multi, 1)[0]
    input_template_list_with_multi_cells = [
        f"Based on the given table, what are the contents of the cells in the following positions in the table? {JSON_INSTRUCTION}\n{cell_location_repr}",
        f"Return the values of the cells in the following table postions:\n{cell_location_repr}\n\nRequirements: {JSON_INSTRUCTION}",
        f"Analyze the provided table and extract the contents of cells located at the specified positions, identified by row and column indices. {JSON_INSTRUCTION}\nPositions:\n{cell_location_repr}",
        f"Retrieve the values of cells at the given table positions, indicated by row and column indices. {JSON_INSTRUCTION}\nPositions to check:\n{cell_location_repr}",
        f"Examine the given table and identify the contents of cells located at specified locations, denoted by row and column indices. {JSON_INSTRUCTION}\nSpecified positions:\n{cell_location_repr}",
        f"Based on the provided table, please extract the cells' values located at the specified positions, as denoted by row and column indices. {JSON_INSTRUCTION}\nPositions:\n{cell_location_repr}",
        f"Inspect the given table and provide the values of cells found at the specified positions, determined by row and column indices. {JSON_INSTRUCTION}\nPositions:\n{cell_location_repr}",
        f"This image shows a table. Return the contents of cells at the indicated positions in the table. Positions are identified by row and column indices. {JSON_INSTRUCTION}\nSpecified positions:\n{cell_location_repr}",
        f"Considerding the provided table image, extract the cells' values in the following postions:\n{cell_location_repr}\n\n{JSON_INSTRUCTION}",
        f"{cell_location_repr}\nExtract the contents of cells in the above positions, identified by row and column indices. {JSON_INSTRUCTION}",
        f"What are the cells' value in the following positions in the table? {JSON_INSTRUCTION}\n{cell_location_repr}",
        f"Give you some cell positions and a table image, extract the corresponding cell values in these positions:\n{cell_location_repr}\n\n{JSON_INSTRUCTION}",
    ]
    if len(target_cell_location_list) == 1:
        cell_location_repr = cell_location_repr.strip(',')
    JSON_INSTRUCTION_SINGLE = random.sample(TCE_JSON_instruction_list_single, 1)[0]
    input_template_list_with_single_cell = [
        f"What is the content of the cell located in {cell_location_repr} of this table? {JSON_INSTRUCTION_SINGLE}",
        f"For the cell positioned in {cell_location_repr} of this table, provide its content. {JSON_INSTRUCTION_SINGLE}",
        f"Retrieve the content of the cell located in {cell_location_repr} of this table. {JSON_INSTRUCTION_SINGLE}",
        f"According to the shown table image, what is the value of the cell positioned in {cell_location_repr} of the table? {JSON_INSTRUCTION_SINGLE}",
        f"This image illustrates a table. Find the cell at the intersection of {cell_location_repr}, return its content. {JSON_INSTRUCTION_SINGLE}",
        f"There is a cell located in {cell_location_repr} in this table, identify this cell and report its content. {JSON_INSTRUCTION_SINGLE}",
        f"Given this table, what is the content of the cell situated at {cell_location_repr}? {JSON_INSTRUCTION_SINGLE}",
        f"Extract the content of the cell at {cell_location_repr} in this table. {JSON_INSTRUCTION_SINGLE}",
        f"For the cell at {cell_location_repr} in this table, provide its content. {JSON_INSTRUCTION_SINGLE}",
        f"Provide the content of the cell located in {cell_location_repr} of this table. {JSON_INSTRUCTION_SINGLE}",
        f"At {cell_location_repr} of this table, retrieve and report the content of the corresponding cell. {JSON_INSTRUCTION_SINGLE}",
        f"Based on the table image, extract the value of the cell located in the subsequent postion:\n{cell_location_repr}\n\n{JSON_INSTRUCTION_SINGLE}",
        f"{cell_location_repr}\nExtract the content of cell in the above position, identified by row and column indices. {JSON_INSTRUCTION_SINGLE}",
        f"What are the cell's value in the following position in the table?\n{cell_location_repr}\n\n{JSON_INSTRUCTION_SINGLE}",
    ]
    if len(target_cell_location_list) > 1:
        input_template_list = input_template_list_with_multi_cells
        output_template_list = [
            f"The target cell values are as follows:\n{target_cell_repr}",
            f"The extracted cell contents are listed below.\n{target_cell_repr}",
        ]
    else:
        input_template_list = input_template_list_with_single_cell

        output_template_list = [
            f"The target cell value in {cell_location_repr} is {target_cell_str}."
        ]
    final_input = random.sample(input_template_list, 1)[0]
    final_output = random.sample(output_template_list, 1)[0]
    return final_input, final_output


# RCE
RCE_JSON_instruction_list_multi_rows_or_columns = [
    'Represent the cells in a row or a column with the JSON format {"row_id/column_id":"<row or column index>", "cell_list":"<a list of cells in this row/column>"}. For instance, {"row_id":"5", "cell_list": ["13", "england", "2023-1201"]}.',
    'Output the cell values in each row or column as JSON in the format {"row_id/column_id":"<row or column index>", "cell_list":"<a list of cells in this row/column>"}, e.g., {"column_id":"3", "cell_list": ["123.89", "News gathering", "selected tools"]}.',
    'Show the cells in each row or column in the JSON format {"row_id/column_id":"<row or column index>", "cell_list":"<a list of cells in this row/column>"}. For example, {"row_id":"3", "cell_list": ["A", "B", "C"]}.',
    'Provide the cells in each row or column in the JSON structure, using the format {"row_id/column_id":"<row or column index>", "cell_list":"<a list of cells in this row/column>"}.',
    'The cells of every row or column should be presented in the JSON format of {"row_id/column_id":"<row or column index>", "cell_list":"<a list of cells in this row/column>"}, e.g., {"row_id":"3", "cell_list": ["xxx", "yyy", "zzz"]}.',
]

RCE_JSON_instruction_list_row = [
    'Represent the cells in a row with the JSON format {"row_id":"<row index>", "cell_list":"<a list of cells in this row>"}. For instance, {"row_id":"5", "cell_list": ["152", "UN", "one last kiss"]}.',
    'Output the cell values in a row as JSON in the format {"row_id":"<row index>", "cell_list":"<a list of cells in this row>"}, e.g., {"row_id":"3", "cell_list": ["123.89", "News gathering", "selected tools"]}.',
    'Show the cells in a row in the JSON format {"row_id":"<row index>", "cell_list":"<a list of cells in this row>"}. For example, {"row_id":"1", "cell_list": ["A", "B", "C"]}.',
    'Provide the cells in a row in the JSON structure, using the format {"row_id":"<row index>", "cell_list":"<a list of cells in this row>"}.',
    'The cells in a row should be presented in the JSON format of {"row_id":"<row index>", "cell_list":"<a list of cells in this row>"}, e.g., {"row_id":"3", "cell_list": ["xxx", "yyy", "zzz"]}.',
]

RCE_JSON_instruction_list_column = [
    'Represent the cells in a column with the JSON format {"column_id":"<column index>", "cell_list":"<a list of cells in this column>"}. For instance, {"column_id":"5", "cell_list": ["152", "UN", "one last kiss"]}.',
    'Output the cell values in a column as JSON in the format {"column_id":"<column index>", "cell_list":"<a list of cells in this column>"}, e.g., {"column_id":"3", "cell_list": ["123.89", "News gathering", "selected tools"]}.',
    'Show the cells in a column in the JSON format {"column_id":"<column index>", "cell_list":"<a list of cells in this column>"}. For example, {"column_id":"6", "cell_list": ["A", "B", "C"]}.',
    'Provide the cells in a column in the JSON structure, using the format {"column_id":"<column index>", "cell_list":"<a list of cells in this column>"}.',
    'The cells in a column should be presented in the JSON format of {"column_id":"<column index>", "cell_list":"<a list of cells in this column>"}, e.g., {"column_id":"3", "cell_list": ["xxx", "yyy", "zzz"]}.',
]


# 指令模板
def build_row_and_column_extraction_input_and_output(target_row_or_column_list, row_or_column_cell_lists):
    # target_row_or_column_list, [ {'type':'row','index': 2} ]
    # row_or_column_cell_lists, [[cell_1,cell_2,...]]，相应行或列对应的单元格

    repr_type = random.sample([1, 2], 1)[0]
    if repr_type == 1:
        digit_num_to_order_num = {1: '1st', 2: '2nd', 3: '3rd'}

        index_repr_list = []
        target_cells_repr_list = []
        sep_char = random.sample(['', ','], 1)[0]
        for row_or_column_item, target_cell_list in zip(target_row_or_column_list, row_or_column_cell_lists):
            row_or_column_type = row_or_column_item['type']  # row / column
            index_id = row_or_column_item['index']
            index_str = digit_num_to_order_num.get(index_id, f"{index_id}th")
            index_repr = f"the {index_str} {row_or_column_type}" + sep_char  # the 1st row,
            cell_list_string = str(target_cell_list)
            cell_list_repr = f'{{"{row_or_column_type}_id": "{index_id}", "cell_list": {cell_list_string}}}'
            target_cell_list_repr = f"For the {index_str} {row_or_column_type}: {cell_list_repr}"
            index_repr_list.append(index_repr)
            target_cells_repr_list.append(target_cell_list_repr)
        final_index_repr = '\n'.join(index_repr_list)
        final_target_cells_repr = '\n'.join(target_cells_repr_list)

    else:
        index_repr_list = []
        target_cells_repr_list = []
        sep_char = random.sample(['', ','], 1)[0]
        for row_or_column_item, target_cell_list in zip(target_row_or_column_list, row_or_column_cell_lists):
            row_or_column_type = row_or_column_item['type']  # row / column
            index_id = row_or_column_item['index']
            index_repr = f"{row_or_column_type} {index_id}" + sep_char  # row 1/ column 2
            cell_list_string = str(target_cell_list)
            cell_list_repr = f'{{"{row_or_column_type}_id": "{index_id}", "cell_list": {cell_list_string}}}'
            target_cell_list_repr = f"For {row_or_column_type} {index_id}: {cell_list_repr}"
            index_repr_list.append(index_repr)
            target_cells_repr_list.append(target_cell_list_repr)
        final_index_repr = '\n'.join(index_repr_list)
        final_target_cells_repr = '\n'.join(target_cells_repr_list)
    # 分五种情况，同时包含行或列，只提取多行、只提取多列、只提取单行或单列
    target_row_or_column_types = set([item['type'] for item in target_row_or_column_list])
    if target_row_or_column_types == set(['row', 'column']):
        target_type_str = "rows or columns"
        indice_type_str = "row or column"
        JSON_INSTRUCTION = random.sample(RCE_JSON_instruction_list_multi_rows_or_columns, 1)[0]
    elif target_row_or_column_types == set(['row']):
        target_type_str = "rows"
        indice_type_str = "row"
        JSON_INSTRUCTION = random.sample(RCE_JSON_instruction_list_row, 1)[0]
    else:
        target_type_str = "columns"
        indice_type_str = "column"
        JSON_INSTRUCTION = random.sample(RCE_JSON_instruction_list_column, 1)[0]
    input_template_list_with_multi_row_or_columns = [
        f"Based on the given table, what are the contents of the subsequent {target_type_str}?\n{final_index_repr}\n\nRequirements: {JSON_INSTRUCTION}",
        f"Can you extract the data from these specific {target_type_str} in the table provided?\n{final_index_repr}\n\n{JSON_INSTRUCTION}",
        f"Please provide the cell values contained in these {target_type_str} of the table:\n{final_index_repr}\n\n{JSON_INSTRUCTION}",
        f"Return the cells' value in the subsequent table {target_type_str}:\n{final_index_repr}\n\n{JSON_INSTRUCTION}",
        f"Analyze the provided table and extract the contents of specified {target_type_str}, identified by {indice_type_str} indices. {JSON_INSTRUCTION}\nTarget {target_type_str}:\n{final_index_repr}",
        f"Retrieve the values of cells in the given {target_type_str}, indicated by {indice_type_str} indices. {JSON_INSTRUCTION}\n{target_type_str} to retrieve:\n{final_index_repr}",
        f"Examine the given table and extract the contents of in the specific {target_type_str}, denoted by {indice_type_str} indices. {JSON_INSTRUCTION}\nSpecified {target_type_str}:\n{final_index_repr}",
        f"Based on the provided table, please extract the cells' values in the following {target_type_str}. {JSON_INSTRUCTION}\nTarget {indice_type_str} indices:\n{final_index_repr}",
        f"Inspect the given table and provide the contents of specific {target_type_str}. {JSON_INSTRUCTION}\nNeeded {target_type_str}:\n{final_index_repr}",
        f"This image shows a table consists of serveral rows and columns. Please return the contents in the following {target_type_str}:\n{final_index_repr}\n\nRequirements: {JSON_INSTRUCTION}",
        f"Given a table image, your task is to extract the cells' values in the following {target_type_str}:\n{final_index_repr}\n\nTask requirements: {JSON_INSTRUCTION}",
        f"{final_index_repr}\nExtract the contents of cells in the above {target_type_str}, identified by {indice_type_str} indices. {JSON_INSTRUCTION}",
        f"What are the cells' values in these {target_type_str} of the table? {JSON_INSTRUCTION}\n{final_index_repr}",
        f"Could you identify and list the entries from the specified {target_type_str} in this table? {JSON_INSTRUCTION}\n{final_index_repr}",
        f"I need the data from these {target_type_str} of the table, can you provide that?\n{final_index_repr}\n\n{JSON_INSTRUCTION}",
        f"Can you extract and list the values from these specific {target_type_str} in the table?\n{final_index_repr}\n\n{JSON_INSTRUCTION}",
    ]

    if len(target_row_or_column_list) == 1:
        index_repr = index_repr.strip(',')

    input_template_list_with_single_row_or_column = [
        f"What are the contents of cells located in {index_repr} of this table? {JSON_INSTRUCTION}",
        f"For the cells in {index_repr} of this table, provide their contents. {JSON_INSTRUCTION}",
        f"Retrieve the cell contents in {index_repr} of this table. {JSON_INSTRUCTION}",
        f"According to the table image, show the cell contents in {index_repr}. {JSON_INSTRUCTION}",
        f"This image illustrates a table. Find the cells in {index_repr}, return their values. {JSON_INSTRUCTION}",
        f"Find {index_repr} in this table and extract its cells' values. {JSON_INSTRUCTION}",
        f"Given this table, what are the contents in {index_repr}? {JSON_INSTRUCTION}",
        f"Extract the cells' contents in {index_repr} in this table. {JSON_INSTRUCTION}",
        f"Based on the table image, your task is to extract the cells' values in {index_repr}. {JSON_INSTRUCTION}",
        f"Provide the contents of the cells located in the {index_repr} of this table. {JSON_INSTRUCTION}",
        f"Based on the table image, extract the cell contents located in {index_repr}. {JSON_INSTRUCTION}",
        f"{index_repr}\nExtract the contents of cells in the above {indice_type_str}. {JSON_INSTRUCTION}",
        f"What are the cells' values in the following position in the table?\n{index_repr}\n\n{JSON_INSTRUCTION}",
        f"Give you a {indice_type_str} index and a table image, extract the corresponding cell values of this {indice_type_str}:\n{index_repr}\n\n{JSON_INSTRUCTION}",
        f"Please list the cell values found in {index_repr} of the table. {JSON_INSTRUCTION}",
        f"I need to know the contents of the cells in {index_repr} of the table. {JSON_INSTRUCTION}",
        f"Please extract and show the values of the cells in {index_repr} of this table. {JSON_INSTRUCTION}",
    ]
    if len(target_row_or_column_list) > 1:
        input_template_list = input_template_list_with_multi_row_or_columns
        output_template_list = [
            f"The cell values of target {target_type_str} are as follows:\n{final_target_cells_repr}",
            f"The extracted {indice_type_str} contents are listed below.\n{final_target_cells_repr}",
        ]
    else:
        input_template_list = input_template_list_with_single_row_or_column
        output_template_list = [
            f"The cells in {index_repr}: {cell_list_repr}",
            f"The target cell values of {index_repr}: {cell_list_repr}"
        ]
    final_input = random.sample(input_template_list, 1)[0]
    final_output = random.sample(output_template_list, 1)[0]
    return final_input, final_output


# TCL
# 指令模板
def build_cell_retrieval_input_and_output(target_cell_str_to_cell_location_str):
    target_cell_str_list = [key for key in target_cell_str_to_cell_location_str]

    # 单元格位置的表示
    # 目标单元格文本的表示
    target_cell_repr_type = random.sample([1, 2, 3], 1)[0]
    formated_cell_str_list = []
    cell_location_str_list = []
    sep_char = random.sample([',', '', ';'], 1)[0]
    for num, cell_str in enumerate(target_cell_str_list):
        if target_cell_repr_type == 1:
            formated_c = f"({num + 1}) '{cell_str}'" + sep_char  # (1) 单元格文本
            location_str = target_cell_str_to_cell_location_str[cell_str]  # (1,2)
            if location_str == 'DOES NOT EXIST':
                location_str = "'DOES NOT EXIST'"
            json_location_str = f"{{'value': '{cell_str}', 'location': {location_str}}}"
            formated_c_location = f"({num + 1}) {json_location_str}"  # (1) (1,2)
            formated_cell_str_list.append(formated_c)
            cell_location_str_list.append(formated_c_location)
        elif target_cell_repr_type == 2:
            formated_c = f"{num + 1}. '{cell_str}'" + sep_char  # 1. '单元格文本'
            location_str = target_cell_str_to_cell_location_str[cell_str]
            if location_str == 'DOES NOT EXIST':
                location_str = "'DOES NOT EXIST'"
            json_location_str = f"{{'value': '{cell_str}', 'location': {location_str}}}"
            formated_c_location = f"{num + 1}. {json_location_str}"  # 1. (1,2)
            formated_cell_str_list.append(formated_c)
            cell_location_str_list.append(formated_c_location)
        else:
            formated_c = f"CELL VALUE {num + 1}: '{cell_str}'" + sep_char  # CELL VALUE 1: '单元格文本'
            location_str = target_cell_str_to_cell_location_str[cell_str]
            if location_str == 'DOES NOT EXIST':
                location_str = "'DOES NOT EXIST'"
            json_location_str = f"{{'value': '{cell_str}', 'location': {location_str}}}"
            formated_c_location = f"CELL LOCATION {num + 1}: {json_location_str}"  # CELL LOCATION 1: (1,2)
            formated_cell_str_list.append(formated_c)
            cell_location_str_list.append(formated_c_location)
    cell_text_repr = '\n'.join(formated_cell_str_list)
    cell_location_repr = '\n'.join(cell_location_str_list)
    cell_location_format, index_str = random.sample(
        [("(row_id, column_id)", "id"), ("(Row_ID, Column_ID)", "IDs"), ("(row index, column index)", "indices"),
         ("(row number, column number)", "number")], 1)[0]
    ss_1 = "Some cell values may not be contained in this table. If so, represent their locations as 'DOES NOT EXIST'."
    ss_2 = "If a cell does not exist in the table, denote its location as 'DOES NOT EXIST'."
    ss_3 = "For the case where a cell is not contained in the table, its location should be denoted as 'DOES NOT EXIST'."
    ss_4 = "Denote the location as 'DOES NOT EXIST' if a cell does not exist in the table."
    ss_5 = "Should a cell be absent in the table, denote its location as 'DOES NOT EXIST'."
    ss_6 = "Use 'DOES NOT EXIST' as the location for a non-existing cell in the table."
    ss_7 = "Represent the location as 'DOES NOT EXIST' if a cell is not present in the table."
    not_existed_str = random.sample([ss_1, ss_2, ss_3, ss_4, ss_5, ss_6, ss_7], 1)[0]
    JSON_FORMAT = f"{{'value': '<cell value>', 'location': {cell_location_format}}}"
    input_template_list_with_multi_cells = [
        f"Based on the given table, what are the locations of the following cells?\n{cell_text_repr}\nReturn the cell location in the JSON format {JSON_FORMAT} where row {index_str} and column {index_str} all start from 1. {not_existed_str}",
        f"Given the table image, tell me the locations of the subsequent table cells. Represent the cell location with JSON {JSON_FORMAT} where both Row {index_str} and Column {index_str} begin from 1.\n{cell_text_repr}\n{not_existed_str}",
        f"Analyze the provided table and identify the locations of these cells:\n{cell_text_repr}\nProvide the cell locations using the JSON format {JSON_FORMAT}, where row and column {index_str} start from 1. {not_existed_str}",
        f"For the specified cells listed below, determine their locations in the given table. Express the cell locations as JSON {JSON_FORMAT}, starting from 1 for both row and column {index_str}. {not_existed_str}\n{cell_text_repr}",
        f"Examine the given table and locate the cells that contain the following values:\n{cell_text_repr}\nReturn the cell locations using the JSON format {JSON_FORMAT}, where both row and column {index_str} commence from 1. {not_existed_str}",
        f"Based on the provided table, find the positions of cells with the subsequent values. Return their locations using the JSON format {JSON_FORMAT}, starting from 1 for both row and column {index_str}. {not_existed_str}\nThe target cell values:\n{cell_text_repr}",
        f"Inspect the provided table and determine the locations of cells that have the following values.\nExpress the cell positions as JSON {JSON_FORMAT}, with row and column {index_str} beginning from 1. {not_existed_str}\n{cell_text_repr}",
        f"Given a table, you can represent a cell's position using the JSON {JSON_FORMAT}, where row and column {index_str} start from 1. Referring to the shown table picture, determine the locations of the specified cells using the mentioned format.\nTarget cell values:\n{cell_text_repr}\n{not_existed_str}",
        f"In the context of a table, we can utilize the json format {JSON_FORMAT} to express a cell's position, where both row and column {index_str} commence from 1. Examining the provided table image, identify the locations of the following cells using this format.\nValues to locate:\n{cell_text_repr}\n{not_existed_str}",
        f"A table may have multiple cells. We can utilize the json format {JSON_FORMAT} to store a cell's positions in a table, where both row and column {index_str} start from 1. I am providing you a table image. Please tell me the positions of the cells mentioned below using the above format. {not_existed_str}\nValues to locate:\n{cell_text_repr}",
        f"Your task:\nLook at the table image, determine the locations of the following cells. A cell's location MUST be represented as a json structure {JSON_FORMAT}, with row and column {index_str} beginning from 1. {not_existed_str}\nTarget cells:\n{cell_text_repr}",
        f"To complete your task, analyze the table image and identify the positions of the specified cells. Ensure that you represent a cell's location using the JSON format {JSON_FORMAT}, with both row and column {index_str} starting from 1. {not_existed_str}\nTarget cells:\n{cell_text_repr}",
        f"Your is as follows:\nExamine the table image and determine the locations of the mentioned cells. You need to express a cell's position with the JSON {JSON_FORMAT}, with row and column {index_str} both commencing from 1. {not_existed_str}\nCells to locate:\n{cell_text_repr}",
        f"Look at the provided table image. Your goal is to find the locations of the specified cells. Remember to represent a cell's location using the JSON {JSON_FORMAT}. Both row and column {index_str} begin from 1. {not_existed_str}\nTarget cells:\n{cell_text_repr}",
        f"To fulfill your task, review the table image and pinpoint the positions of the specified cells. Make sure to represent a cell's location using the JSON format {JSON_FORMAT} which begin from '(1, 1)'.\nTarget cells:\n{cell_text_repr}\n\n{not_existed_str}",
        f"In this task, you are provided with a table image and several target cells. You are required to determine the positions of these cells, which can be represented in the json {JSON_FORMAT}, with both row {index_str} and column {index_str} start from 1. {not_existed_str}\nCell values are shown below:\n{cell_text_repr}",
        f"Given a task involving a table image, your goal is to pinpoint the positions of specified cells. Format each cell's location as JSON in the format {JSON_FORMAT}, with both row and column {index_str} starting from 1.\nRefer to the values below:\n{cell_text_repr}\n\n{not_existed_str} ",
    ]
    if len(target_cell_str_list) == 1:
        cell_text_repr = cell_str
    input_template_list_with_single_cell = [
        f"Given a table image and a cell text '{cell_text_repr}'. Find the location of this cell and represent it as JSON {JSON_FORMAT} with both row and column {index_str} starting from 1. {not_existed_str}",
        f"With the provided table image and the cell text '{cell_text_repr}', please locate this cell with the JSON format {JSON_FORMAT}, remembering that both row and column {index_str} begin at 1. {not_existed_str}",
        f"Using this image of a table, identify the cell containing the text '{cell_text_repr}' and provide its location as JSON in the format {JSON_FORMAT}. Note that row and column {index_str} are numbered from 1. {not_existed_str}",
        f"In the table shown in the image, locate the cell with the value '{cell_text_repr}' and return its location as JSON in the format {JSON_FORMAT}. Both row and column {index_str} start from 1. {not_existed_str}",
        f"Examine the table in this image to find the cell whose value is '{cell_text_repr}', and then provide its location as a json structure {JSON_FORMAT}. The {index_str} for both rows and columns starts from 1. {not_existed_str}",
        f"Please find the cell that has the text '{cell_text_repr}' in the table image. Return its location with the JSON format {JSON_FORMAT}, noting that the {index_str} for rows and columns starts from 1. {not_existed_str}",
        f"I want to konw whether there is a cell in the provided table whose value is '{cell_text_repr}'. If so, return its location with the JSON format {JSON_FORMAT}, where the {index_str} for rows and columns starts from 1. {not_existed_str}",
        f"Given a cell value '{cell_text_repr}' and a table picture, please locate the cell with this value and return its location as a JSON {JSON_FORMAT}. The row {index_str} and column {index_str} both begin from 1. {not_existed_str}",
        f"Based on the given table image and the specific text '{cell_text_repr}', please identify the cell's position and provide its location as JSON in the format {JSON_FORMAT}, keeping in mind that row and column {index_str} are numbered from 1.",
        f"Find the cell in this table that contains the text '{cell_text_repr}' and report its location using the JSON format {JSON_FORMAT}. Note that the numbering for both row and column {index_str} begins at 1. {not_existed_str}",
        f"In the provided image of a table, search for the cell with the text '{cell_text_repr}' and specify its location using the JSON {JSON_FORMAT}, with the understanding that row and column {index_str} both start from 1. {not_existed_str}",
        f"In this task, you are provided with a table image and a cell text '{cell_text_repr}'. Can you check whether the table contains such a cell and return its coordinate in the JSON format of {JSON_FORMAT}?  {not_existed_str} The row {index_str} and column {index_str} begin from 1.",
        f"With the given table picture and the specific cell text '{cell_text_repr}', please determine if such a cell exists in the table and provide its location using the json format {JSON_FORMAT}. {not_existed_str} Remember, both row and column {index_str} start from 1.",
        f"Target cell value: {cell_text_repr}\nWatch the provided table image to check if a cell with the above cell value is contained in the table. If true, return the cell's location as JSON in the format {JSON_FORMAT} where both row and column {index_str} start from (1, 1). {not_existed_str}",
        f"Can you locate a cell with the text '{cell_text_repr}' in this table image and return its coordinates in the JSON format {JSON_FORMAT}? {not_existed_str} Keep in mind that both the row and column {index_str} start numbering from 1.",
        f"Search for this cell content: '{cell_text_repr}'\nIn the given table image, please determine if there's a cell matching this content. If so, report its location with the json format {JSON_FORMAT}, with row and column {index_str} beginning from (1, 1). {not_existed_str}",
        f"The target cell text to locate: '{cell_text_repr}'\nCheck the table in this image to see if a cell with the stated content is included. If yes, provide its location as JSON {JSON_FORMAT}, beginning from the coordinate (1, 1). {not_existed_str}",
        f"With this table image, look for a cell containing '{cell_text_repr}'. If it exists, report its location in the json format {JSON_FORMAT}. {not_existed_str} Remember, row and column numbers start at 1.",
    ]
    if len(target_cell_str_list) > 1:
        input_template_list = input_template_list_with_multi_cells
        output_template_list = [
            f"The target cell locations are as follows:\n{cell_location_repr}",
            f"The coordinates of target cells are listed below.\n{cell_location_repr}",
        ]
    else:
        input_template_list = input_template_list_with_single_cell
        output_template_list = [
            f"The location of the cell is {json_location_str}.",
            f"The target cell position is {json_location_str}."
        ]
    final_input = random.sample(input_template_list, 1)[0]
    final_output = random.sample(output_template_list, 1)[0]
    return final_input, final_output


# MCD
def extract_merged_region_of_custom_table(item):
    """
    根据给定的表格数据提取合并单元格信息，生成所需的格式。
    """
    if 'shapes' not in item or not item['shapes']:
        return "This table does not contain any merged cells.", []

    merged_regions = []

    # 遍历每一个形状，确定是否为合并单元格
    for shape in item['shapes']:
        if len(shape['label'].split('-')) >= 5:

            label_parts = shape['label'].split('-')
            try:
                row = int(label_parts[0])
                col = int(label_parts[1])
                rowspan = int(label_parts[2])
                colspan = int(label_parts[3])
                if rowspan > 1 or colspan > 1:
                    # 如果存在 rowspan 或 colspan，表示这是一个合并单元格
                    top_left = (row, col)
                    bottom_right = (row + rowspan - 1, col + colspan - 1)
                    merged_regions.append({
                        'top-left': top_left,
                        'bottom-right': bottom_right
                    })
            except ValueError as ve:
                print(f"Error parsing row/col/span in {shape['label']}: {ve}")
                continue

    if not merged_regions:
        return "This table does not contain any merged cells.", []

    # 格式化输出
    final_output = json.dumps(merged_regions)
    final_region_cell_repr = merged_regions

    return final_output, final_region_cell_repr



def build_merged_region_detection_input_and_output(table_item):
    coordinate_list = [('X', 'Y', 'Z', 'W'), ('x', 'y', 'z', 'w'), ('x', 'y', 'm', 'n'), ('X1', 'Y1', 'X2', 'Y2'),
                       ('A', 'B', 'C', 'D'), ('R1', 'C1', 'R2', 'C2')]
    x, y, m, n = random.sample(coordinate_list, 1)[0]
    regions = random.sample(['regions', 'areas'], 1)[0]
    input_template_list = [
        f"Given a table image, please tell me which table cells are merged cells. Return the merged cell {regions} in the JSON format of {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, where ({x}, {y}) and ({m}, {n}) represent the (row_id, column_id) coordinates of top-left cell and bottom-right cell, respectively. The row_id and column_id are numberd from 1.",
        f"This image shows a table. Determine whether this table contains merged cells and output merged cell {regions} with the JSON format of {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, where {x}, {y}, {m} and {n} represent the indices of the first row, the first column, the last row, and the last column in the merged region. Row and column indices are numberd from 1.",
        f"In this table image, can you identify any merged cells and provide their locations in the JSON format of {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, where ({x}, {y}) is the top-left and ({m}, {n}) is the bottom-right cell coordinates? Cell coordinates start from (1,1).",
        f"From the provided table image, locate any cells that are merged and list their {regions} as {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, with ({x}, {y}) indicating the (row_id, column_id) of top-left cell and ({m}, {n}) the bottom-right cell. Both the row_id and column_id start from 1.",
        f"Examine the table in this image and extract any merged cell {regions}. Please format the merged cell {regions} as JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, with ({x}, {y}) indicating the (row_id, column_id) of the top-left cell and ({m}, {n}) the bottom-right cell in the merged regions. Remember that the {x}, {y}, {m}, {n} all start from 1.",
        f"Could you analyze the table shown in the image and inform me about all the merged cell {regions}? Use the JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}} to represent each merged area, with ({x}, {y}) as the (first row, first column) and ({m}, {n}) as the (last row, last column). Note that the {x}, {y}, {m}, {n} all start from 1.",
        f"In this table image, are there any merged cells? If so, describe their locations using the JSON format {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, where ({x}, {y}) and ({m}, {n}) indicate the (row_id, column_id) of top-left and bottom-right cells in the merged regions, respectively. Note that the {x}, {y}, {m}, {n} all start from 1.",
        f"Look at the table in the image and show any merged cells, specifying their locations with the JSON format of {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, where {x}, {y}, {m} and {n} are indices (starting from 1) of the first row, the first column, the last row and the last column, respectively.",
        f"The picture contains a table. You task is to identify any merged cells in this table, and output the scope of each merged cell using the JSON format of {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}. The row id and column id should start from 1.",
        f"Return the merged cell {regions} in the provided table image. Your answer should be in the JSON format of {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, where ({x}, {y}) and ({m}, {n}) represent the (row_id, column_id) coordinates of top-left cell and bottom-right cell, respectively. Note that row_id and column_id start from 1 instead of 0.",
        f"Based on this table picture, can you identify any merged cells and give their coordinates in the JSON format {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, where ({x}, {y}) and ({m}, {n}) correspond to the top-left and bottom-right (row_id, column_id) of the merged area? The row_id and column_id should start from 1 rather than 0.",
        f"I need you to conduct the following task:\nGiven this table image, find all merged table cells and return merged regions with the JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}},  where ({x}, {y}) and ({m}, {n}) indicate the (row_id, column_id) of top-left and bottom-right cells in the merged regions, respectively. You should remember that row id and column id start from 1.",
        f"Please perform the following task:\nExamine the provided table image to identify all cells that are merged. Report back the merged cell areas using the JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, where '({x}, {y})' represents the top-left and '({m}, {n})' the bottom-right cell's (row_id, column_id) in each merged region. Note that both row and column IDs begin at 1.",
        f"Your task is as follows:\nIn this table image, locate all merged cells and detail their regions using the JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}. Here, '({x}, {y})' and '({m}, {n})' denote the coordinates (row_id, column_id) of the top-left and bottom-right cells of the merged regions, respectively. Keep in mind that row and column IDs start from 1.",
        f"Here's what I need you to do:\nIn the image of this table, identify all the merged cells. Provide the coordinates of these merged regions in the JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, with '({x}, {y})' and '({m}, {n})' indicating the (row_id, column_id) of the top-left and bottom-right cells, respectively. Remember, row and column numbering starts at 1.",
        f"A table may have multiple merged cells and we can represent a merged cell region by a JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}. Here, '({x}, {y})' and '({m}, {n})' denote the coordinates (row_id, column_id) of the top-left and bottom-right cells of the merged regions, respectively. Now, based on the shown table image, please find all merged cells in this table and return their representations in the above format. Keep in mind that row and column IDs start from 1.",
        f"The task is as follows:\nAnalyze the table in this image to find every merged cell. Return the regions of these merged cells in the JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, where '({x}, {y})' and '({m}, {n})' show the (row_id, column_id) of the top-left and bottom-right cells in these regions, respectively. The row and column IDs start from 1.",
        f"Different merged cells often exist in a table and they can be represented by the JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}. In this JSON item, '({x}, {y})' and '({m}, {n})' are the (row_id, column_id) coordinates for the top-left and bottom-right cells in the merged region, respectively. Please examine the provided table image, identify all merged cells, and return their details using the above-mentioned format. Remember, the numbering for both rows and columns starts at 1.",
        f"A merged cell in a table could be represented by the JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, where '({x}, {y})' and '({m}, {n})' signify the (row_id, column_id) of the top-left and bottom-right cells in the merged area. Using the shown table image, locate all merged cells and provide their coordinates in this format. Bear in mind that row and column IDs begin from 1.",
        f"A merged cell in a table can be described using the JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}. Here, '({x}, {y})' represents the top-left and '({m}, {n})' the bottom-right cells' (row_id, column_id) of the merged region. Using the displayed table image, identify all such merged cells in this table and report their locations in the given format. Note that the numbering of both row and column IDs starts at 1.",
        f"In tables, merged cells are often found and we can denote them as JSON {{'top-left':({x}, {y}), 'bottom-right':({m}, {n})}}, with '({x}, {y})' and '({m}, {n})' indicating the (row_id, column_id) of the top-left and bottom-right cells of the merged region. Please scan the table image provided, find all occurrences of merged cells, and return their coordinates in the stated format. It's important to remember that row and column IDs begin from 1.",
    ]

    final_input = random.sample(input_template_list, 1)[0]
    final_output, final_region_cell_repr = extract_merged_region_of_custom_table(table_item)

    return final_input, final_output, final_region_cell_repr

# same_row_or_column_task
def build_same_row_or_column_input_and_output(cell_value_1, cell_value_2, result):
    input_template_list = [
        f"Check if the cells containing '{cell_value_1}' and '{cell_value_2}' are in the same row or column in this table.",
        f"In the given table, determine if the cell with content '{cell_value_1}' and the cell with content '{cell_value_2}' are located in the same row or column.",
        f"Are the cells with values '{cell_value_1}' and '{cell_value_2}' positioned in the same row or column in this table?",
        f"Determine if the cells containing the text '{cell_value_1}' and '{cell_value_2}' are in the same row or column within the given table.",
        f"Given a table, check whether the cells containing '{cell_value_1}' and '{cell_value_2}' are located in the same row or column."
    ]

    output_template_list = [
        f"The cells containing '{cell_value_1}' and '{cell_value_2}' {'are' if result else 'are not'} in the same row or column.",
        f"The answer is {'Yes' if result else 'No'}, the cells with values '{cell_value_1}' and '{cell_value_2}' {'are' if result else 'are not'} in the same row or column."
    ]

    final_input = random.sample(input_template_list, 1)[0]
    final_output = random.sample(output_template_list, 1)[0]

    return final_input, final_output
