/* similar to java switch case - difference step for different condition
scala's match case is more powerful
1 basic
2 type
3 Array and List
4 case class
5 Option
 */
//------------------------------------------------------------------
// match(case value => what to do}
// _ means all other cases
// if any case satisfies , it will not move onto the next
def judgeGrade(grade: String): Unit ={
  grade match{
    case "A" => println("Excellent")
    case "B" => println("good")
    case "C" => println("just ok")
    case _ => println("should work harder")
  }
}
judgeGrade("A")

// add if to case
def judgeGrade1(name: String, grade: String): Unit ={
  grade match{
    case "A" => println(name + ", Excellent")
    case "B" => println(name + ", good")
    case "C" => println(name + ", just ok")
    case _ if name == "Leo" => println(name + ", You can do better")
    case _ => println(name + "should work harder")
  }
}
judgeGrade1("Leo", "")
// add variable
def judgeGrade2(name: String, grade: String): Unit ={
  grade match{
    case "A" => println(name + ", Excellent")
    case "B" => println(name + ", good")
    case "C" => println(name + ", just ok")
    case _grade if name == "Leo" => println(name + ", your current grade is " + _grade)
    case _grade => println(name + " should work harder, your grade is " + _grade)
  }
}
judgeGrade2("Leo", "A+")
judgeGrade2("Jack", "F")
//------------------------------------------------------------------
// match type, cannot achieve use java, use case variable:type => what to do
// not case value => what to do
import java.io._
def processException(e: Exception): Unit ={
  e match {
    case e1: IllegalArgumentException => println("passed illegal arguments " + e1)
    case e2: FileNotFoundException => println("cannot find your file " + e2)
    case e3: IOException => println("IO error " + e3)
    case _ : Exception => println("check details here " + _)
  }
}
processException(new IllegalArgumentException("expect two args, only found one"))
processException(new IOException("socket fails"))
processException(new ArrayIndexOutOfBoundsException("index out of bound"))
//------------------------------------------------------------------
// match array and list
def greeting(arr: Array[String]): Unit ={
  arr match{
    case Array("Leo") => println("Hi, Leo!")
    case Array(girl1, girl2, girl3) => println("Hi, " + girl1 + "," +girl2 + ","  + girl3 + " !")
    case Array("Leo", _*) => println("Hi, Leo! Can you introduce your friend to me? ")
    case _ => println("Hi, what is your name!")
  }
}
greeting(Array("Leo"))
greeting(Array("Leo", "Emma"))


def greeting1(list: List[String]): Unit ={
  list match{
    case "Leo"::Nil => println("Hi, Leo!")
    case girl1::girl2::girl3::Nil => println("Hi, " + girl1 + "," +girl2 + ","  + girl3 + " !")
    case "Leo"::tail => println("Hi, Leo! Can you introduce your friend to me? ")
    case _ => println("Hi, what is your name!")
  }
}
greeting1(List("Leo", "Emma"))
//------------------------------------------------------------------
//case class
// only defined filed - scala provides getter and setter but no method
// do not need var or val
// scala created companion for case class, which is an object
class Person
case class Teacher(name: String, subject: String) extends Person
case class Student(name: String, classroom: String) extends Person
case class Worker(name: String) extends Person
def identity(p: Person): Unit ={
  p match{
    case Teacher(name, subject) => println(name + " teaches " + subject)
    case Student(name, classroom) => println(name + " is in " + classroom)
    case _ => println("unknown identity")
  }
}
val leo: Person = Student("leo", "class 1")
val tom: Person = Teacher("tom", "math")
val joe: Person = Worker("joe")
identity(leo)
identity(tom)
identity(joe)
//------------------------------------------------------------------
// Option: Some means have value, None means no value
val grades = Map("leo" -> "A", "jack" -> "B", "jen" -> "C")
def getGrade(name: String): Unit ={
  val grade = grades.get(name)
  grade match{
    case Some(grade) => println(name + " grade is " + grade)
    case None => println(name + " has no grade!!")
  }
}
getGrade("emma")