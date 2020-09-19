from __future__ import annotations
from typing import Any, Type


class Node:



    def __init__(self, data:Any=None,prev:Node=None, next:Node=None)-> None:
        ####reset

        self.data=data
        self.prev=prev or self
        self.next=next or self

class DoubleLinkedList:

    def __init__(self)-> None:

        self.head=self.current=Node()
        self.no=0

    def __len__(self)-> int:
        return self.no

    def is_empty(self)->bool:
        return self.head.next is self.head



    def search(self,data:Any)-> Any:
        cnt=0
        ptr=self.head.next
        while ptr is not self.head:
            if data==ptr.data:
                self.current=ptr
                return cnt
            
            cnt+=1
            ptr=ptr.next
        return -1
    def __contain_(self,data:Any)-> bool:

        return self.search(data)>=0



    def print_current_node(self)-> None:

        if self.is_empty():
            print(
                '주목 노드는 없습니다.'
            )
        else:
            print(self.current.data)


    def print(self)->None:
        ptr=self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr=ptr.next
    def print_reverse(self)-> None:

        ptr=self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr=ptr.prev

    def next(self)-> bool:
        ##주목 노드를 한 칸 뒤로 이동

        if self.is_empty( ) or self.current.next is self.head:
            return False
        self.current=self.current.next
        return True


    def prev(self)-> bool:
        if self.is_empty( ) or self.current.prev is self.head:
            return False

        self.current=self.current.prev
        return True


    def add(self, data: Any) -> None:
        """주목 노드의 바로 뒤에 노드를 삽입"""
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        self.current = self.head  # 더미 노드 head의 바로 뒤에 삽입
        self.add(data)

    def add_last(self, data: Any) -> None:  
        """맨 뒤에 노드를 삽입"""
        self.current = self.head.prev  # 꼬리 노드 head.prev의 바로 뒤에 삽입
        self.add(data)

# Do it! 실습 8-5[E]
    def remove_current_node(self) -> None:
        """주목 노드 삭제"""
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next

    def remove(self, p: Node) -> None:
        """노드 p를 삭제"""
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:  # p를 발견
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next

    def remove_first(self) -> None:
        """머리 노드 삭제"""
        self.current = self.head.next  # 머리 노드 head.next를 삭제
        self.remove_current_node()

    def remove_last(self) -> None:
        """꼬리 노드 삭제"""
        self.current = self.head.prev  # 꼬리 노드 head.prev를 삭제
        self.remove_current_node()

    def clear(self) -> None:
        """모든 노드를 삭제"""
        while not self.is_empty():  # 리스트 전체가 빌 때까지
            self.remove_first()  # 머리 노드를 삭제
        self.no = 0

# Do it! 실습 8-5[F]
    def __iter__(self) -> DoubleLinkedListIterator:
        """반복자를 반환"""
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        """내림차순 반복자를 반환"""
        return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    """DoubleLinkedList의 반복자용 클래스"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:
    """DoubleLinkedList의 내림차순 반복자용 클래스"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data