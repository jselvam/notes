Imagine an Operating System managing **running processes**.

Each process is stored in a list.

```python
processes = [
    "chrome.exe",
    "spotify.exe",
    "python.exe",
    "vscode.exe",
    "notepad.exe"
]
```

Think of this like **Task Manager** in Windows or `top` in Linux.

---

# 1. `remove()` → Kill process by name

OS searches process by name and stops it.

```python
processes.remove("spotify.exe")

print(processes)
```

Output:

```python
['chrome.exe', 'python.exe', 'vscode.exe', 'notepad.exe']
```

### Real OS analogy

You open Task Manager and choose:

> End Task → Spotify

The OS removes the process by its **name/value**.

---

# 2. `pop()` → Remove latest/background process and return it

Suppose OS removes the last started process and logs it.

```python
killed_process = processes.pop()

print("Killed:", killed_process)
print(processes)
```

Output:

```python
Killed: notepad.exe
['chrome.exe', 'python.exe', 'vscode.exe']
```

### Real OS analogy

OS scheduler removes a process from memory and records:

> “Process notepad.exe terminated.”

Important:
`pop()` returns the removed process.

---

# 3. `del` → Force remove process by index

Suppose OS knows exact position in process table.

```python
del processes[1]

print(processes)
```

Output:

```python
['chrome.exe', 'vscode.exe']
```

### Real OS analogy

Kernel directly removes process entry from process table using memory/index location.

This is more low-level.

---

# 4. `clear()` → Shutdown all processes

System shutdown clears all running processes.

```python
processes.clear()

print(processes)
```

Output:

```python
[]
```

### Real OS analogy

During shutdown:

* all applications close
* RAM process list becomes empty

But the process table structure still exists.

---

# BONUS — `del processes`

```python
del processes
```

### Real OS analogy

The OS destroys the entire process table object itself.

After this:

```python
print(processes)
```

You get:

```python
NameError
```

Because the variable no longer exists.

---

# Full OS Simulation Program

```python
processes = [
    "chrome.exe",
    "spotify.exe",
    "python.exe",
    "vscode.exe",
    "notepad.exe"
]

# remove by name
processes.remove("spotify.exe")
print("After remove():", processes)

# remove last process
killed = processes.pop()
print("Popped Process:", killed)
print("After pop():", processes)

# remove by index
del processes[1]
print("After del:", processes)

# clear all
processes.clear()
print("After clear():", processes)
```

---

# Interview Memory Trick

Think of OS Task Manager:

| Operation  | OS Meaning                             |
| ---------- | -------------------------------------- |
| `remove()` | End task by process name               |
| `pop()`    | Remove and get terminated process      |
| `del`      | Force delete process entry by position |
| `clear()`  | Shutdown all running processes         |
