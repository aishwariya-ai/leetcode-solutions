<div align="center">

# 3498. Reverse Degree of a String

![Difficulty](https://img.shields.io/badge/DIFFICULTY-Easy-00b8a3?style=for-the-badge&labelColor=1a1a2e)  ![Language](https://img.shields.io/badge/LANGUAGE-Python-6c5ce7?style=for-the-badge&labelColor=1a1a2e)  ![Solutions](https://img.shields.io/badge/SOLUTIONS-1-6c5ce7?style=for-the-badge&labelColor=1a1a2e)  ![Date](https://img.shields.io/badge/DATE-2026--09--20-605d5d?style=for-the-badge&labelColor=1a1a2e)

[![View on LeetCode](https://img.shields.io/badge/View%20on-LeetCode-ffa116?style=flat-square&logo=leetcode&logoColor=ffa116)](https://leetcode.com/problems/reverse-degree-of-a-string/)

</div>

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="panel-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="panel-light.svg">
  <img alt="Topics: String, Simulation — best runtime 12 ms (Beats 40%), best memory 12.4 MB (Beats 56%)" src="panel-dark.svg">
</picture>

</div>

> **New personal best** — Runtime improved on this submission.

### HOW IT WENT

| | |
|:--|:--|
| **Attempts** | first try |
| **Time to solve** | 3 min |
| **Verdicts** | ✅ Accepted |

---

### NOTES

_No notes yet._

---

### SOLUTIONS (1)

| # | File | Language | Date |
|:-:|------|:--------:|:----:|
| 1 | [sol1.py](./sol1.py) | `Python` | 2026-09-20 ← **latest** |

---

### PROBLEM DESCRIPTION

Given a string `s`, calculate its **reverse degree**.

The **reverse degree** is calculated as follows:

	- For each character, multiply its position in the *reversed* alphabet (`'a'` = 26, `'b'` = 25, ..., `'z'` = 1) with its position in the string **(1-indexed)**.

	- Sum these products for all characters in the string.

Return the **reverse degree** of `s`.

 

**Example 1:**

**Input:** s = "abc"

**Output:** 148

**Explanation:**

	
		
			Letter
			Index in Reversed Alphabet
			Index in String
			Product
		
		
			`'a'`
			26
			1
			26
		
		
			`'b'`
			25
			2
			50
		
		
			`'c'`
			24
			3
			72
		
	

The reversed degree is `26 + 50 + 72 = 148`.

**Example 2:**

**Input:** s = "zaza"

**Output:** 160

**Explanation:**

	
		
			Letter
			Index in Reversed Alphabet
			Index in String
			Product
		
		
			`'z'`
			1
			1
			1
		
		
			`'a'`
			26
			2
			52
		
		
			`'z'`
			1
			3
			3
		
		
			`'a'`
			26
			4
			104
		
	

The reverse degree is `1 + 52 + 3 + 104 = 160`.

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` contains only lowercase English letters.

---

<div align="center">

<sub>Auto-synced by <strong>LeetSync</strong> · Built by <a href="https://deveshsamant.in/">Devesh Samant</a></sub>

</div>
