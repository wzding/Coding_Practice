/* similar to java switch case - difference step for different condition
scala's match case is more powerful
1 basic
2 type
3 Array and List
4 case class
5 Option
 */

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



// match array and list
