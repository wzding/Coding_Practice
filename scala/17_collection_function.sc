/*
Iterable, Seq, Set, Map
Iterable is the root trait of set trait
scala' collections have two types: mutable and immutable scala.collection.mutable & scale.collection.immutable

Seq include: Range, ArrayBuffer, List
1 List
2 LinkedList
3 Set
4 example
*/

//------------------------------------------------------------------
// range
1 to 10
1 until 10
1.to(10)
1.until(10)
//------------------------------------------------------------------
// list is immutable, it has head and tail
// :: to combine element with list
val list = List(1,2,3,4)
val list1 = List.apply(1,2,3,4) // companion object
list.head
list.tail
0::list
List(4).tail == Nil

// add prefix to all elements in a list
def decorate(l:List[Int], prefix: String): Unit ={
  if (l != Nil){
    println(prefix + l.head)
    decorate(l.tail, prefix)
  }
}
decorate(List(3,6,7,4), "+")
decorate(List(), "+")
//------------------------------------------------------------------
// LinkedList is mutable, typically use elem and next rather than head and tail though the values are the same
val l=scala.collection.mutable.LinkedList(1,2,3,4,5)
l.elem
l.head
l.next
l.tail

// multiply 2 for all elements in list
val list2 = scala.collection.mutable.LinkedList(1,2,3,4,5)
var currentList = list2
while (currentList != Nil){
  currentList.elem = currentList.elem * 2
  currentList = currentList.next
}
list2

// multiply 2 for every other element in list
val list3 = scala.collection.mutable.LinkedList(1,2,3,4,5)
var currentList1 = list3
var first = true
while(currentList1 != Nil && currentList1.next != Nil){
  if(first){currentList1.elem = currentList1.elem * 2; first = false}
  currentList1 = currentList1.next.next
  currentList1.elem = currentList1.elem * 2
}
list3
//------------------------------------------------------------------
//set no duplicates, no order
val s = Set(1,2,3)
s + 4
// no order
val s1 = new scala.collection.mutable.HashSet[Int](); s1 += 1; s1 +=3 ; s1 +=2
s1
scala.collection.mutable.HashSet[Int](1,5,3,4,7,2)
// insert order
val s2 = new scala.collection.mutable.LinkedHashSet[Int](); s2 += 1; s2 +=3 ; s2 +=2
s2
scala.collection.mutable.LinkedHashSet[Int](1,5,3,4,7,2)
// sorted set
scala.collection.mutable.SortedSet.apply("banana", "apply", "orange")
//------------------------------------------------------------------
// collection + function -> high-order function: receive other function as input
List("Leo", "Emma", "Jen").map("name is " + _)
List("Hello World", "You Me").flatMap(_.split(" "))
List("I", "have", "a", "beautiful", "house").foreach(println(_))
List("Leo","Jen", "Peter").zip(List(100, 85, 94))

//count number of words in multiple text files
//val lines1 = scala.io.Source.fromFile("test01.txt").mkString
//val lines2 = scala.io.Source.fromFile("test02.txt").mkString
val lines = List("hello world", "hello Emma")
lines.flatMap(_.split(" ")).map((_, 1)).map(_._2).sum
//------------------------------------------------------------------