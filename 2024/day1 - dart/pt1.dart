import 'dart:io';
void main(){
  var totalDistance = 0;
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
  rightList.sort();
  leftList.sort();
  for (var i=0; i<leftList.length; i++){
    var distance = rightList[i]-leftList[i];
    if (distance<0){
      distance= -1*(distance);
    }
    totalDistance+=distance;
  }
  print(totalDistance);
}