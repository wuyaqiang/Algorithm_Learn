
public class DoublyLinkList<Item> {

    private class DoubleNode {
        Item data;
        DoubleNode previous;
        DoubleNode next;
    }

    private int size;
    private DoubleNode first;
    private DoubleNode last;

    public boolean isEmpty() {
        return size == 0;
    }
    public int size() {
        return size;
    }

    public void insertHead(Item data) {
        // 在链表表头插入结点
        DoubleNode old_first = first;

        first = new DoubleNode();
        first.data = data;
        first.next = old_first;

        if (old_first != null) {
            old_first.previous = first;
        }
        // 如果old_first == null,则不存在old_first.previous,不需要处理
        if (isEmpty()) {
            last = first;
        }

        size++;

    }
    
    public void insertTail(Item data) {
        // 在链表表尾插入结点
        DoubleNode old_last = last;

        last = new DoubleNode();
        last.data = data;
        last.previous = old_last;

        if (old_last != null) {
            old_last.next = last;
        }
        if (isEmpty()) {
            first = last;
        }

        size++;
    }

    public Item deleteHead() {
        // 删除表头结点，并返回表头结点的data值
        if (isEmpty()) {
            return null;
        }
        Item data = first.data;
        if (first.next != null) {
            first.next.previous = null;
        } else {
            last = null;
        }
        first = first.next;
        size--;
        
        return data;
    }

    public Item deleteTail() {
        // 删除表尾结点，并返回表尾结点的data值
        if (isEmpty()) {
            return null;
        }
        Item data = last.data;
        if (last.previous != null) {
            last.previous.next = null;
        } else {
            first = null;
        }
        last = last.previous;
        size--;

        return data;
    }

}