# Python strings — practice to-do

Use this page as a checklist while you practice topics from [Python strings: core concepts](core-concepts.md). Work in a `.py` file or the REPL; check boxes off as you finish each item (in your editor or mentally).

## How to use

- Do tasks **in order** the first time through; later you can skip around.
- After each section, run the **self-check** snippets and compare your output to the hints.
- Keep notes on mistakes—those are what interviews and debugging reward.

---

## 1. Basics — quotes and multiline

- [ ] Create a variable with a string that contains a **single quote** inside (use either mixed quotes or `\'`).
- [ ] Create a variable with a string that contains **double quotes** inside the text.
- [ ] Write a **triple-quoted** string with at least **three lines**; print it and confirm newlines appear.

---

## 2. Length, indexing, slicing

- [ ] For `s = "Programming"`, print `len(s)` and confirm the count by hand.
- [ ] Print the **first** character, the **last** character, and the **third-from-last** using indexing (including negative index for the last).
- [ ] Slice `s` to get exactly `"gram"` (hint: find start/stop; remember stop is **exclusive**).
- [ ] Using slicing only, produce `"Pro"` and `"ing"` from the same `s`.

**Self-check**

```python
s = "Programming"
# Your answers should match:
# len(s) == 11
# s[0] == "P", s[-1] == "g"
# slice for "gram" == "gram"
```

---

## 3. Common methods

- [ ] Start with `"Hello World"`; print `.lower()` and `.upper()` and verify the **original** string is unchanged.
- [ ] On `"mississippi"`, use `.count("i")` and `.count("ss")`; write down the two numbers before you run.
- [ ] Use `.find("ss")` and `.find("zzz")`; know what the second result means.
- [ ] Assign `msg = "one fish two fish"`; call `.replace("fish", "boat")` into a **new** variable; show that `msg` is still the old text, then **reassign** `msg` and show it updated.

---

## 4. Concatenation and formatting

- [ ] Build the exact string `Hello, Ada!` using **`+`** and variables for `Hello` and `Ada` (with comma and space).
- [ ] Build the same idea with **`.format()`** using at least one **named** placeholder (`{name=...}`).
- [ ] Rewrite using an **f-string**; include an expression in `{...}` (for example `.upper()` on a name or `2 + 3`).

---

## 5. Exploring `str` in the REPL

- [ ] Pick any string `s`; print a list of **public** method names (filter out names starting with `_`), similar to the snippet in the core guide.
- [ ] Run `help(str.replace)` and read the first few lines; note what it returns.

---

## 6. Mini-challenges (optional)

Complete without peeking at the guide first; verify with `print`.

- [ ] **Reverse feel (no `[::-1]` required for this list):** using only indexing and slicing on `"Python"`, print `"nohtyP"` as **five** slices/concat steps, *or* do it in one line with slicing `[::-1]` and explain what `::-1` means.
- [ ] **Normalize:** given `raw = "  HeLLo  "`, produce `"hello"` (you may use `.strip()` if you look it up—it's the next natural method after this tutorial).
- [ ] **Template:** given `user = "sam"` and `points = 100`, one f-string that prints: `sam has 100 points` with **both** values coming from variables.

---

## Progress tracker

| Section              | Done |
|----------------------|------|
| 1. Basics            | [ ] |
| 2. Len / index / slice | [ ] |
| 3. Methods           | [ ] |
| 4. Concat / format   | [ ] |
| 5. dir / help        | [ ] |
| 6. Mini-challenges   | [ ] |

---

## See also

- [Python strings: core concepts](core-concepts.md)
- [Python interview Q&A](../interview-questions.md)
