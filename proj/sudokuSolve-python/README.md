# 数独求解器

## 技术说明

### pycosat

 `pycosat` 是一个用于解决布尔可满足性问题（SAT问题）的Python库。它实现了DPLL（Davis–Putnam–Logemann–Loveland）算法，用于在给定的布尔逻辑公式中找到满足条件的变量赋值。

 官网:https://pypi.org/project/pycosat/

### 数独问题的逻辑建模

我们用$S_{xyz}$ 表示命题**在(x,y)上填上z**(注意x,y从0开始)，因此问题可以表述为如下逻辑表达式

- 每个格子只能填1-9中一个

  <span style="font-size: larger;">$\land$</span>$_{x=0}^{8}$<span style="font-size: larger;">$\land$</span>$_{y=0}^{8}$(<span style="font-size: larger;">$\lor$</span>$_{z=1}^{9}S_{xyz}\land$<span style="font-size: larger;">$\land$</span>$_{z=1}^{8}$<span style="font-size: larger;">$\land$</span>$_{i=z+1}^{9}(\neg S_{xyz}\lor \neg S_{xyi})$)

- 每一列都存在1-9

  <span style="font-size: larger;">$\land$</span>$_{y=0}^{8}$<span style="font-size: larger;">$\land$</span>$_{z=1}^{9}$<span style="font-size: larger;">$\lor$</span>$_{x=0}^{8}S_{xyz}$

- 每一行都存在1-9

   <span style="font-size: larger;">$\land$</span>$_{x=0}^{8}$<span style="font-size: larger;">$\land$</span>$_{z=1}^{9}$<span style="font-size: larger;">$\lor$</span>$_{y=0}^{8}S_{xyz}$
  
- 每一个就宫格都有1-9

	<span style="font-size: larger;">$\land$</span>$_{i=0}^{2}$<span style="font-size: larger;">$\land$</span>$_{j=1}^{2}$<span style="font-size: larger;">$\land$</span>$_{z=1}^{9}$<span style="font-size: larger;">$\lor$</span>$_{x=0}^{2}$<span style="font-size: larger;">$\lor$</span>$_{y=0}^{2}S_{(3i+x)(3j+y)z}$
