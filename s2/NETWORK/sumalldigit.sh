sum_of_digits() {  
number=$1 
sum=0 
while [ $number -gt 0 ]; do 
digit=$((number % 10))   
sum=$((sum + digit))        
number=$((number / 10))   
done    
echo "Sum of Digits: $sum"
}
read -p "Enter a number: " input_number
sum_of_digits $input_number
