import math

def get_radius(prompt):
 r = int(input(prompt))
 return r

def get_circle_area(r):
    area = math.pi*(r**2)
    return area

def main():
    radius=get_radius("넓이를 구하고자 하는 원의 반지름은?")
    
    area = get_circle_area(radius)

    print("반지름이", radius,"인 원의 넓이=",area)
    
if __name__=="__main__":
    main()

input()
