class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    return self.name + "'s estimated insurance cost is " + str(estimated_cost) + " dollars."

# UPDATED AGE
  def update_age(self, new_age):
    self.age = new_age
    return self.name + " is now " + str(self.age) + " years old."

    return self.estimated_insurance_cost()

# UPDATED NUMBER OF CHILDREN
  def update_num_of_children(self, new_num_of_children):
    self.num_of_children = new_num_of_children

    if self.num_of_children == 1:
      return self.name + " has " + str(self.num_of_children) + " child."
    else:
      return self.name + " has " + str(self.num_of_children) + " children."

    return self.estimated_insurance_cost()

# STORING PATIENT DATA
  def patient_profile(self):
    patient_data = {}
    patient_data["Name"] = self.name
    patient_data["Age"] = self.age
    patient_data["Sex"] = self.sex
    patient_data["BMI"] = self.bmi
    patient_data["Number of children"] = self.num_of_children
    return patient_data

# METHOD CALLINGS
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)

print(patient1.estimated_insurance_cost())
print(patient1.update_age(26))
print(patient1.estimated_insurance_cost())
print(patient1.update_num_of_children(1))
print(patient1.estimated_insurance_cost())

print(patient1.patient_profile())