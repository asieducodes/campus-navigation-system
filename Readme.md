# 🗺 KNUST Campus Navigation System

> An interactive web-based campus pathfinding system built with Python and Streamlit — demonstrating graph data structures, four classic algorithms, and real-time path animation.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B?style=flat-square&logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.18%2B-3F4F75?style=flat-square&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📌 Project Overview

This system models the KNUST campus as a **weighted undirected graph**, where:

- **Nodes** = campus buildings / locations
- **Edges** = walkable paths between locations
- **Weights** = distance (metres) + walking time (minutes)

Users interact through a **modern browser-based UI** powered by Streamlit. They can find optimal routes, animate algorithm traversal step by step, compare all four algorithms side by side, and manage the campus map live — all from a single web interface.

**Course:** Data Structures & Algorithms — COE 363
**Department:** Computer Engineering, KNUST
**Supervisor:** Dr. T. S. M. Adjaidoo
**Group:** 13

---

## 🏗 Project Structure

```
campus_navigation_system/
│
├── app.py                      ← Streamlit entry point — run this
├── streamlit_utils.py          ← Shared helpers, Plotly graph builder, algo runner
├── requirements.txt            ← All Python dependencies
├── README.md                   ← This file
│
├── graph/
│   ├── __init__.py
│   ├── node.py                 ← Node class — represents one campus location
│   └── graph.py                ← Graph class — adjacency list + full CRUD
│
├── algorithms/
│   ├── __init__.py
│   ├── bfs.py                  ← Breadth-First Search
│   ├── dfs.py                  ← Depth-First Search
│   ├── dijkstra.py             ← Dijkstra's Algorithm
│   └── astar.py                ← A* Pathfinding
│
├── pages_nav/
│   ├── __init__.py
│   ├── page_navigate.py        ← 🗺  Find Path — main pathfinding page
│   ├── page_compare.py         ← 📊  Compare Algorithms — side-by-side analysis
│   ├── page_learn.py           ← 📚  Learn Algorithms — educational deep-dives
│   └── page_manage.py          ← ⚙️   Manage Graph — add/remove locations and paths
│
├── storage/
│   ├── __init__.py
│   └── data_manager.py         ← JSON save / load / default KNUST graph seed
│
├── data/
│   └── campus_map.json         ← Persisted graph (auto-generated on first run)
│
└── tests/
    ├── __init__.py
    └── test_all.py             ← 40+ pytest test cases
```

---

## 🏫 Campus Locations

| Location | Coordinates | Description |
|---|---|---|
| Main Gate | (10, 50) | Primary campus entrance |
| Admin Block | (25, 65) | University administration offices |
| Library | (40, 70) | Central study hub |
| Cafeteria | (40, 50) | Student dining hall |
| SRC | (55, 60) | Student Representative Council |
| Lecture Hall | (55, 80) | Main lecture hall complex |
| Engineering Block | (70, 70) | College of Engineering |
| Sports Complex | (70, 35) | Stadium, courts, and gym |

**Graph stats:** 8 nodes · 12 edges · undirected · weighted by distance and time

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/asieducodes/campus-navigation-system.git
cd campus-navigation-system

# 2. Install dependencies
pip install -r requirements.txt
```

**requirements.txt includes:**
```
streamlit>=1.32.0
plotly>=5.18.0
pandas>=2.0.0
networkx>=3.0
matplotlib>=3.7
pytest>=7.0
```

---

## 🚀 Running the App

```bash
streamlit run app.py
```

The app opens automatically at `http://localhost:8501` in your browser. On first run, the default KNUST campus map is built and saved to `data/campus_map.json` automatically — no setup required.

---

## 🧭 App Pages

### 🗺 Find Path
The main navigation screen. Select a start location and destination, choose an algorithm, and click **Find Path**. The interactive Plotly campus map highlights the shortest route instantly. Click **Animate Traversal** to watch the algorithm explore the graph node by node with a live progress bar.

### 📊 Compare Algorithms
Run all four algorithms on the same route simultaneously. See metric cards, a full comparison table, two bar charts (distance vs nodes explored), and four mini campus maps — one per algorithm — showing each path highlighted differently.

### 📚 Learn Algorithms
One tab per algorithm. Each tab explains how the algorithm works, shows its properties (data structure, time complexity, optimality), displays pseudocode, and includes a live demo on the real campus map. A **Compare All** tab shows the full BFS → DFS → Dijkstra → A* progression story.

### ⚙️ Manage Graph
Add new campus locations with coordinates, connect them with weighted paths, remove existing locations or edges, and watch the live campus map update instantly. Save the graph to JSON or reload the default KNUST map at any time.

---

## 🧪 Running Tests

```bash
pytest tests/test_all.py -v
```

The test suite covers node creation, graph CRUD operations, BFS/DFS traversal correctness, Dijkstra optimality, and A* heuristic consistency — 40+ cases in total.

---

## 📐 Data Structures

| Structure | Where Used | Why |
|---|---|---|
| `dict` (Hash Map) | `Graph.locations`, `Graph.adjacency` | O(1) average node and edge lookup |
| Adjacency List | `Graph.adjacency` | O(V+E) space — efficient for sparse campus graphs |
| `deque` (Queue) | BFS | FIFO traversal; `popleft()` is O(1) |
| `list` (Stack) | DFS iterative | LIFO traversal; `append/pop` are O(1) |
| Call Stack | DFS recursive | Implicit LIFO via Python's recursion mechanism |
| `heapq` (Min-Heap) | Dijkstra, A* | O(log V) priority extraction — essential for efficiency |

---

## 🧠 Algorithms

### 🔵 Breadth-First Search (BFS)
Explores all neighbours at distance k before moving to k+1. Uses a `deque` (FIFO queue). Guarantees the fewest-hops path — ignores edge weights.

- **Time:** O(V + E) · **Space:** O(V)
- **Best for:** Fewest stops, unweighted shortest path, connectivity checks

### 🟣 Depth-First Search (DFS)
Goes as deep as possible along each branch before backtracking. Uses recursion (call stack) or an explicit list as a stack (LIFO). Does **not** guarantee the shortest path.

- **Time:** O(V + E) · **Space:** O(V)
- **Best for:** Cycle detection, exploring all possible routes

### 🟢 Dijkstra's Algorithm
Greedily expands the node with the lowest known cumulative cost using a min-heap. Edge relaxation updates cheaper paths as they are discovered. Guaranteed optimal for non-negative weights.

- **Time:** O((V + E) log V) · **Space:** O(V)
- **Best for:** Minimum distance or minimum time routing

### 🟠 A\* Pathfinding
Combines Dijkstra's optimality with a Euclidean heuristic `h(n)` that estimates the remaining cost to the goal. Prioritises nodes by `f(n) = g(n) + h(n)`, steering the search toward the destination and exploring fewer nodes.

- **Time:** O((V + E) log V) · **Space:** O(V)
- **Best for:** Fastest optimal path when (x, y) coordinates are available

---

## 🆚 Algorithm Comparison

| Feature | BFS | DFS | Dijkstra | A* |
|---|---|---|---|---|
| Guarantees shortest path? | ✅ hops | ❌ | ✅ weighted | ✅ weighted |
| Uses edge weights? | ❌ | ❌ | ✅ | ✅ |
| Uses heuristic? | ❌ | ❌ | ❌ | ✅ |
| Data structure | Queue | Stack / Recursion | Min-Heap | Min-Heap + h(n) |
| Time complexity | O(V+E) | O(V+E) | O((V+E)logV) | O((V+E)logV) |
| Explores fewer nodes? | ⚖️ | ⚖️ | ⚖️ | ✅ |

---

## 🎨 Visualisation Colour Coding

| Colour | Meaning |
|---|---|
| 🔵 Blue | Unexplored campus location |
| 🟢 Green | Already visited during traversal |
| 🔴 Red | Node on the final shortest path |
| 🟠 Orange edge | Highlighted route edge |

---

## 📂 JSON Storage Format

The campus graph is saved to `data/campus_map.json` with this structure:

```json
{
  "nodes": {
    "Library": {
      "name": "Library",
      "coords": [40, 70],
      "description": "Central study hub"
    }
  },
  "edges": {
    "Library": {
      "Admin Block": { "distance": 220, "time": 2.8 }
    }
  }
}
```

Each edge is stored once (where `loc1 < loc2` alphabetically). Both directions are reconstructed automatically on load.

---

## 👥 Group Members

| # | First Name(s) | Last Name | Student ID |
|---|---|---|---|
| 1 | Tyrone Nii Dromo Tettey | Addy | 20984701 |
| 2 | Timothy Joshua Ashirifi | Ago-Larsey | 21002785 |
| 3 | Samuella | Andoh Bannerman | 20985108 |
| 4 | Prince | Appau | 20274915 |
| 5 | Seth Osei | Asiedu | 21011542 |
| 6 | Emzera Akosua Oye | Ayesu | 21021727 |
| 7 | Joshua | Darrah | 20972117 |
| 8 | Emmanuel | Gyapong | 21026604 |
| 9 | Michael Awinneriba | Nkema | 21037754 |
| 10 | Kwame Nketia | Owusu | 21015744 |

---

## 📚 Learning Objectives

After working through this project you will understand:

- How to represent a real-world network as a weighted undirected graph
- Why adjacency lists outperform adjacency matrices for sparse graphs
- How BFS and DFS differ in traversal order and what that means for path quality
- Why Dijkstra requires a priority queue and what edge relaxation does
- How A* uses a spatial heuristic to outperform Dijkstra without sacrificing optimality
- How to build a multi-page web application with Streamlit
- How to structure a modular Python project with clean separation of concerns
- How to write meaningful unit tests with pytest

---

## 🔮 Future Improvements

- Integrate real KNUST campus GPS coordinates
- Live obstacle and path closure detection
- Real-time crowd density as a dynamic edge weight
- Deploy publicly via Streamlit Cloud for a shareable URL
- Mobile-responsive layout improvements
- Multi-floor indoor navigation support