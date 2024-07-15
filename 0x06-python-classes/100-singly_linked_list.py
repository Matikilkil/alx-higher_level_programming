#!/usr/bin/python3
"""
Module: 100-singly_linked_list
"""


class Node:
    """
    Defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes the Node with data and next_node.

        Args:
            data (int): The data stored in the node.
            next_node (Node): The next node in the linked list.
            Defaults to None.

        Raises:
            TypeError: If data is not an integer or
            next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data from the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data of the node.

        Args:
            value (int): The new data for the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next node.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node.

        Args:
            value (Node): The new next node.

        Raises:
            TypeError: If next_node is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes the SinglyLinkedList with no nodes.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value (int): The data value for the new Node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and
            current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Prints the entire list in stdout, one node number by line.

        Returns:
            str: String representation of the linked list.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
