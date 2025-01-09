#include<iostream>
using namespace std;
/////////////////////////////////////////////////////////////

// Structur for singly linear and singly circular

/////////////////////////////////////////////////////////////

template<class T>
struct NodeS  
{            
    T data;
    struct NodeS *next;
};

/////////////////////////////////////////////////////////////

// Structur for doubly linear and Dubly circular

/////////////////////////////////////////////////////////////

template<class T>
struct NodeD  
{            
    T data;
    struct NodeD *next;
    struct NodeD *prev;
};

/////////////////////////////////////////////////////////////
// class of singly linear linked list
/////////////////////////////////////////////////////////////

template<class T>
class SinglyLL
{
    public:
    struct NodeS<T> * first;
    int iCount;

    SinglyLL();
    void Display();
    int Count();
    void InsertFirst(T);
    void InsertLast(T);
    void InsertAtPos(T, int iPos);
    
    void DeleteFirst();
    void DeleteLast();
    void DeleteAtPos(int iPos);
};

template<class T>
SinglyLL<T>::SinglyLL()
{
    first = NULL;
    iCount = 0;
}

template<class T>
void SinglyLL<T>::Display()
{
   cout<<"Elements of Singly Linear Linked list are : "<<"\n";

    NodeS<T> * temp = first;

    while(temp != NULL)
    {
        cout<<"| "<<temp->data<<" |-> ";
        temp = temp -> next;
    }
    cout<<"NULL"<<"\n";
}

template<class T>
int SinglyLL<T>::Count()
{
    return iCount;
}

template<class T>
void SinglyLL<T>::InsertFirst(T no)
{ NodeS<T> * newn = new NodeS<T>;

    newn->data = no;
    newn->next = NULL;

    if(first == NULL)
    {
        first = newn;
    }
    else
    {
        newn->next = first;
        first = newn;
    }
    iCount++;
}

template<class T>
void SinglyLL<T>::InsertLast(T no)
{
    NodeS<T> * newn = new NodeS<T>;

    newn->data = no;
    newn->next = NULL;

    if(first == NULL)
    {
        first = newn;
    }
    else
    {
        NodeS<T> *temp = first;

        while(temp->next != NULL)
        {
            temp= temp -> next;
        }
        temp->next = newn;
    }
    iCount++;
}

template<class T>
void SinglyLL<T>::InsertAtPos(T no, int iPos)
{
    int iCount = Count();

    if((iPos < 1) || (iPos > iCount+1))
    {
        cout<<"Invaild position\n";
        return;
    }

    if(iPos == 1)
    {
        InsertFirst(no);
    }

    else if(iPos == iCount+1)
    {
        InsertLast(no);
    }
    else
    {
        NodeS<T> * temp = first;
        NodeS<T> * newn = new NodeS<T>;

        for(int iCnt = 1; iCnt < iPos -1; iCnt++)
        {
            temp = temp->next;
        }

        newn->next = temp-> next;
        temp->next=newn;

        iCount++;
    }
}


template<class T>
void SinglyLL<T>::DeleteFirst()
{
   if(first == NULL)
    {
        return;
    }
    else if(first -> next == NULL)
    {
        delete first;
        first = NULL;
    }
    else
    {
        NodeS<T> *temp = first;

        first = first->next;
        delete temp;
    }
    iCount--;
}

template<class T>
void SinglyLL<T>::DeleteLast()
{

        if(first == NULL)
    {
        return;
    }
    else if(first -> next == NULL)
    {
        delete first;
        first = NULL;
    }
    else
    {
        NodeS<T> *temp = first;

        while(temp ->next -> next!= NULL)
        {
            temp = temp -> next;
        }

        delete temp->next;
        temp->next = NULL;
    }
    iCount--;
}

template<class T>
void SinglyLL<T>::DeleteAtPos(int iPos)
{}

/////////////////////////////////////////////////////////////
// class of singly circular linked list
/////////////////////////////////////////////////////////////

template<class T>
class SinglyCL
{
    public:
    struct NodeS<T> * first;
    struct NodeS<T> * last;
    int iCount;

    SinglyLC();
    void Display();
    int Count();
    void InsertFirst(T);
    void InsertLast(T);
    void InsertAtPos(T, int iPos);
    
    void DeleteFirst();
    void DeleteLast();
    void DeleteAtPos(int iPos);
};

template<class T>
SinglyCL<T>::SinglyCL()
{
    
    first = NULL;
    iCount = 0;
}

template<class T>
void SinglyCL<T>::Display()
{}

template<class T>
int SinglyCL<T>::Count()
{
    return 0;
}

template<class T>
void SinglyCL<T>::InsertFirst(T no)
{}

template<class T>
void SinglyCL<T>::InsertLast(T no)
{}

template<class T>
void SinglyCL<T>::InsertAtPos(T no, int iPos)
{}


template<class T>
void SinglyCL<T>::DeleteFirst()
{}

template<class T>
void SinglyCL<T>::DeleteLast()
{}

template<class T>
void SinglyCL<T>::DeleteAtPos(int iPos)
{}

/////////////////////////////////////////////////////////////
// class of doubly linear linked list
/////////////////////////////////////////////////////////////

template<class T>
class DoublyLL
{
    public:
    struct NodeD<T> * first;
    int iCount;
    
    DoublyLL();
    void Display();
    int Count();
    void InsertFirst(T);
    void InsertLast(T);
    void InsertAtPos(T, int iPos);
    
    void DeleteFirst();
    void DeleteLast();
    void DeleteAtPos(int iPos);
};

/////////////////////////////////////////////////////////////
// class of Doubly circular linked list
/////////////////////////////////////////////////////////////

template<class T>
class DouclyCL
{
    public:
    struct NodeD<T> * first;
    struct NodeD<T> * last;
    int iCount;

    DouclyCL();
    void Display();
    int Count();
    void InsertFirst(T);
    void InsertLast(T);
    void InsertAtPos(T, int iPos);
    
    void DeleteFirst();
    void DeleteLast();
    void DeleteAtPos(int iPos);
};

// Logic of 32 Fuction 
int main()
{
    SinglyLL <int>obj1;

    obj1.InsertFirst(51);
    obj1.InsertFirst(21);
    obj1.InsertFirst(11);

    obj1.InsertLast(101);
    obj1.InsertLast(111);

    obj1.Display();
    cout<<"Number of elements are :"<<obj1.Count()<<"\n";

    // obj1.DeleteFirst(51);
    // obj1.DeleteFirst(21);
    // obj1.DeleteFirst(11);

    return 0;
}