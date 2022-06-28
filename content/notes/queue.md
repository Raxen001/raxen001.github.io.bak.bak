+++
title="Queue"
+++
# Unit 4

## Queue FIFO ( First In First Out )

- Abstract data type (or) Linear data structure

  - list stack data

- 1st element **REAR**(or)**TAIL**
- removal from **FRONT**
- Once a new element is inserted into the Queue, all the elements inserted before
  the new element in the queue must be removed, to remove the new element.
- `peek()` value of the first element without **dequeing**

- storage requirement o[n]
- time operation o[1]

### Applications

1. Serving requests on a single shared resource, like a printer, CPU task scheduling, etc.
2. In a real-life scenario, Call Centre phone systems use Queues to hold people calling them in order, until a service representative is free.
3. Handling of interrupts in real-time systems. The interrupts are handled in the same order as they arrive i.e. First come first served.

### Queue using array

```c
#include <stdio.h>
#define n 5
int queue[n];
int front = -1, rear = -1;
void enqueue(int x) {
  if (rear == n - 1)
    printf("overflow");
  else if (front == -1 && rear == -1) {
    front = rear = 0;
    queue[rear] = x;
  } else {
    rear++;
    queue[rear] = x;
  }
}
void dequeue() {
  if (front == -1 && rear == -1)
    printf("underflow");
  else if (front == rear) // only element in a queue
    front = rear = -1;
  else {
    printf("element deleted is %d", queue[front]);
    front++;
  }
}
void display() {
  if (front == -1 && rear == -1)
    printf("underflow");
  else {
    for (int i = front; i <= rear; i++)
      printf("%d ", queue[i]);
  }
}
void peek() {
  if (front == -1 && rear == -1)
    printf("underflow");
  else
    printf("element at the front is %d", queue[front]);
}
int main() {
  int x, ch, c;
  printf("\n1.enqueue\n2.dequeue\n3.peek\n4.display");
  do {
    printf("\nenter your choice : ");
    scanf("%d", &ch);
    switch (ch) {
    case 1:
      printf("enter the element to be inserted:");
      scanf("%d", &x);
      enqueue(x);
      break;
    case 2:
      dequeue();
      break;
    case 3:
      peek();
      break;
    case 4:
      display();
    }
    printf("\ndo you wish to continue press (1 - yes and 0 - no) : ");
    scanf("%d", &c);
  } while (c == 1);
}
```

## Circular Queue

### Applications

Ring Buffers are common data structures frequently used when the input and output to a data stream occur at different rates.

- Buffering Data Streams
- Computer Controlled Trafficking signal systems
- Memory Management
- CPU scheduling
- Advantages
- Circular Queues offer a quick and clean way to store FIFO data with a maximum size.

### Advantages

- Doesn’t use dynamic memory → No memory leaks
- Conserves memory as we only store up to our capacity (opposed to a queue which could continue to grow if input outpaces output.)
- Simple Implementation → easy to trust and test
- Never has to reorganize / copy data around
- All operations occur in constant time O(1)
- Disadvantages
- Circular Queues can only store the pre-determined maximum number of elements.

### Disadvantages 

- Have to know the max size beforehand



## Priority Queue

In a queue, the **first-in-first-out** rule is implemented whereas, in a *priority*
queue, the values are removed on the basis of **priority**. The element with the
**highest priority is removed first**.
