# Multiply two linked lists
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def convertToLL(l):
    if not l:
        return None
    
    head=node(l[0])
    temp=head
    for i in range(1,len(l)):
        temp.next=node(l[i]) # type: ignore
        temp=temp.next
    
    return head

def multiply(head1,head2):
    n1=0
    n2=0
    while head1 or head2:
        if head1:
            n1=n1*10+head1.data
            head1=head1.next
        if head2:
            n2=n2*10+head2.data
            head2=head2.next
        
    return n1*n2
l1=[3,2]
l2=[2]
head1=convertToLL(l1)
head2=convertToLL(l2)
res=multiply(head1,head2)
# tmp=head1
# while tmp is not None:
#     print(tmp.data,end=" - > " if tmp.next else "")
#     tmp=tmp.next
mod=res%1000000007
print(mod)