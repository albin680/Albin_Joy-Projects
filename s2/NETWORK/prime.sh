echo"enter the number"
read a
s=1
for((i=2;i<=$a;i++))
do
e= $(($a%$i))
if [ $e -eq 0]
then 
 s = $((s+1))
fi
done
 if[ $s -eq 2]
then
 echo" number is prime"
else
echo"number is not prime"
fi 
