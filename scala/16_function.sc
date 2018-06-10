/*
functions are independent, do not need to reply on class and object
scala: both object oriented and process oriented
why not replace Java: lots of applications, such as Spring, Lucene, Activiti, Hadoop

1. set a function as a variable
2. anonymous function
3. high-order function
4. type of high level function
5. commonly used high level function
6. Closure
7. SAM transformation
8. Currying function
9. return different from Java
*/
//------------------------------------------------------------------
// independent function
def sayHello(name:String){println("Hello, " + name)}
// add space and _ when define a value as a function
val sayHelloFunc = sayHello _
sayHelloFunc("leo")
//------------------------------------------------------------------
// anonymous function syntax
val sayHelloFunc1 = (name: String) => println("Hello, " + name)
//------------------------------------------------------------------
//high-order function
val sayHelloFunc2 = (name: String) => println("Hello, " + name)
def greeting(func: (String) => Unit, name: String){func(name)}
// greeting is a high-order function
greeting(sayHelloFunc2, "leo")
// another example
Array(1,2,3,4,5).map((num: Int) => num * num)
//return a function
def getGreetingFunc(msg: String) = (name: String) => println(msg + ", " + name)
val greetingFunc = getGreetingFunc("hello ")
greetingFunc("leo")
val greetingFunc1 = getGreetingFunc("how are you ")
greetingFunc1("leo")

//don't need to specify type, if there is only one variable, it's ok to remove ()
// if the only variable will only be used once, could use _ instead
def greeting1(func:(String) => Unit, name: String){func(name)}
greeting1((name: String) => println("Hello, " + name), "leo")
// do not need to specify type of name
greeting1((name) => println("Hello, " + name), "leo")
// if there is only one variable, it's ok to remove ()
greeting1(name => println("Hello, " + name), "leo")
// if the only variable will only be used once, could use _ instead
def triple(func: (Int) => Int ) = {func(3)}
triple(3 * _)
triple(5 * _)

//commonly used high-order function
Array(1,2,3,4,5).map(2 * _)
// foreach does not return values
(1 to 9).map("*" * _).foreach(println _)
(1 to 20).filter(_ % 2 == 0)
//reduceLeft
(1 to 9).reduceLeft(_ * _)
//sortWith
Array(3, 2, 5, 4, 10, 1).sortWith(_ < _)
//------------------------------------------------------------------
// Closure
def getGreetingFunc1(msg: String) = (name: String) => println(msg + "," + name)
// msg can be used beyond its scope --> closure
val greetingFuncHello = getGreetingFunc1("hello")
greetingFuncHello("leo")
val greetingFuncHi = getGreetingFunc1("hi")
greetingFuncHi("leo")
//------------------------------------------------------------------
//SAM single abstract method, transfer SAM to scala function
import javax.swing._
import java.awt.event._

val button = new JButton("Click")
// java syntax
button.addActionListener(new ActionListener {
  override def actionPerformed(event: ActionEvent): Unit ={
    println("Click Me!")
  }
})

// the code below does not work, type mismatch need ActionListener
//button.addActionListener((event: ActionEvent) => println("Click Me!"))

// scala
implicit def getActionListener(actionProcessFunc:(ActionEvent)=>Unit) = new ActionListener{
  override def actionPerformed(event: ActionEvent): Unit ={
    actionProcessFunc(event)
  }
}
button.addActionListener((event: ActionEvent)=>println("Click Me!"))
//------------------------------------------------------------------
// Currying function
def sum(a: Int, b: Int) = a + b
sum(1,1)

def sum2(a: Int)=(b:Int)=> a+b
sum2(1)(1)

def sum3(a:Int)(b:Int) = a + b
sum3(1)(1)
//------------------------------------------------------------------
//return - unanonymous function use anonymous function - must specify return type
//normally the last line is the returned value
def greeting2(name: String)={
  def sayHello(name: String):String ={
    return "Hello, " + name
  }
  sayHello(name)
}
//------------------------------------------------------------------
