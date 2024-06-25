def savings(gross_pay, tax_rate, expenses):
    
    total = (gross_pay - (gross_pay*tax_rate)) // 1 - expenses
    return int(total)

def material_waste(total_material, material_units, num_jobs, job_consumption):
   
    waste = num_jobs*job_consumption
    remaining_material =  total_material - waste
    return str(remaining_material) + material_units

def interest(principal, rate, periods):
    
    final_value = (principal + (principal  * (rate*periods))) // 1
    return int(final_value)