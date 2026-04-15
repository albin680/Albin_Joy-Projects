echo "enter the first number"
read a
echo "enter the second number"
read b
s=$(($a+$b))
a=$(($s/2))
echo "sum="$s
echo "average="$a

