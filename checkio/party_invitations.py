class Friend():
    def __init__(self, name):
        self.name = name
        self.invite_text = 'No party...'

    def get_invite(self, invite_text: str):
        self.invite_text = invite_text

    def show_invite(self):
        return self.invite_text


class Party():
    def __init__(self, place):
        self.place = place
        self.friends_list = []

    def add_friend(self, friend: Friend):
        self.friends_list.append(friend)

    def del_friend(self, friend: Friend):
        self.friends_list.remove(friend)

    def send_invites(self, invite_text: str):
        for friend in self.friends_list:
            friend.get_invite(f'{self.place}: {invite_text}')


party = Party("Midnight Pub")
nick = Friend("Nick")
john = Friend("John")
lucy = Friend("Lucy")
chuck = Friend("Chuck")

party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.send_invites("Friday, 9:00 PM")
party.del_friend(nick)
party.send_invites("Saturday, 10:00 AM")
party.add_friend(chuck)

print(john.show_invite()) #"Midnight Pub: Saturday, 10:00 AM"
print(lucy.show_invite()) #"Midnight Pub: Saturday, 10:00 AM"
print(nick.show_invite()) #"Midnight Pub: Friday, 9:00 PM"
print(chuck.show_invite()) #"No party..."