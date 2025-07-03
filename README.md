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

**download link**

Upon acceptance of the manuscript, we will release the subsequent datasets.



