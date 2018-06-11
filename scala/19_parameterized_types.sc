import com.sun.javadoc.ParameterizedType

/*  Parameterized Types
1. upper bounds
2. lower bounds
3. view bounds
4. context bounds
5. manifest context bounds
6. existential type
*/
//------------------------------------------------------------------
// broad type class
class Student[T](val localId: T){
  def getSchoolId(stdId: T) = "S-" + stdId + "-" + localId
}
val leo = new Student[Int](123)
//leo.getSchoolId("222") // type mismatch
leo.getSchoolId(222)
//------------------------------------------------------------------
// broad type function
def getCard[T](content:T)={
  if(content.isInstanceOf[Int]) "card: 001, " + content
  else if(content.isInstanceOf[String]) "card: this is your card, " + content
  else "card: " + content
}
getCard[Int](100)
getCard[String]("Happy birthday")
getCard("Happy birthday") // no need to specify type
//------------------------------------------------------------------
//upper bounds
class Person(val name: String){
  def sayHello = println("Hi, I'm " + name)
  def makeFriends(p: Person): Unit ={
    sayHello
    p.sayHello
  }
}
class Student1(name: String) extends Person(name)
// <: upper bound
class Party[T <: Person](p1: T, p2: T){
  def play = p1.makeFriends(p2)
}
val emma = new Student1("emma")
val tom = new Person("tom")
val party = new Party(emma, tom)
party.play
//------------------------------------------------------------------
// lower bounds
class Parent(val name: String)
class Child(name: String) extends Parent(name)
// >: lower bound
def getIDCard[R >: Child](person: R): Unit ={
  if (person.getClass == classOf[Child]) println("what are your parents' names?")
  else if(person.getClass == classOf[Parent]) println("please sign here")
  else println("you are not supposed to be here")
}
getIDCard(emma)
val jack = new Parent("jack")
getIDCard(jack)
val joy = new Child("joy")
getIDCard(joy)
//------------------------------------------------------------------
//view Bounds - include both upper and lower bounds <%
class Dog(val name: String){
  def sayHello = println("Wang, wang. I'm " + name)
}
implicit def dog2person(dog: Object): Person = if(dog.isInstanceOf[Dog]){
  val _dog = dog.asInstanceOf[Dog]; new Person(_dog.name)} else Nil
class Party1[T <% Person](p1: T, p2: T)
val doggy = new Dog("doggy")
val pat = new Party1(leo, doggy)
//------------------------------------------------------------------
// context bounds
class Calculator[T: Ordering](val number1:T, val number2:T){
  def max(implicit order: Ordering[T]) = if(order.compare(number1, number2) >0) number1 else number2
}
val cal = new Calculator(1, 2)
cal.max
// Manifest context bounds
class Meat(val name: String)
class Vege(val name: String)
def packageFood[T: Manifest](food: T*) = {
  val foodPackage = new Array[T](food.length)
  for(i <- 0 until food.length) foodPackage(i) = food(i)
  foodPackage
}
val m = new Meat("pork")
val c = new Meat("chicken")
val pak = packageFood(m,c)
pak
//------------------------------------------------------------------
class Master
class Professional extends Master
// both master and below are ok
class Card[+T](val name: String)
def enterMeeting(card: Card[Master]){
  println("welcome!")
}
val jane = new Card[Master]("jane")
val amy = new Card[Professional]("amy")
enterMeeting(jane)
enterMeeting(amy)
// another way to use
class Card1[-T](val name: String)
def enterMeeting1(card: Card1[Professional]){
  println("welcome!")
}
val emma1 = new Card1[Master]("emma")
val john = new Card1[Professional]("john")
enterMeeting1(emma1)
enterMeeting1(john)
//------------------------------------------------------------------
// Existential Type
//Array[T] forSome {type T}
//Array[_]
//------------------------------------------------------------------








