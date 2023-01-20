# from third_app.models import *
# import telebot
# from telebot import types
# def menu(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton('/Curators')
#     button2 = types.KeyboardButton('/Faculties')
#     button3 = types.KeyboardButton('/Departments')
#     button4 = types.KeyboardButton('/Groups')
#     button5 = types.KeyboardButton('/GroupsCurators')
#     button6 = types.KeyboardButton('/Students')
#     button7 = types.KeyboardButton('/Subjects')
#     button8 = types.KeyboardButton('/Teachers')
#     button9= types.KeyboardButton('/GroupsStudents')
#     button10=types.KeyboardButton('/Lectures')
#     button11=types.KeyboardButton('/GroupsLectures')
#     keyboard.add(button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11)
#     botler.send_message(message.chat.id,'Menu:',reply_markup=keyboard)
# config = {
#     'name': 'BanVital_bot',
#     'token': '5787697902:AAHmBf2JqZGctl3zbwunMgfBQVvhxXEUfI8'
# }
# botler = telebot.TeleBot(config['token'])
#
#
# @botler.message_handler(commands=['start'])
# def start(message):
#     menu(message)
#
#
# @botler.message_handler(content_types=['text'])
# def get_text(message):
#     if message.text == "/Curators":
#         academy = Curators.objects.all()
#         curators=""
#         for i in academy:
#             curators=curators+f'Name: {i.name}, Surname: {i.surname}\n'
#         botler.send_message(message.chat.id, curators)
#     if message.text == "/Faculties":
#         academy = Faculties.objects.all()
#         curators = ""
#         for i in academy:
#             curators =curators + f'Name: {i.name}\n'
#         botler.send_message(message.chat.id, curators)
#     if message.text == "/Departments":
#         academy = Departments.objects.all()
#         curators = ""
#         for i in academy:
#             curators = curators + f'Name: {i.name}, Building: {i.building}, Financing: {i.financing}, FacultID: {i.facultyId}\n'
#         botler.send_message(message.chat.id, curators)
#     if message.text == "/Groups":
#         academy = Groups.objects.all()
#         curators = ""
#         for i in academy:
#             curators = curators + f'Name: {i.name}, Year: {i.year}, Departamentid: {i.departamentid}\n'
#         botler.send_message(message.chat.id, curators)
#     if message.text == "/GroupsCurators":
#         academy = GroupsCurators.objects.all()
#         curators = ""
#         for i in academy:
#             curators = curators + f'CuratorId: {i.curatorId}, GroupId: {i.groupId}\n'
#         botler.send_message(message.chat.id, curators)
#     if message.text == "/Students":
#         academy = Students.objects.all()
#         curators = ""
#         for i in academy:
#             curators = curators + f'Name: {i.name}, Surname: {i.surname}, Rating: {i.rating}\n'
#         botler.send_message(message.chat.id, curators)
#     if message.text == "/Subjects":
#         academy = Subjects.objects.all()
#         curators = ""
#         for i in academy:
#             botler.send_message(message.chat.id, f'Name: {i.name}\n')
#     if message.text == "/Teachers":
#         academy = Teachers.objects.all()
#         curators = ""
#         for i in academy:
#             curators = curators + f'Name: {i.name}, Surname: {i.surname}, IsProfessor: {i.IsProfessor}, salary: {i.salary}\n'
#         botler.send_message(message.chat.id, curators)
#     if message.text == "/GroupsStudents":
#         academy = GroupsStudents.objects.all()
#         curators = ""
#         for i in academy:
#             curators = curators + f'GroupId: {i.groupId}, StudentId: {i.studentId}\n'
#         botler.send_message(message.chat.id, curators)
#     if message.text == "/Lectures":
#         academy = Lectures.objects.all()
#         curators = ""
#         for i in academy:
#             curators = curators + f'Date: {i.date}, SubjectId: {i.subjectId}, TeacherId: {i.teacherId}\n'
#         botler.send_message(message.chat.id, curators)
#     if message.text == "/GroupsLectures":
#         academy = GroupsLectures.objects.all()
#         curators = ""
#         for i in academy:
#             curators = curators + f'CuratorId: {i.curatorId}, GroupId:{i.groupId}\n'
#         botler.send_message(message.chat.id, curators)
#
# botler.polling(none_stop=True,interval=0)
