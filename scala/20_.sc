// implicit conversion function
// naming convention : one2one
class SpecialPerson(val name:String)
class Student(val name: String)
class Older(val name:String)
implicit def object2SpecialPerson(obj: Object):SpecialPerson={
  if(obj.getClass==classOf[Student]){val stu = obj.asInstanceOf[Student]; new SpecialPerson(stu.name)}
  else if (obj.getClass==classOf[Older]){val old = obj.asInstanceOf[Older]; new SpecialPerson(old.name)}
  else Nil
}

var ticketNumber = 0
def buySpecialTicket(p: SpecialPerson)= {
  ticketNumber += 1
  "T-" + ticketNumber
}
val leo = new Student("leo")
buySpecialTicket(leo)
buySpecialTicket(leo)
//------------------------------------------------------------------
// strength existing type
class Man(val name: String)
class Superman(val name: String){
  def emitLaser = println(name + " emits a laser")
}
implicit def man2superman(man:Man): Superman = new Superman(man.name)
// note Man does not have method emitLaser, but scala will search for it
val jack = new Man("jack")
jack.emitLaser
//------------------------------------------------------------------
//import
class TicketHouse{
  var ticketNum = 0
  def buySpecial(p: SpecialPerson)={
    ticketNum += 1
    "T-" + ticketNum
  }
}
val tickethouse = new TicketHouse
tickethouse.buySpecial(leo)
//------------------------------------------------------------------
// implicit parameter
class SignPen{
  def write(content: String) = println(content)
}
implicit val signPen = new SignPen
def signforexam(name: String)(implicit signPen: SignPen){
  signPen.write(name + " is in exam")
}
signforexam("leo")
//------------------------------------------------------------------