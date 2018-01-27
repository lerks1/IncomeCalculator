#NZ Income Tax Calculator - Written 09/2015 (settings current as of 01/2018) - John Lerke. Validate against https://www.paye.net.nz/calculator.html.

#r1, r2 etc = Salary tax brackets.
def Tax_Deductions (s):
    if s > 70000:
        b1 = s - 70000
        b2 = 22000
        b3 = 34000
        b4 = 14000
    if s > 48000 and s <= 70000:
        b1 = 0
        b2 = s - 48000
        b3 = 34000
        b4 = 14000
    if s > 14000 and s <= 48000:
        b1 = 0
        b2 = 0
        b3 = s - 14000
        b4 = 14000
    if s <= 14000:
        b1 = 0
        b2 = 0
        b3 = 0
        b4 = s
    
    d =(b1 * .33) + (b2 * .3) + (b3 * .175) + (b4 * .105)
    return d

def Student_Loan_Deductions (s, b):
    if not b:
        d = 0
    elif s <= 19136:
        d = 0
    else:
        t = s - 19136
        d = t * .12
    return d

def KiwiSaver_Deductions (s, b): 
    r = b / 100.0
    d = s * r
    return d

def ACC_Levy_Deductions (s):
    if s >= 124053:
        d = 124053 * 0.0139
    else:
        d = s * 0.0139
    return d

#Parameters a = salary, b = kiwisaver percentage, c = student loan (1 = yes, 0 = no).
def Annual_Salary_After_Tax (a, b, c):
    q = Tax_Deductions (a)
    w = Student_Loan_Deductions (a, c)
    r = KiwiSaver_Deductions (a, b)
    n = ACC_Levy_Deductions (a)
    s = a - q - w - r - n
    return s


#Example = $50,000 p.a with 3% kiwisaver and a student loan.
sat = Annual_Salary_After_Tax (50000, 3, 1)

print ("Annual Salary After Tax: ", sat)
print ("Weekly: ", sat/52)
print ("Fortnightly: ", sat/26)






    
    
    
        
    


        
