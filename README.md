# NYC 311 噪音投诉数据分析

本项目使用 **NYC Open Data 311 Service Requests 数据集**，对纽约市噪音投诉数据进行统计分析，研究不同 borough 之间的投诉分布差异。

---

## 项目目标

研究问题：

**NYC 不同 borough 的噪音投诉数量是否存在显著差异？**

假设：

- H0：投诉在 borough 之间均匀分布
- H1：投诉在 borough 之间不均匀分布

---

## 数据来源

NYC Open Data

https://data.cityofnewyork.us

数据规模：

约 **76万条噪音投诉记录**

---

## 分析内容

### 1 数据清洗

- 筛选 2025 年的噪音投诉数据
- 删除缺失 borough 或坐标的数据
- 保留关键变量

包括：

- created_date
- borough
- descriptor
- coordinates

---

### 2 描述性分析

统计不同 borough 的投诉数量。

结果显示：

- Bronx 和 Brooklyn 投诉最多
- Manhattan 次之
- Staten Island 最少

说明投诉在不同 borough 之间存在明显差异。

---

### 3 探索性分析

分析不同 borough 的噪音类型结构（descriptor）。

发现不同区域的主要噪音来源不同，例如：

- Loud Music / Party
- Banging / Pounding

---

### 4 假设检验

使用 **Chi-square goodness-of-fit test** 检验投诉是否均匀分布。

结果：

- Chi-square ≈ 188000
- p-value < 0.05

因此拒绝原假设。

说明 NYC borough 之间的噪音投诉分布存在显著差异。

---

## 技术栈

- Python
- Pandas
- Matplotlib
- Statistical Analysis

---
