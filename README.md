# **PCTR: Photographed Chinese Table Reasoning**

Tables captured in real-world applications are often under suboptimal conditions, such as blur, shadows, tilted angles, and lighting variations. This poses a great challenge to contemporary computer vision techniques. While recent multimodal language models (MLLMs) have demonstrated impressive reasoning capabilities on high-quality table images, their performance still degrades significantly when confronted with noisy, real-world photographs.

To address this challenge, we present **PCTR**, a large-scale dataset specifically designed for **multimodal table reasoning over photographed Chinese tables**. The goal of this dataset is to evaluate and enhance the **robustness and reasoning abilities** of MLLMs under realistic conditions.

---

## **Task Description**

The objective of this competition task is to develop a robust multimodal system that can accurately predict answers by processing both textual questions and their corresponding photographed table images.

The challenge spans multiple **STEM disciplines**, including mathematics, physics, chemistry, biology, among others, requiring models to demonstrate **effective cross-modal reasoning** under real-world conditions.

---

## **Dataset Overview**

The **PCTR dataset** consists of:

* **13,298 training samples**
* **1,000 test samples**

Notes:

* The **training data** contains real-world noise and some annotation errors.
* The **test set** has been meticulously verified by experts to ensure accuracy. While the complete dataset contains 3k samples, we are currently releasing a subset of 1k samples for evaluation purposes.

**Data Format**:

All data is organized in **JSON format** with accompanying image files.

* **Training set**:

  * `train/train.json`
  * `train/images/` (image folder)

* **Test set**:

  * `test/test.json`
  * `test/images/` (image folder)

Each JSON entry contains:

* `id`: unique question ID
* `image`: file path to the photographed table image
* `question`: grounded in image content
* `solution`: step-by-step annotated solution
* `answer`: final answer as a string

**Example JSON entry (training)**:

```json
{
  "id": "4",
  "image": "images/train/1622044524477847261674147110912_0.jpg",
  "question": "初一和初二在90≤x≤100分数段的总人数是多少?",
  "solution": "12+15",
  "answer": "27"
}
```

**Example JSON entry (test)**:

```json
{
  "id": "1",
  "image": "images/test/dfdb38e3500edd96d45b3398ae8b0e65.jpg",
  "question": "如果从周六之后开始之后到下周六利润呈等差数列，那下周三的利润是多少元？"
}
```

---

**Download link**

Baidu Netdisk: https://pan.baidu.com/s/1_3vMrReD9kUYjn4IYQeNhA?pwd=PCTR

## **TSU Prompt Templates**

For each of the seven TSU tasks, we designed a diverse set of specific prompt templates to guide the model and ensure robustness to different instruction phrasings. For each task, we created between 15-22 distinct input prompt templates and multiple output templates to encourage semantic diversity. Below are representative examples of input prompts and expected outputs for each task. The complete collection of prompt templates for all TSU tasks is in [tabrec_instruction.py](tabrec_instruction.py)

* **Table Size Detection (TSD):**
    * *Input:* "How many rows and columns does this table have? Output the final answer in the JSON format `{"row_number": "m", "column_number": "n"}`."
    * *Output:* "This table has 5 rows and 4 columns. Thus, the final answer is `{"row_number": "5", "column_number": "4"}`."

* **Table Cell Extraction (TCE):**
    * *Input:* "What is the content of the cell located in row 2 and column 3 of this table? Represent the cell value in the JSON format `{"row_id":"m", "column_id":"n", "cell_value":"<Corresponding Cell Value>"}`."
    * *Output:* "The target cell values are as follows: `{"row_id":"2", "column_id":"3", "cell_value":"Example Value"}`."

* **Table Cell Locating (TCL):**
    * *Input:* "Given a table image and a cell text 'Target Text'. Find the location of this cell and represent it as JSON `{"value": "<cell value>", "location": (row_id, column_id)}` with both row and column indices starting from 1. Denote the location as 'DOES NOT EXIST' if a cell is not present in the table."
    * *Output:* "The location of the cell is `{"value": "Target Text", "location": (2, 4)}`."

* **Row/Column Extraction (RCE):**
    * *Input:* "What are the contents of cells located in row 3 of this table? Represent the cells in a row with the JSON format `{"row_id":"<row index>", "cell_list":"<a list of cells in this row>"}`."
    * *Output:* "The cells in row 3: `{"row_id": "3", "cell_list": ["A", "B", "C", "D"]}`"

* **Merged Cell Detection (MCD):**
    * *Input:* "Given a table image, please tell me which table cells are merged cells. Return the merged cell regions in the JSON format of `{"top-left":(x, y), "bottom-right":(m, n)}`, where (x, y) and (m, n) represent the (row_id, column_id) coordinates of top-left cell and bottom-right cell, respectively. The row_id and column_id are numbered from 1."
    * *Output:* "`[{"top-left":(1, 1), "bottom-right":(1, 3)}, {"top-left":(2, 4), "bottom-right":(3, 4)}]`"

* **Same Row/Column (SRC):**
    * *Input:* "Check if the cells containing 'Value1' and 'Value2' are in the same row or column in this table."
    * *Output:* "The cells containing 'Value1' and 'Value2' are in the same row or column."

* **Table Recognition (TR):**
    * *Input:* "This picture illustrates a table. Please represent this table with the markdown format in text."
    * *Output:* "`| Header1 | Header2 | Header3 | \n | --- | --- | --- | \n | Cell1,1 | Cell1,2 | Cell1,3 | \n | Cell2,1 | Cell2,2 | Cell2,3 |`"



