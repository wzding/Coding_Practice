/*
exception
*/


try{
  throw new IllegalArgumentException("ddd")
}catch{
  case _: IllegalArgumentException => print("illegal !!")
}finally {
  print("dddjsjes!")
}


try{
  throw new Exception("ddd")
}catch{
  case _: IllegalArgumentException => print("illegal !!")
}finally {
  print("dddjsjes!")
}
