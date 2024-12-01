import 'dart:io';
void main(){
  var total = 0;
  final leftList =<int>[];
  final rightList =<int>[];
  
  final doc = File('input.txt').readAsLinesSync();
  for (var line in doc){
    final cleanLine = line.split("   ");
    final lListNum = int.parse(cleanLine[0]);
    final rListNum = int.parse(cleanLine[1]);
    leftList.add(lListNum);
    rightList.add(rListNum);
  }
  for (var lNum in leftList){
    var multiplier = 0;
    for (var rNum in rightList){
      if(rNum == lNum){
        multiplier +=1;
      }
    }
    total += lNum*multiplier;
  }
  print(total);
}