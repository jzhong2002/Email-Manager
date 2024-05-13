import tkinter.messagebox


from message import Message

messages = {}
messages[1] = Message("Chris@redwich.ac.uk", "Hello", "Kate@redwich.ac.uk", "How is the course going?", "Done", 2)
messages[2] = Message("Kate@redwich.ac.uk", "Re: Hello", "Chris@redwich.ac.uk",
                      "> How is the course going?\n\nBrilliant, thanks. The students are all fantastic and are going to get top marks in their coursework.", "Done",
                      2)
messages[3] = Message("A.Friend@hmail.com", "Coffee", "Chris@redwich.ac.uk",
                      "You're working too hard - fancy meeting for coffee?.", "ToDo", 5)
messages[4] = Message("Chris@redwich.ac.uk", "Exam", "Asif@redwich.ac.uk",
                      "I have nearly finished writing the exam - I hope the students have revised hard.", "Done", 4)
messages[5] = Message("A.Student@redwich.ac.uk", "Timetable", "Chris@redwich.ac.uk",
                      "help!!! my timetable is rubbish - i cant understand it!!! what r u going to do?", "ToDo", 0)
messages[6] = Message("Chris@redwich.ac.uk", "Re: Timetable", "A.Student@redwich.ac.uk",
                      "Please follow the advice on Moodle - all will be clear.", "Done", 0)
messages[7] = Message("A.Student@redwich.ac.uk", "Re: Timetable", "Chris@redwich.ac.uk", "thx :)", "ToDo", 0)


def list_all(label=None):
    output = "ID Priority From                      Label Subject\n" \
             "== ======== ====                      ===== =======\n"
    for message_id in messages:
        message = messages[message_id]
        if label is not None and (len(label) == 0 or label not in message.label):
            continue
        output += f"{message_id:2d} {message.info()}\n"
    return output


def get_sender(message_id):
    try:
        message = messages[message_id]
        return message.sender
    except KeyError:
        return None


def get_recipient(message_id):
    try:
        message = messages[message_id]
        return message.recipient
    except KeyError:
        return None


def get_subject(message_id):
    try:
        message = messages[message_id]
        return message.subject
    except KeyError:
        return None


def get_content(message_id):
    try:
        message = messages[message_id]
        return message.content
    except KeyError:
        return None


def get_priority(message_id):
    try:
        message = messages[message_id]
        return message.priority
    except KeyError:
        return -1


def set_priority(message_id, priority):
    try:
        message = messages[message_id]
        message.priority = priority
    except KeyError:
        return


def get_unread(message_id):
    try:
        message = messages[message_id]
        return message.unread
    except KeyError:
        return -1


def set_label(message_id, label):
    try:
        user_id = message_id
        for message_id, value in messages.items():
            if user_id != message_id:
                tkinter.messagebox.showwarning("WARNING", "Can not find message ID" + f"{user_id}")
                run_once = 1
                tkinter.msgbox = tkinter.messagebox.run_once, "The Warning box will pop up once to show error and close"
        message = messages[message_id]
        message.label = label
    except ValueError:
        return


def set_unread(message_id, unread):
    try:
        message = messages[message_id]
        message.unread = unread
    except KeyError:
        return


def delete_message(message_id):
    try:
        messages.pop(message_id)
    except KeyError:
        return


def new_message(sender, recipient, subject, content):
    # find the next empty message_id
    message_id = 0
    for message_id in messages:
        continue
    message_id += 1
    messages[message_id] = Message(sender, subject, recipient, content, 0)
