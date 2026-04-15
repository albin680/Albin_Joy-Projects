reverse_number() {
 number=$1
 reversed=""
 while [ $number -gt 0 ]; do
  digit=$((number % 10))
  reversed="${reversed}${digit}"
  number=$((number / 10))
 done
  echo "Reversed Number: $reversed"
}
read -p "Enter a number: " input_number
reverse_number $input_number
