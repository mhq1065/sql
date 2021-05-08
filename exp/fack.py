from faker import Faker
import random
fake = Faker(locale='zh_CN')
# stu
startStuNum = 11032010
stu_range = list(range(startStuNum+1, startStuNum+1001))
# course
startCourseEE = 1
startCourseCS = 1
startCourseAUTO = 1
startCourseMATH = 1
with open('course_name.txt') as f:
    course_names = f.read().splitlines()


def getStuItem():
    # 随机生成学生信息
    # S#，
    # SNAME，
    # SEX，
    # BDATE，
    # HEIGHT，
    # DORM
    def getSex():
        return random.choice(['男', '女'])

    def getHeight():
        t = random.randint(50, 95)
        return '1.'+str(t)

    def getDorm():
        m = random.choice(['东', '西'])
        q = str(random.randint(1, 20))
        p = str(random.randint(100, 1000))
        return m+q+'舍'+p

    def getS():
        global startStuNum
        startStuNum += 1
        return str(startStuNum)

    return getS(), fake.name(), getSex(), str(fake.date_of_birth()), getHeight(), getDorm()


def getCourseItem():
    # 随机生成课程信息
    #   C#
    # 	CNAME
    # 	PERIOD
    # 	CREDIT
    # 	TEACHER
    def getC():
        n = random.choice(['EE', 'CS', 'AUTO', 'MATH'])
        if n == 'EE':
            global startCourseEE
            startCourseEE += 1
            return n+'-'+str(startCourseEE)
        elif n == 'CS':
            global startCourseCS
            startCourseCS += 1
            return n+'-'+str(startCourseCS)
        elif n == 'AUTO':
            global startCourseAUTO
            startCourseAUTO += 1
            return n+'-'+str(startCourseAUTO)
        elif n == 'MATH':
            global startCourseMATH
            startCourseMATH += 1
            return n+'-'+str(startCourseMATH)
        else:
            print("not found course")
            return

    def getCourse():
        return random.choice(course_names)

    def getPERIOD():
        return str(random.randint(20, 100))

    def getCREDIT():
        return str(random.randint(2, 20)/2)

    return getC(), getCourse(), getPERIOD(), getCREDIT(), fake.name()


def generateStu():
    # 将随机信息写入文件
    with open("stu.csv", "w+") as f:
        f.write("S#,SNAME,SEX,BDATE,HEIGHT,DORM\n")
        # 写入1k数据
        for i in range(5000):
            f.write(','.join(getStuItem())+'\n')


def generateCourse():
    # 将随机信息写入文件
    with open("course.csv", "w+") as f:
        f.write("C#,CNAME,PERIOD,CREDIT,TEACHER\n")
        # 写入150数据
        for i in range(1500):
            f.write(','.join(getCourseItem())+'\n')


def generateGrades(stu, course):
    with open("grades.csv", "w+") as f:
        f.write("S#,C#,GRADE\n")
        # 写入5k数据
        for i in range(20000):
            t = [str(random.choice(stu)), random.choice(
                course),str(random.randint(0, 1000)/10)]
            f.write(','.join(t)+'\n')
    return


if __name__ == "__main__":
    generateStu()
    generateCourse()
    with open("course.csv") as coursefile:
        course = coursefile.read().splitlines()
        # 去除标题行，过滤获取C#
        courseID = list(map(lambda s: s.split(',')[0], course[1:]))
    generateGrades(stu_range, courseID)
