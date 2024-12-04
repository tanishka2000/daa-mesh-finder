# Graph Mesh Finder

Graph Mesh Finder is a Python-based tool designed to identify mesh topologies in graph-based networks. This project aims to bridge the concepts of computer network topologies and graph theory by applying algorithms to detect a mesh structure in various network configurations.

## Project Description

We came across an algorithm for finding the **maximum clique** in a graph, which inspired us to explore its application in detecting **mesh topologies**. Drawing from our studies in Computer Network Topologies (CNT), we realized the similarity between the two concepts. This project is an attempt to integrate theoretical knowledge from both subjects by developing a practical tool to identify mesh-like structures in networks.

Given network configurations in JSON format, this tool applies graph algorithms to detect and analyze mesh topologies, providing insights into the network structure.

### Key Features

- **Integration of Graph Theory and Networking**: Utilizes concepts from graph theory to explore mesh topologies in network configurations.
- **JSON-based Input**: Processes network configurations provided in a flexible JSON format.
- **Mesh Detection**: Implements algorithms to identify mesh-like structures (similar to the maximum clique problem).
- **Educational Value**: Serves as a practical application of academic concepts, bridging graph theory and network topology.

---

## Installation and Usage

### Prerequisites

- Python 3.8+ installed on your system.
- Required libraries listed in the `requirements.txt` file.

### Steps to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tanishka2000/graph-mesh-finder.git
   cd graph-mesh-finder
   ```

2. **Install Dependencies**:
   Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Main Script**:
   Execute the primary script:
   ```bash
   python main.py
   ```

4. **Provide Input Files**:
   Use sample JSON files (`input1.json` to `input5.json`) or create your own input files. Place them in the project directory and configure the script to read them.

---

## Input Format

The JSON input should define the graph structure as follows:
```json
{
  "nodes": [
    {"id": 1, "x": 0, "y": 0},
    {"id": 2, "x": 1, "y": 1}
  ],
  "edges": [
    {"source": 1, "target": 2}
  ]
}
```

- **Nodes**: Represents entities in the network.
- **Edges**: Represents the connections or links between nodes.

---

## Example Use Case

### Input:
A network represented as:
```json
{
  "nodes": [
    {"id": 1, "x": 0, "y": 0},
    {"id": 2, "x": 1, "y": 1},
    {"id": 3, "x": 2, "y": 2}
  ],
  "edges": [
    {"source": 1, "target": 2},
    {"source": 2, "target": 3},
    {"source": 1, "target": 3}
  ]
}
```

### Output:
The algorithm identifies a mesh topology consisting of nodes {1, 2, 3} and edges forming a complete graph.

---

## Project Structure

```
graph-mesh-finder/
├── modules/
│   ├── algorithm.py      # Core algorithms for mesh detection
│   ├── utils.py          # Helper functions
├── input/
│   ├── input1.json       # Sample input files
├── main.py               # Main script
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## Contributing

We welcome contributions to improve this project! Here’s how you can help:

1. Fork the repository.
2. Create a new branch for your feature (`feature/your-feature`).
3. Commit your changes with clear and descriptive messages.
4. Push to your fork and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

If you have questions or suggestions, feel free to open an issue or reach out via this repository.

---

This README provides a clear project description, user instructions, and insights into its purpose and implementation. Let me know if you’d like further refinements!
