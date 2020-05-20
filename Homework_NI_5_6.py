# Задание 6
subj = {}
with open('5_6.txt', 'r') as init_f:
    for line in init_f:
        for el in line:
            if el in "—-":
                line = line.replace(el, '0')
        subject, lecture, practice, lab = line.split()
        subject = subject.strip(':')
        lecture = lecture.strip('(л)—-')
        practice = practice.strip('(пр)—-')
        lab = lab.strip('(лаб)—-')
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')