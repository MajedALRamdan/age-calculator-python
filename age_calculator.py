from datetime import date


def get_dob(year, month, day):
    # write code here
	...
year=int(input("Enter year of birth: "))
month=int(input("Enter month of birth: "))
day=int(input("Enter day of birth:"))
dob=date(year,month,day)


def get_age(dob):
    # write code here
	...
today=date.today()
age=today-dob
aiy=str(age.days//365)
if age.days//365<0:
	print("Invalid date of birth")
else:
	print(f"You are {aiy} years old")
 


def main():
	# write code here
	...


if __name__ == '__main__':
    main()
