/*
Array & ArrayBuffer
*/


// to use an array that have changable length
import scala.collection.mutable.ArrayBuffer

val b = ArrayBuffer[Int]()
b += 1
b += (2,5,6)
b ++= Array(6,7,7)
b.trimEnd(3)
b
b(2) = 0
b.insert(2, 7,8,9)
b
b.remove(0, 3)
b

var b_a = b.toArray
b_a
var a_b = b_a.toBuffer
a_b
