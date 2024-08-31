/**
 * A generic queue implementation using a singly linked list.
 *
 * @param <T> the type of elements stored in the queue
 */
public class Queue<T> {
    /** The underlying singly linked list for the queue. */
    SList<T> list = new SList<T>();

    /** Default constructor to initialize an empty queue. */
    Queue() {
    }

    /**
     * Enqueues an element into the queue.
     *
     * @param element the element to enqueue
     */
    void enqueue(T element) {
        // Exercise 1a
        list.addLast(element);
    }

    /**
     * Dequeues an element from the queue.
     *
     * @return the dequeued element
     */
    T dequeue() {
        return list.removeFirst(); // Exercise 1b
    }

    /**
     * Gets the element at the front of the queue without removing it.
     *
     * @return the element at the front of the queue
     */
    T queuefront() {
        return list.first.element; // Exercise 1c
    }

    /**
     * Gets the element at the rear of the queue without removing it.
     *
     * @return the element at the rear of the queue
     */
    T queuerear() {
        return list.last.element; // Exercise 1d
    }

    /**
     * Checks if the queue is empty.
     *
     * @return true if the queue is empty, false otherwise
     */
    boolean isEmpty() {
        return list.isEmpty();
    }

    /**
     * Creates a copy of this queue.
     *
     * @return a new queue containing the same elements as this queue
     */
    Queue<T> copyQueue() { // Exercise 2
        Queue<T> Q2 = new Queue<T>();
        // Add your code here
        Node<T> walker = list.first;
        for (int i=0;i<this.list.size;i++){
            Q2.enqueue(walker.element);
            walker = walker.next;
        }
        return Q2;
    }

    /**
     * Checks if this queue is identical to another queue in terms of content and
     * sequence.
     *
     * @param Q2 the queue to compare with
     * @return true if the queues are identical, false otherwise
     */
    boolean isIdentical(Queue<T> Q2) {
        if (this.list.size == Q2.list.size){
            Node<T> walker1 = this.list.first;
            Node<T> walker2 = Q2.list.first;
            for (int i=0;i<this.list.size;i++){
                if (walker1.element!=walker2.element){
                    return false;
                }
                walker1 = walker1.next;
                walker2 = walker2.next;
            }
            return true;
        }
        else {
            return false; // Exercise 3
        }
    }

    /**
     * Prints the elements of the queue horizontally. Handles potential
     *
     */
    void printHorizontal() {
        Node<T> walker = list.first;
        while (walker != null) {
            System.out.print(walker.element + " ");
            walker = walker.next;
        }

    }

}