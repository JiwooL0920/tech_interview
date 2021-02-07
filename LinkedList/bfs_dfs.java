//DFS
void search(Node root) {
    if (root == null) return;
    visit(root);
    root.visited = true;
    for (Node n : root.adjacent) {
        if (!visited) {
            search(n);
        }
    }
}


//BFS
void search(Node root) {
    Queue queue = new Queue();
    root.marked = true;
    queue.enqueue(root);
    while (!queue.isEmpty()) {
        Node r = queue.dequeue();
        visit(r);
        for (Node r : r.adjacent) {
            if (!n.marked) {
                n.marked = true;
                queue.enquque(n);
            }
        }
    }
}