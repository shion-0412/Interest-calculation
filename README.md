# Interest-calculation
You can calculate the total repayment amount with interest rate.

# How to use
Type "python repayment.py [ganri] or [gankin]" on your command line.  
In both cases, you will be required to type the principal, the number of repayment, the interest rate.  
After it, a list of every set of the number and the repayment amount, the interest amount, the remains are displayed, and then the amount of every repayment and total repayment, total interest are displayed under the list.

# Mode explanation
・ganri
In "ganri" mode, you can calculate repayment of principal and interest equal system.
If you want to repay same amount in every time until you complete payment, it's better for you to use this mode.

・gankin
In "gankin" mode, you can calculate repayment of capital equal system.
If you use this one, you can keep total repayment low.

# Install
```
git clone https://github.com/shion-0412/Interest-calculation.git
```

# Example
 
```:ganri
##Input##
python repayment.py ganri
type the principal (yen): [PUT-PRINCIPAL-HERE]
type the number of repayment: [PUT-NUMBER-HERE]
type the interest rate (%): [PUT-PERCENTAGE-HERE]
##Output##
time--repayment--interest--remains
Every repayment: *** yen.
Total repayment: *** yen.
 Total interest: *** yen.
 ```
 
 ```:gankin
##Input##
python repayment.py gankin
type the principal (yen): [PUT-PRINCIPAL-HERE]
type the number of repayment: [PUT-NUMBER-HERE]
type the interest rate (%): [PUT-PERCENTAGE-HERE]
##Output##
time--repayment--interest--remains
Total repayment: *** yen.
 Total interest: *** yen.
```
