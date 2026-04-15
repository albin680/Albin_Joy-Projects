echo "Please enter the first no."
read a
echo "Please enter the second no."
read b
m=$(($a*$b))
echo "mul="$m
c=$(($a-$b))
echo "sub="$c
s=$(($a+$b))
echo "add="$s
v=$(echo "scale=2;($s)/2"|bc)
echo "div="$v

