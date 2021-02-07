import java.util.*;

public class LinkedList {
    private class Node {
        int data;
        Node next;
    }

    Node head;
    int size = 0;

    public void insert(int data) {
        Node node = new Node();
        node.data = data;

        // we're adding the first node to our linked list
        if (head == null) {
            head = node;
        } else {
            Node n = head;
            while (n.next != null) {
                n = n.next;
            }
            n.next = node;
        }

        size++;
    }

    public void insert_all(int[] arr) {
        for (int n : arr) {
            insert(n);
        }
    }

    public void show() {
        Node n = head;
        while (n != null) {
            System.out.print(n.data + "->");
            n = n.next;
        }
        System.out.println();
    }

    public void reverse() {
        Node prev = null;
        Node curr = head;
        while (curr != null) {
            Node next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;
    }

    public void delete(int d) {
        Node prev = null;
        Node curr = head;
        //head
        if (curr != null && curr.data == d) {
            head = curr.next;
            return;
        }
        //search
        while (curr != null && curr.data != d) {
            prev = curr;
            curr = curr.next;
        }
        //if key is not present
        if (curr == null) return;
        //unlink node from linked list
        prev.next = curr.next;
    }

    public void delete_at_pos(int position) {
        //position out of bounds
        if (position > size-1) return;
        //deleting head
        if (position == 0) {
            head = head.next;
            return;
        }
        //deleting some node that's after head
        int counter = 0;
        Node n = head;
        while (counter < position-1) {
            n = n.next;
            counter++;
        }
        n.next = n.next.next;
    }

    public int get_nth(int index) {
        Node n = head;
        int count = 0;
        while (n != null) {
            if (count == index) {
                return n.data;
            }
            count++;
            n = n.next;
        }
        //index out of bound
        return -1;
    }

    public int get_nth_from_end(int index) {
        Node p1 = head;
        Node p2 = head;
        //move p1 k nodes into the list
        for (int i = 0; i < index; i++) {
            if (p1 == null) return -1; //out of bounds
            p1 = p1.next;
        }
        //move them at the same place
        //when p1 hits the end, p2 will bee at right element
        while (p1 != null) {
            p1 = p1.next;
            p2 = p2.next;
        }
        return p2.data;
    }

    public int length() {
        Node n = head;
        int count = 0;
        while (n != null) {
            count++;
            n = n.next;
        }
        return count;
    }

    public boolean contains(int num) {
        Node n = head;
        while (n != null) {
            if (n.data == num) return true;
            n = n.next;
        }
        return false;
    }

    public int middle() {
        Node slow = head;
        Node fast = head;
        if (head != null) {
            while (fast != null && fast.next != null) {
                fast = fast.next.next;
                slow = slow.next;
            }
            return slow.data;
        }
        return -1;
    }

    public boolean detectLoop() {
        Node n = head;
        HashSet<Node> s = new HashSet<Node>();
        while (n != null) {
            if (s.contains(n)) return true;
            s.add(n);
            n = n.next;
        }
        return false;
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        int[] arr = new int[]{1,2,3,4,5,6,7,8,9};
        list.insert_all(arr);
        list.show();
        // list.reverse();
        // list.show();
        // list.delete_at_pos(0);
        // list.show();
        // list.delete(1);
        System.out.println(list.get_nth(100));
        System.out.println(list.length());
        System.out.println(list.contains(3));
        System.out.println(list.get_nth_from_end(2));
        // list.show();
        list.show();
        System.out.println(list.middle());
        System.out.println(list.detectLoop());
    }


}