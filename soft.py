import datetime

class allwork():
    def __init__(self):
       pass
    def Works(self):
     while True:
         print("-------------------------------------------------------------------------------")
         z = datetime.datetime.now()
         print("Today is : " + z.strftime("%A"))
         print("Now is : " + z.strftime("%I,%M,%S,%p") + " O'clock")
         Works = {
            "First work": "Waking Up and Eating Morning Tea ---> 6:00am up to 8:00am : ",
            "Second work": "Repeat Past Lessons ---> 8:00am up to 10:00am : ",
            "Third work": "Go to the course and Coming ---> 11:00am up to 1:00am : ",
            "Fourth work": "Repeat new Lessons ---> 2:00pm up to 5:00pm : ",
            "Fifth work": "Eat Night Bread ---> 7:00pm up to 8:00pm : ",
            "Sixth work": "Going to Bed ---> 10:00pm : "
         }
         s = str(input(Works["First work"]))
         s1 = str(input(Works["Second work"]))
         s2 = str(input(Works["Third work"]))
         s3 = str(input(Works["Fourth work"]))
         s4 = str(input(Works["Fifth work"]))
         s5 = str(input(Works["Sixth work"]))

         x = ["First Work is :", s], ["Second Work is :", s1], ["Third Work is :", s2], ["Fourth Work is :", s3], ["Fifth Work is :", s4], ["Sixth Work is :", s5]
         for i in x:
             print(i)
         boo = input("Do you Want to Add a new Work :\n[1]:yes \n[2]:No ")
         if boo.__eq__('yes'):
              num = int(input('How Many Work Do you want to Add: '))
              v = 0
              while v < num:
                  name = input('Enter A Name for your work : ')
                  xa = str(input('Write Your Work :'))
                  Works[name] = xa
                  v +=1
         else:
              print('Have a Good day')

         for i in Works.items():
             print(i)
         update= input('Do You want to Update the work :\n[1]:Yes \n[2]:No ')
         if update.__eq__('yes'):
             for i in Works.items():
                 print(i)
             chosse=input('Which Work do You want to Update : ')
             chosse2=input('Enter The Work : ')
             Works.update({chosse:chosse2})
             for i in Works.items():
                 print(i)
         b001 = input('Do you want to Delete Any new Work :\n[1]:Yes \n[2]:No ')
         if b001.__eq__('yes'):
              for i in Works.items():
                  print(i)
              sol=input('Which Work do want to Delete : ')
              del Works[sol]
              for i in Works.items():
                  print(i)
         else:
               print('Not Important')
         body =input('Do You Want to Stop this :')
         if body.__eq__("stop"):
                break

    def Todolast(self):
      while True:
        print("-------------------------------------------------------------------------------")
        z = datetime.datetime.now()
        print("Today is : " + z.strftime("%A"))
        print("Now is : " + z.strftime("%I,%M,%S,%p") + " O'clock")
        name = input('What is your name please :')
        x = input('In the First When You wakeup in morning You Most Doing What :')
        if x.__eq__('prayer'):
            #print('You Answer is Correct.')
            n = int(input(
                'After pray You Have Two Option : \n [1]: In the First You Exercise . \n [2]: In the Second You Eat Breakfast.'))
            if n == 1:
                print('This Option can be Useful to Body.')
            elif n == 2:
                print('This Option can be Useful to Your Stomach.')
        else:
            print('You Begin Your day Now With ' + x)
        y = input('You Went to the course and Come to the home in A Specific Time and that time is :')
        o = y[0]
        p = y[1] + o
        v = y[6]
        An = ['I Went to Course in ' + p + 'O Clock' + 'And Come Form Course in ' + v + 'O Clock']

        At = int(input('After Come From Course in ' + v + ':00 O clock' + ' Again You Have Two Option : \n [1]: In the First You Can Sleep \n [2]: In the Second You Can Reapet Your Lesson.'))
        if At == 1:
            print('In this Option can help You to your Mind Become Comfortable.')
        elif At == 2:
            print('In this Option Can be Useful for your Future')
        print('After This You can Doing Every think')
        k = input('Every Think you Want write :')
        if k.__eq__('playing football'):
            print('It is Good.')
        else:
            print('You are Base of Yourself.')
        i = int(input('Now the day is Finish and Night come Which Time do you want to sleep : '))
        print('Good Night Mr ' + name)
        name1 = 'Your name is ' + name
        name2 = 'In the Begining of day you Do ' + x
        name3 = 'Your Course Time is ', p, 'to', v
        name4 = 'After You come Form Course Sleep'
        name5 = 'After That You Doing ' + k
        name6 = 'Your Sleep Time is ', i, 'O Clock'
        Total = input('If your Want to See The All Works In this day Press ok :')
        if Total.__eq__('ok'):
            print(name1)
            print(name2)
            print(name3)
            print(name4)
            print(name5)
            print(name6)
        else:
            print('Not Important')
        body = input('Do You Want to Stop this :')
        if body.__eq__("stop"):
            break
        print("----------------------------------------------------------------------------------")

x =allwork()
x.Works()
x.Todolast()